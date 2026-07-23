from PySide6.QtWidgets import QDialog, QTextEdit, QVBoxLayout

from phoenix.core.inspection_engine import InspectionEngine
from phoenix.health.health_engine import HealthEngine


class DoctorDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Phoenix Doctor")
        self.resize(500, 350)

        layout = QVBoxLayout()

        text = QTextEdit()
        text.setReadOnly(True)

        report = InspectionEngine().inspect()
        health = HealthEngine().evaluate(report)

        output = []

        output.append(f"Health Score : {health.score}")
        output.append("")
        output.append("Recommendations")
        output.append("-------------------------")

        for item in health.recommendations:
            output.append(item.title)

        text.setPlainText("\n".join(output))

        layout.addWidget(text)

        self.setLayout(layout)