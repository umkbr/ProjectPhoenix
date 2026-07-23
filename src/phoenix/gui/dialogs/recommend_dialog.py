from PySide6.QtWidgets import QDialog, QTextEdit, QVBoxLayout

from phoenix.core.inspection_engine import InspectionEngine
from phoenix.recommendation.recommendation_engine import RecommendationEngine


class RecommendDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.resize(500,400)

        self.setWindowTitle(
            "Compatible Apps"
        )

        layout = QVBoxLayout()

        text = QTextEdit()

        text.setReadOnly(True)

        report = InspectionEngine().inspect()

        apps = RecommendationEngine().recommend(
            report.device
        )

        output = []

        for app in apps:

            output.append(
                f"{app.score:3}   {app.name}"
            )

        text.setPlainText(
            "\n".join(output)
        )

        layout.addWidget(text)

        self.setLayout(layout)