from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QPushButton,
)


class RestorePage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        self.transactions = QListWidget()

        self.restore_button = QPushButton(
            "Restore Selected"
        )

        layout.addWidget(self.transactions)
        layout.addWidget(self.restore_button)

        self.setLayout(layout)

    def update_transactions(self, ids):

        self.transactions.clear()

        self.transactions.addItems(ids)

    def selected_transaction(self):

        item = self.transactions.currentItem()

        if item is None:
            return None

        return item.text()