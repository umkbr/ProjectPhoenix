from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QProgressBar,
)


class ProgressCard(QFrame):

    def __init__(self, title: str):

        super().__init__()

        self.setStyleSheet("""
        QFrame{
            border:1px solid #505050;
            border-radius:10px;
            background:#2f2f2f;
        }

        QLabel{
            border:none;
            background:transparent;
        }

        QProgressBar{
            border:1px solid #444;
            border-radius:6px;
            text-align:center;
            height:18px;
        }

        QProgressBar::chunk{
            background:#00b894;
            border-radius:5px;
        }
        """)

        layout = QVBoxLayout()

        self.title = QLabel(title)

        self.title.setStyleSheet("""
            font-size:13px;
            color:#bbbbbb;
        """)

        self.value = QLabel("--")

        self.value.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
        """)

        self.progress = QProgressBar()

        self.progress.setRange(0, 100)

        layout.addWidget(self.title)
        layout.addWidget(self.value)
        layout.addWidget(self.progress)

        self.setLayout(layout)

    def update_value(self, value, percent):

        self.value.setText(str(value))

        percent = max(0, min(100, int(percent)))

        self.progress.setValue(percent)