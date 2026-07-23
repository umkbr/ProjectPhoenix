from PySide6.QtWidgets import (
    QDialog,
    QTextEdit,
    QVBoxLayout,
)

from phoenix.core.inspection_engine import InspectionEngine
from phoenix.health.health_engine import HealthEngine


class DoctorDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Phoenix Doctor")

        self.resize(650, 450)

        layout = QVBoxLayout()

        text = QTextEdit()
        text.setReadOnly(True)

        report = InspectionEngine().inspect()
        health = HealthEngine().evaluate(report)

        output = []

        output.append("=" * 45)
        output.append("PROJECT PHOENIX DOCTOR")
        output.append("=" * 45)
        output.append("")
        output.append(f"Model : {report.device.model}")
        output.append(f"Android : {report.device.android_version}")
        output.append(f"Health Score : {health.score}")
        output.append("")
        output.append("Recommendations")
        output.append("-" * 45)

        if health.recommendations:

            for item in health.recommendations:
                output.append(f"• {item.title}")

        else:

            output.append("No recommendation")

        text.setPlainText("\n".join(output))

        layout.addWidget(text)

        self.setLayout(layout)