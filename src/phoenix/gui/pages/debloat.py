from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QMessageBox,
)

from PySide6.QtCore import Qt


class DebloatPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Debloat")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        self.counter = QLabel("Selected : 0")

        layout.addWidget(self.counter)

        self.list = QListWidget()

        layout.addWidget(self.list)

        button_layout = QHBoxLayout()

        self.select_all_button = QPushButton("Select All")
        self.clear_button = QPushButton("Clear")
        self.preview_button = QPushButton("Preview")
        self.execute_button = QPushButton("Execute")

        button_layout.addWidget(self.select_all_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addStretch()
        button_layout.addWidget(self.preview_button)
        button_layout.addWidget(self.execute_button)

        layout.addLayout(button_layout)

        layout.addStretch()

        self.list.itemChanged.connect(
            self.update_counter
        )

        self.select_all_button.clicked.connect(
            self.select_all
        )

        self.clear_button.clicked.connect(
            self.clear_selection
        )

    def update_apps(self, apps):

        self.list.clear()

        for app in apps:

            item = QListWidgetItem(
                f"{app.name} ({app.package})"
            )

            item.setFlags(
                item.flags() | Qt.ItemIsUserCheckable
            )

            item.setCheckState(Qt.Unchecked)

            item.setData(Qt.UserRole, app)

            self.list.addItem(item)

        self.update_counter()

    def selected_apps(self):

        apps = []

        for row in range(self.list.count()):

            item = self.list.item(row)

            if item.checkState() == Qt.Checked:

                apps.append(item.data(Qt.UserRole))

        return apps

    def update_counter(self):

        self.counter.setText(
            f"Selected : {len(self.selected_apps())}"
        )

    def select_all(self):

        for row in range(self.list.count()):

            self.list.item(row).setCheckState(
                Qt.Checked
            )

        self.update_counter()

    def clear_selection(self):

        for row in range(self.list.count()):

            self.list.item(row).setCheckState(
                Qt.Unchecked
            )

        self.update_counter()

    def show_preview(self, commands):

        if not commands:

            QMessageBox.information(
                self,
                "Preview",
                "No application selected.",
            )

            return

        QMessageBox.information(
            self,
            "Preview Commands",
            "\n".join(commands),
        )

    def show_result(self, tx_id, results):

        total = len(results)
        success = sum(
            1 for r in results if r.success
        )
        failed = total - success

        text = (
            f"Transaction : {tx_id}\n\n"
            f"Total      : {total}\n"
            f"Success    : {success}\n"
            f"Failed     : {failed}"
        )

        QMessageBox.information(
            self,
            "Execute Finished",
            text,
        )