import os
import subprocess
import time
import glob
import xml.etree.ElementTree as ET

def find_xml_files(folder_path):
    """
    遍历文件夹，找到所有文件名包含指定字符串的 .ts 文件
    :param folder_path: 文件夹路径
    :param search_string: 要搜索的字符串
    :return: 包含指定字符串的 .ts 文件列表
    """
    # 初始化结果列表
    matching_files = []

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件名是否为xml文件
        if filename.endswith(".xml"):
            # 构建完整文件路径，并添加到结果列表中
            matching_files.append(os.path.join(folder_path, filename))

    return matching_files

def merge_ts_files(ts_filenames, merged_ts_filename):
    """
    合并多个 .ts 文件
    :param ts_filenames: 要合并的 .ts 文件列表
    :param merged_ts_filename: 合并后的 .ts 文件名
    """
    # 创建一个新的 XML 树
    merged_tree = ET.ElementTree(ET.Element("TS", version="2.1"))
    merged_root = merged_tree.getroot()

    # 遍历所有 .ts 文件
    for ts_filename in ts_filenames:
        if not os.path.isfile(ts_filename):
            print(f"File {ts_filename} does not exist.")
            continue
        
        try:
            tree = ET.parse(ts_filename)
            root = tree.getroot()
        except ET.ParseError as e:
            print(f"Error parsing {ts_filename}: {e}")
            continue
        
        # 遍历文件中的所有 context
        for context in root.findall('context'):
            merged_root.append(context)

    # 将合并后的内容写入到合并文件中
    ET.indent(merged_tree, space="    ", level=0)  # 自动缩进
    merged_tree.write(merged_ts_filename, encoding='utf-8', xml_declaration=True)
    
    # 手动插入 <!DOCTYPE TS> 在文件开头
    with open(merged_ts_filename, 'r+', encoding='utf-8') as file:
        content = file.read()
        file.seek(0, 0)
        file.write('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE TS>\n' + content[content.find('<TS'):])

def generate_qm(ts_filename, qm_filename):
    """
    将 .ts 文件编译为 .qm 文件
    :param ts_filename: 输入的 .ts 文件路径
    :param qm_filename: 输出的 .qm 文件路径
    """
    if not os.path.isfile(ts_filename):
        print("ts文件不存在")
        return
    # 拼接命令
    command = ['pyside6-lrelease', ts_filename, '-qm', qm_filename]

    # 执行命令
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    if result.returncode == 0:
        print(f"成功生成 {qm_filename}")
    else:
        print(f"生成 {qm_filename} 失败: {result.stderr}")

def relative_path(path):
    '''
    path: 相对路径
    返回相对路径或exe运行时的临时目录下的此路径
    '''
    base_dir = ""
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    return os.path.join(base_dir, path)

if __name__ == "__main__":
    ts_config = {
        "xml_dir": "res\\ts\\model",
        "ts_dir": "res\\ts",
        "qm_dir": "res\\qm",
        "languages": ["en", "zh_CN"]
    }
    
    for lan in ts_config["languages"]:
        xml_dir = relative_path(ts_config["xml_dir"] + "\\" + lan)
        ts_filename = relative_path(ts_config["ts_dir"] + "\\" + lan + ".ts")
        qm_filename = relative_path(ts_config["qm_dir"] + "\\" + lan + ".qm")

        xml_files = find_xml_files(xml_dir)
        merge_ts_files(xml_files, ts_filename)
        generate_qm(ts_filename, qm_filename)