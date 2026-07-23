from PySide6.QtWidgets import QDialog, QTextEdit, QVBoxLayout

from phoenix.inventory.inventory_engine import InventoryEngine


class InventoryDialog(QDialog):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Installed Apps")

        self.resize(600,500)

        layout = QVBoxLayout()

        text = QTextEdit()

        text.setReadOnly(True)

        apps = InventoryEngine().scan()

        output = []

        for app in apps:

            state = "SAFE" if app.safe_disable else "KEEP"

            output.append(
                f"{state:5}  {app.name}"
            )

        text.setPlainText(
            "\n".join(output)
        )

        layout.addWidget(text)

        self.setLayout(layout)