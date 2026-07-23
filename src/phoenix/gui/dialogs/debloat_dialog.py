from PySide6.QtWidgets import QDialog, QTextEdit, QVBoxLayout

from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.debloat.debloat_engine import DebloatEngine


class DebloatDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.resize(600,450)

        self.setWindowTitle(
            "Safe To Disable"
        )

        layout = QVBoxLayout()

        text = QTextEdit()

        text.setReadOnly(True)

        apps = InventoryEngine().scan()

        safe = DebloatEngine().recommend(
            apps
        )

        output = []

        for app in safe:

            output.append(
                app.name
            )

        text.setPlainText(
            "\n".join(output)
        )

        layout.addWidget(text)

        self.setLayout(layout)