from PySide6.QtWidgets import (
    QDialog,
    QTextEdit,
    QVBoxLayout,
)

from phoenix.core.inspection_engine import InspectionEngine


class DeviceDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Device Information")
        self.resize(700, 650)

        layout = QVBoxLayout()

        text = QTextEdit()
        text.setReadOnly(True)

        report = InspectionEngine().inspect()

        storage = report.storage[-1]

        info = f"""
MODEL
-----------------------
{report.device.model}

MANUFACTURER
-----------------------
{report.device.manufacturer}

ANDROID
-----------------------
{report.device.android_version}

FIRMWARE
-----------------------
{report.device.firmware}

FINGERPRINT
-----------------------
{report.device.fingerprint}

CPU ABI
-----------------------
{report.device.abi}

SERIAL
-----------------------
{report.device.serial}

BATTERY
-----------------------
Level : {report.battery.level} %

Status : {report.battery.status}

Temperature : {report.battery.temperature} °C

Voltage : {report.battery.voltage} mV

RAM
-----------------------
Total :
{report.memory.total_kb//1024} MB

Available :
{report.memory.available_kb//1024} MB

STORAGE
-----------------------
Available :
{storage.available_kb//1024} MB

Used :
{storage.used_kb//1024} MB
"""

        text.setPlainText(info)

        layout.addWidget(text)

        self.setLayout(layout)