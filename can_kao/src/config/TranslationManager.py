from PySide6.QtCore import QCoreApplication, QTranslator, Qt
from PySide6.QtWidgets import QApplication
from globals import relative_path

# relative_path("res/qm/qt_zh_CN.qm"),

class TranslationManager:
    _instance = None
    current_language_index = 0
    _language_items = [
        "English", 
        "简体中文"
        ]
    _language_qms = [
        relative_path('res/qm/en.qm'),
        # relative_path('res/qm/ch.qm')
        relative_path('res/qm/zh_CN.qm')
    ]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.translator = QTranslator()
            cls._instance.set_language(0)  # Default language is English
        return cls._instance

    def set_language(self, language_index:int):
        if 0 <= language_index < len(TranslationManager._language_qms):
            qm_file_path = TranslationManager._language_qms[language_index]
        else:
            # Default to English if language is not supported
            qm_file_path = TranslationManager._language_qms[0]

        if self.translator.load(qm_file_path):
            QApplication.instance().installTranslator(self.translator)
        else:
            print(f"Failed to load translation file for language: {language_index}")

    def tr(self, context, text):
        return QCoreApplication.translate(context, text)


# Usage example
if __name__ == "__main__":
    app = QApplication([])
    translator = TranslationManager()

    # Set language to English
    translator.set_language('en')

    # Example usage of tr() method
    print(translator.tr("context", "Hello"))

    # Set language to Chinese
    translator.set_language('zh')

    # Example usage of tr() method
    print(translator.tr("context", "Hello"))

    app.exec()
