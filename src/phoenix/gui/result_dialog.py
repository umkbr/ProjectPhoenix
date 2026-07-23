from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
)


class ResultDialog(QDialog):

    def __init__(self, title, text):

        super().__init__()

        self.setWindowTitle(title)
        self.resize(700, 500)

        layout = QVBoxLayout()

        self.editor = QTextEdit()
        self.editor.setReadOnly(True)
        self.editor.setText(text)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout.addWidget(self.editor)
        layout.addWidget(close_button)

        self.setLayout(layout)