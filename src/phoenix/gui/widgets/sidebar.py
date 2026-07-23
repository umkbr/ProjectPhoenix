from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
)


class Sidebar(QWidget):

    def __init__(self):

        super().__init__()

        self.setFixedWidth(190)

        layout = QVBoxLayout()

        title = QLabel("PROJECT\nPHOENIX")

        title.setStyleSheet("""
            font-size:20px;
            font-weight:bold;
            padding:15px;
        """)

        layout.addWidget(title)

        self.dashboard_button = QPushButton("🏠 Dashboard")
        self.doctor_button = QPushButton("🩺 Doctor")
        self.inventory_button = QPushButton("📦 Inventory")
        self.recommend_button = QPushButton("💡 Recommend")
        self.debloat_button = QPushButton("🧹 Debloat")
        self.restore_button = QPushButton("♻ Restore")
        self.history_button = QPushButton("🕒 History")
        self.settings_button = QPushButton("⚙ Settings")

        buttons = [

            self.dashboard_button,
            self.doctor_button,
            self.inventory_button,
            self.recommend_button,
            self.debloat_button,
            self.restore_button,
            self.history_button,
            self.settings_button,

        ]

        for button in buttons:

            button.setMinimumHeight(42)

            layout.addWidget(button)

        layout.addStretch()

        self.setLayout(layout)