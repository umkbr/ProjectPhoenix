from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
    QGroupBox,
    QPushButton,
    QHBoxLayout,
)

from phoenix.gui.widgets.info_card import InfoCard
from phoenix.gui.widgets.progress_card import ProgressCard


class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Dashboard")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        self.device_box = QGroupBox("Connected Device")

        device_layout = QVBoxLayout()

        self.device_label = QLabel()

        device_layout.addWidget(self.device_label)

        self.device_box.setLayout(device_layout)

        layout.addWidget(self.device_box)

        grid = QGridLayout()

        self.health = InfoCard("Health Score", "--")

        self.battery = ProgressCard("Battery")

        self.memory = ProgressCard("RAM")

        self.storage = ProgressCard("Storage")

        self.total_apps = InfoCard(
            "Installed Apps",
            "--"
        )

        self.recommended_apps = InfoCard(
            "Recommended",
            "--"
        )

        self.last_action = InfoCard(
            "Last Optimization",
            "-"
        )

        grid.addWidget(self.health, 0, 0)
        grid.addWidget(self.battery, 0, 1)
        grid.addWidget(self.memory, 1, 0)
        grid.addWidget(self.storage, 1, 1)

        grid.addWidget(
            self.total_apps,
            2,
            0
        )

        grid.addWidget(
            self.recommended_apps,
            2,
            1
        )

        grid.addWidget(
            self.last_action,
            3,
            0,
            1,
            2
        )

        layout.addLayout(grid)

        action_layout = QHBoxLayout()

        self.quick_optimize_button = QPushButton(
            "⚡ Quick Optimize"
        )

        self.refresh_button = QPushButton(
            "🔄 Refresh"
        )

        action_layout.addWidget(
            self.quick_optimize_button
        )

        action_layout.addWidget(
            self.refresh_button
        )

        layout.addLayout(action_layout)

        layout.addStretch()

        self.setLayout(layout)

    def update_dashboard(
        self,
        device_text,
        battery,
        ram_percent,
        storage_percent,
        health_score,
        ram_text,
        storage_text,
    ):

        self.device_label.setText(device_text)

        self.health.set_value(f"{health_score}/100")

        self.battery.update_value(
            f"{battery} %",
            battery,
        )

        self.memory.update_value(
            ram_text,
            ram_percent,
        )

        self.storage.update_value(
            storage_text,
            storage_percent,
        )

    def update_statistics(

        self,

        installed,

        recommended,

        last_action,

    ):

        self.total_apps.set_value(
            str(installed)
        )

        self.recommended_apps.set_value(
            str(recommended)
        )

        self.last_action.set_value(
            last_action
        )

    def set_connected(

        self,

        connected,

    ):

        self.quick_optimize_button.setEnabled(
            connected
        )

        self.refresh_button.setEnabled(
            True
        )