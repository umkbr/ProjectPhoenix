from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
)

from PySide6.QtCore import Qt


class InventoryPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("Inventory")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        search_layout = QHBoxLayout()

        search_layout.addWidget(QLabel("Search"))

        self.search = QLineEdit()

        self.search.setPlaceholderText(
            "Search application..."
        )

        search_layout.addWidget(self.search)

        layout.addLayout(search_layout)

        self.total_label = QLabel("Total Apps : 0")

        layout.addWidget(self.total_label)

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Application",
            "Package",
            "Vendor",
            "Category",
            "Safe Disable",
        ])

        self.table.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(self.table)

        self.setLayout(layout)

    def update_inventory(self, apps):

        self.table.setRowCount(len(apps))

        self.total_label.setText(
            f"Total Apps : {len(apps)}"
        )

        for row, app in enumerate(apps):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(app.name),
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(app.package),
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(app.vendor),
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(app.category),
            )

            status = "Yes" if app.safe_disable else "No"

            item = QTableWidgetItem(status)

            item.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(
                row,
                4,
                item,
            )

        self.table.resizeColumnsToContents()