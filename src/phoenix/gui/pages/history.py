from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class HistoryPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("History")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        layout.addWidget(
            QLabel("History will appear here.")
        )

        layout.addStretch()

        self.setLayout(layout)