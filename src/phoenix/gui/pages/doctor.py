from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QListWidget,
    QPushButton,
    QGroupBox,
    QGridLayout,
)

from phoenix.gui.widgets.info_card import InfoCard

from PySide6.QtWidgets import QFormLayout

class DoctorPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Doctor")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        self.health = InfoCard("Health Score", "--")

        layout.addWidget(self.health)

        grid = QGridLayout()

        self.risk = InfoCard(
            "Risk Level",
            "--"
        )

        self.total_recommendations = InfoCard(
            "Recommendations",
            "0"
        )

        grid.addWidget(
            self.risk,
            0,
            0
        )

        grid.addWidget(
            self.total_recommendations,
            0,
            1
        )

        layout.addLayout(grid)

        self.status_box = QGroupBox("Device Status")

        status_layout = QVBoxLayout()

        self.status_label = QLabel("--")

        status_layout.addWidget(self.status_label)

        self.status_box.setLayout(status_layout)

        layout.addWidget(self.status_box)

        self.device_box = QGroupBox(
            "Device Information"
        )

        device_layout = QFormLayout()

        self.model_label = QLabel("--")
        self.android_label = QLabel("--")
        self.battery_label = QLabel("--")
        self.memory_label = QLabel("--")
        self.storage_label = QLabel("--")

        device_layout.addRow(
            "Model",
            self.model_label,
        )

        device_layout.addRow(
            "Android",
            self.android_label,
        )

        device_layout.addRow(
            "Battery",
            self.battery_label,
        )

        device_layout.addRow(
            "Memory",
            self.memory_label,
        )

        device_layout.addRow(
            "Storage",
            self.storage_label,
        )

        self.device_box.setLayout(
            device_layout
        )

        layout.addWidget(
            self.device_box
        )

        self.recommendation_box = QGroupBox("Recommendations")

        recommendation_layout = QVBoxLayout()

        self.recommendation_list = QListWidget()

        recommendation_layout.addWidget(self.recommendation_list)

        self.recommendation_box.setLayout(recommendation_layout)

        layout.addWidget(self.recommendation_box)

        self.refresh_button = QPushButton("Analyze Again")

        self.optimize_button = QPushButton(
            "⚡ Optimize Recommended Apps"
        )

        layout.addWidget(
            self.optimize_button
        )

        layout.addWidget(self.refresh_button)

        layout.addStretch()

        self.setLayout(layout)

    def update_report(self, health_report):

        self.health.set_value(
            f"{health_report.score}/100"
        )

        self.status_label.setText(
            health_report.status
        )

        if health_report.score >= 80:

            risk = "🟢 Safe"

        elif health_report.score >= 60:

            risk = "🟡 Medium"

        else:

            risk = "🔴 Critical"

        self.risk.set_value(risk)

        self.total_recommendations.set_value(

            str(

                len(

                    health_report.recommendations

                )

            )

        )

        self.recommendation_list.clear()

        if not health_report.recommendations:

            self.recommendation_list.addItem(

                "No recommendations."

            )

            return

        for recommendation in health_report.recommendations:

            self.recommendation_list.addItem(

                f"• {recommendation.title}"

            )

    def update_device_info(

        self,

        report,

    ):

        self.model_label.setText(

            report.device.model

        )

        self.android_label.setText(

            report.device.android_version

        )

        self.battery_label.setText(

            f"{report.battery.level}%"

        )

        total = report.memory.total_kb // 1024

        free = report.memory.available_kb // 1024

        self.memory_label.setText(

            f"{free} MB Free / {total} MB"

        )

        storage = report.storage[-1]

        available = storage.available_kb // 1024

        self.storage_label.setText(

            f"{available} MB Free"

        )
    