from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
)


class TextDialog(QDialog):

    def __init__(self, title, text):

        super().__init__()

        self.setWindowTitle(title)

        self.resize(700, 500)

        layout = QVBoxLayout()

        editor = QTextEdit()
        editor.setReadOnly(True)
        editor.setPlainText(text)

        layout.addWidget(editor)

        close = QPushButton("Close")
        close.clicked.connect(self.accept)

        layout.addWidget(close)

        self.setLayout(layout)