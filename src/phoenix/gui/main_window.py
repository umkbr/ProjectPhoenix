from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
)

from PySide6.QtCore import QTimer

from phoenix.core.inspection_engine import InspectionEngine

from phoenix.gui.actions import (
    show_doctor,
    show_inventory,
    show_recommend,
    show_debloat,
    show_history,
)

from phoenix.gui.output_panel import OutputPanel


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Project Phoenix")

        self.resize(900, 650)

        self.inspection = InspectionEngine()

        main_layout = QVBoxLayout()

        title = QLabel("PROJECT PHOENIX")
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        main_layout.addWidget(title)

        # ==========================
        # Device
        # ==========================

        device_box = QGroupBox("Connected Device")

        device_layout = QVBoxLayout()

        self.device_label = QLabel("Loading...")

        device_layout.addWidget(self.device_label)

        device_box.setLayout(device_layout)

        main_layout.addWidget(device_box)

        # ==========================
        # Buttons
        # ==========================

        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        self.doctor_button = QPushButton("Doctor")
        self.inventory_button = QPushButton("Inventory")
        self.recommend_button = QPushButton("Recommend")

        self.debloat_button = QPushButton("Debloat")
        self.restore_button = QPushButton("Restore")
        self.history_button = QPushButton("History")

        row1.addWidget(self.doctor_button)
        row1.addWidget(self.inventory_button)
        row1.addWidget(self.recommend_button)

        row2.addWidget(self.debloat_button)
        row2.addWidget(self.restore_button)
        row2.addWidget(self.history_button)

        main_layout.addLayout(row1)
        main_layout.addLayout(row2)

        # ==========================
        # Output Panel
        # ==========================

        self.output = OutputPanel()

        main_layout.addWidget(self.output)

        self.setLayout(main_layout)

        # ==========================
        # Signal
        # ==========================

        self.doctor_button.clicked.connect(
            lambda: show_doctor(self)
        )

        self.inventory_button.clicked.connect(
            lambda: show_inventory(self)
        )

        self.recommend_button.clicked.connect(
            lambda: show_recommend(self)
        )

        self.debloat_button.clicked.connect(
            lambda: show_debloat(self)
        )

        self.history_button.clicked.connect(
            lambda: show_history(self)
        )

        self.restore_button.clicked.connect(
            lambda: self.output.write(
                "Restore feature coming soon..."
            )
        )

        # ==========================
        # Auto Refresh
        # ==========================

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.refresh_device
        )

        self.timer.start(2000)

        self.refresh_device()

    def refresh_device(self):

        try:

            report = self.inspection.inspect()

            storage = report.storage[-1]

            text = (
                f"Model : {report.device.model}\n"
                f"Android : {report.device.android_version}\n"
                f"Battery : {report.battery.level}%\n"
                f"RAM Free : {report.memory.available_kb // 1024} MB\n"
                f"Storage Free : {storage.available_kb // 1024} MB\n\n"
                "🟢 Connected"
            )

        except Exception:

            text = (
                "No Device\n\n"
                "🔴 Disconnected"
            )

        self.device_label.setText(text)