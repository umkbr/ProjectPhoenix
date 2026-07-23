from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout


class InfoCard(QFrame):

    def __init__(self, title, value=""):

        super().__init__()

        self.setFrameShape(QFrame.Box)

        self.setStyleSheet("""
            QFrame{
                border:1px solid #cccccc;
                border-radius:8px;
                padding:8px;
            }
        """)

        layout = QVBoxLayout()

        self.title = QLabel(title)
        self.title.setStyleSheet("""
            font-size:12px;
            color:gray;
        """)

        self.value = QLabel(value)
        self.value.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
        """)

        layout.addWidget(self.title)
        layout.addWidget(self.value)

        self.setLayout(layout)

    def set_value(self, value):
        self.value.setText(str(value))