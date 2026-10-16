import os
import subprocess
import time
import glob
import xml.etree.ElementTree as ET

def find_ts_files_with_string(folder_path, search_string):
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
        # 检查文件名是否包含指定字符串，并且是 .ts 文件
        if search_string in filename and filename.endswith(".ts"):
            # 构建完整文件路径，并添加到结果列表中
            matching_files.append(os.path.join(folder_path, filename))

    return matching_files

def generate_ts(ts_filename, *paths):
    """
    生成 .ts 文件
    :param ts_filename: 要生成的 .ts 文件名
    :param paths: 目录或文件的路径，可变长度参数
    """
    files_to_process = []
    for path in paths:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.py') or file.endswith(".ui"):
                        files_to_process.append(os.path.join(root, file))
        elif os.path.isfile(path) and path.endswith('.py'):
            files_to_process.append(path)

    if not files_to_process: return

    # for batch_idx in range(0, len(files_to_process), 1):
    #     batch_files = files_to_process[batch_idx: batch_idx+1]
    for batch_idx, batch_files in enumerate(files_to_process):

        # 拼接命令
        command = ['pyside6-lupdate', "-tr-function-alias", "translate+=_translate"]
        # command.extend(batch_files)
        command.append(batch_files)
        command.extend(['-ts', f'{ts_filename}.{batch_idx}.ts'])

        # 执行命令
        print('Command:', ' '.join(command))  # 打印检查命令
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
        relative_file_path = f"{ts_filename}.{batch_idx}.ts"
        ts_content = ""
        if result.returncode == 0:
            with open(relative_file_path, 'r', encoding='utf-8') as ts_file:
                # 读取 .ts 文件的内容
                ts_content = ts_file.read()
            if '<context>' not in ts_content:
                os.remove(relative_file_path) # 删掉没有context内容的ts文件
                continue
            print(f"成功生成 {relative_file_path}")
        else:
            print(f"生成 {relative_file_path} 失败: {result.stderr}")

    return len(files_to_process)

def merge_ts_files_v2(ts_filenames, merged_ts_filename):
    """
    合并多个 .ts 文件
    :param ts_filenames: 要合并的 .ts 文件列表
    :param merged_ts_filename: 合并后的 .ts 文件名
    """
    # 创建一个新的 XML 树
    merged_tree = ET.ElementTree(ET.Element("TS", version="2.1"))
    merged_root = merged_tree.getroot()

    # 用于跟踪已处理的 location 元素，避免重复
    processed_locations = set()

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
            # 获取 context 内所有的 location 元素
            location_elements = context.findall('message/location')
            
            # 如果 context 中的所有 location 元素的组合没有处理过，则添加到合并内容中
            locations = tuple((location.get('filename'), location.get('line')) for location in location_elements)
            if locations not in processed_locations:
                merged_root.append(context)
                processed_locations.add(locations)

    # 将合并后的内容写入到合并文件中
    ET.indent(merged_tree, space="    ", level=0)  # 自动缩进
    merged_tree.write(merged_ts_filename, encoding='utf-8', xml_declaration=True)
    
    # 手动插入 <!DOCTYPE TS> 在文件开头
    with open(merged_ts_filename, 'r+', encoding='utf-8') as file:
        content = file.read()
        file.seek(0, 0)
        file.write('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE TS>\n' + content[content.find('<TS'):])

    if os.path.isfile(merged_ts_filename):
        # 删除原始的分文件
        for ts_file in ts_filenames:
            if ts_file == merged_ts_filename: continue
            os.remove(ts_file)

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

if __name__ == "__main__":
    # # 英文
    ts_filename ="..\\..\\res\\ts\\en.ts" #"res\\ts\\en.ts" # 源ts文件
    qm_filename ="..\\..\\res\\qm\\en.qm" #"res\\qm\\en.qm" # 目标qm文件
    generate_qm(ts_filename, qm_filename)
    # # 中文
    ts_filename ="..\\..\\res\\ts\\zh_CN.ts" # "res\\ts\\zh_CN.ts" # 源ts文件
    qm_filename ="..\\..\\res\\qm\\zh_CN.qm" #"res\\qm\\zh_CN.qm" # 目标qm文件
    paths = ["src/ui", 
             "src/components/DeviceWidget.py", 
             "main.py", 
             "src/view/cue01/systemSettingWidget.py",
             "src/view/cue01/chromaKeyWidget.py",
             "src/view/cue01/colorGenerationWidget.py",
             ]  # 替换为您的实际目录或文件路径

    # file_counts = generate_ts(ts_filename.rstrip(".ts"), *paths) # 分批生成的 ts 文件，获取相关py文件的数量
    # time.sleep(1)
    # ts_list = find_ts_files_with_string("res\\ts", "en")         # 获取ts列表
    # merge_ts_files_v2(ts_list, ts_filename)                    # 合并
    # time.sleep(2) 
    generate_qm(ts_filename, qm_filename)                      # 生成qm文件

''' merge 指令 '''
# pyside6-lupdate -merge res/ts/aaaaa.ts -ts res/ts/aaaaa.ts

# pyside6-lupdate -tr-function-alias translate+=_translate xx.py -ts xx.ts
