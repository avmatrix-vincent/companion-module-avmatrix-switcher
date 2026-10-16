import os

def update_pro_file(pro_path, source_dirs, ts_files, codec='UTF-8'):
    py_files = []

    # 遍历指定的目录，收集所有 .py 文件的相对路径
    for source_dir in source_dirs:
        if os.path.isdir(source_dir):
            for root, _, files in os.walk(source_dir):
                for file in files:
                    if file.endswith(".py"):
                        relative_path = os.path.relpath(os.path.join(root, file), os.path.dirname(pro_path))
                        py_files.append(relative_path.replace("\\", "/"))
        elif os.path.isfile(source_dir) and source_dir.endswith('.py'):
            py_files.append(source_dir)

    # 写入到 .pro 文件
    with open(pro_path, 'w', encoding='utf-8') as pro_file:
        # pro_file.write(f"SOURCE = {' '.join(py_files)}\n")
        # pro_file.write(f"TRANSLATIONS = {' '.join(ts_files)}\n")
        # pro_file.write(f"CODECFORTR = {codec}\n")
        pro_file.write("SOURCE = \\\n")
        pro_file.write(" \\\n".join(py_files))
        pro_file.write("\n\n")

        pro_file.write("TRANSLATIONS = \\\n")
        pro_file.write(" \\\n".join(ts_files))
        pro_file.write("\n\n")

        pro_file.write(f"CODECFORTR = {codec}\n")

if __name__ == "__main__":
    pro_path = "res\\avmatrix.pro"
    source_dirs = [
        "src\\ui",
        "src\\components",
        "src\\view",
        "main.py"
    ]
    ts_files = [
        # "res/ts/en.ts",
        "res/ts/zh_CN.ts",
        # "res/ts/fr.ts"
    ]
    update_pro_file(pro_path, source_dirs, ts_files)
