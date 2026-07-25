from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QTextEdit,
)

from phoenix.history.history_manager import HistoryManager


class HistoryPage(QWidget):

    def __init__(self):

        super().__init__()

        self.manager = HistoryManager()

        layout = QVBoxLayout()

        self.transactions = QListWidget()

        self.detail = QTextEdit()
        self.detail.setReadOnly(True)

        layout.addWidget(self.transactions)
        layout.addWidget(self.detail)

        self.setLayout(layout)

        self.transactions.currentTextChanged.connect(
            self.load_transaction
        )

        self.refresh()

    def refresh(self):

        self.transactions.clear()

        for tx in self.manager.list():

            self.transactions.addItem(tx["id"])

    def load_transaction(self, tx_id):

        if not tx_id:
            return

        transaction = self.manager.load(tx_id)

        if transaction is None:
            return

        lines = []

        lines.append(f"Transaction : {transaction.id}")
        lines.append("")

        for item in transaction.results:

            status = "OK" if item.success else "FAILED"

            lines.append(
                f"[{status}] {item.package}"
            )

        self.detail.setPlainText(
            "\n".join(lines)
        )
