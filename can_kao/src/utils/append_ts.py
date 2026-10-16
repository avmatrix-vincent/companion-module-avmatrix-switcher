import xml.etree.ElementTree as ET

def merge_ts_files(file1, file2, output_file):
    tree1 = ET.parse(file1)
    root1 = tree1.getroot()
    
    tree2 = ET.parse(file2)
    root2 = tree2.getroot()
    
    for context in root2:
        root1.append(context)
    
    tree1.write(output_file, encoding="utf-8", xml_declaration=True)

merge_ts_files("res/ts/ch.ts", "res/ts/qtbase_zh_CN.ts", "res/ts/zh_CN_new.ts")
