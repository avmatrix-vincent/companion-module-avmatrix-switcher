from PySide6.QtWidgets import QLabel, QLayout

def convert_html_labels_to_hex(widget):
    for child in widget.children():
        if isinstance(child, QLabel):
            text = child.text()
            if text.upper() == "HTML:":
                child.setText("HEX")
        elif child.layout() is not None:
            # 递归遍历子布局
            convert_html_labels_to_hex(child.layout())
        elif hasattr(child, 'children'):
            # 递归遍历子控件
            convert_html_labels_to_hex(child)


def modify_html_to_hex_str(layout):
    for index in range(layout.count()):
        item = layout.itemAt(index)
        if isinstance(item, QLabel):
            if "HTML" in item.widget().text():
                item.widget().setText("HEX")
        elif isinstance(item, QLayout):
            modify_html_to_hex_str(item)