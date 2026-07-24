from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class RestorePage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Restore")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        layout.addWidget(
            QLabel("Restore disabled applications.")
        )

        layout.addStretch()

        self.setLayout(layout)