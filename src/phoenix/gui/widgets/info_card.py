from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class InfoCard(QFrame):

    def __init__(self, title: str, value: str = ""):

        super().__init__()

        self.setStyleSheet("""
            QFrame{
                border:1px solid #505050;
                border-radius:10px;
                background:#2f2f2f;
            }
        """)

        layout = QVBoxLayout()

        self.title = QLabel(title)

        self.title.setStyleSheet("""
            font-size:13px;
            color:#bbbbbb;
            border:none;
            background:transparent;
        """)

        self.value = QLabel(value)

        self.value.setStyleSheet("""
            font-size:26px;
            font-weight:bold;
            border:none;
            background:transparent;
        """)

        layout.addWidget(self.title)
        layout.addWidget(self.value)

        self.setLayout(layout)

    def set_value(self, value):

        self.value.setText(str(value))