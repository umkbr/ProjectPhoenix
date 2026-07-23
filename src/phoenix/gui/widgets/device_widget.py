from PySide6.QtWidgets import QGroupBox
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout


class DeviceWidget(QGroupBox):

    def __init__(self):

        super().__init__("Device")

        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)

    def update(self, report):

        storage = report.storage[-1]

        self.label.setText(
            f"""
Model      : {report.device.model}

Android    : {report.device.android_version}

Battery    : {report.battery.level} %

RAM Free   : {report.memory.available_kb//1024} MB

Storage    : {storage.available_kb//1024} MB
"""
        )