from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QListWidget,
    QPushButton,
    QGroupBox,
)

from phoenix.gui.widgets.info_card import InfoCard


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

        self.status_box = QGroupBox("Device Status")

        status_layout = QVBoxLayout()

        self.status_label = QLabel("--")

        status_layout.addWidget(self.status_label)

        self.status_box.setLayout(status_layout)

        layout.addWidget(self.status_box)

        self.recommendation_box = QGroupBox("Recommendations")

        recommendation_layout = QVBoxLayout()

        self.recommendation_list = QListWidget()

        recommendation_layout.addWidget(self.recommendation_list)

        self.recommendation_box.setLayout(recommendation_layout)

        layout.addWidget(self.recommendation_box)

        self.refresh_button = QPushButton("Analyze Again")

        layout.addWidget(self.refresh_button)

        layout.addStretch()

        self.setLayout(layout)

    def update_report(self, health_report):

        self.health.set_value(f"{health_report.score}/100")

        self.status_label.setText(health_report.status)

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