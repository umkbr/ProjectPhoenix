from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QMessageBox,
)

from PySide6.QtCore import Qt


class DebloatPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

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

        self.preview_button = QPushButton(
            "Preview Commands"
        )

        layout.addWidget(self.preview_button)

        layout.addStretch()

        self.setLayout(layout)

        self.list.itemChanged.connect(
            self.update_counter
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

                apps.append(
                    item.data(Qt.UserRole)
                )

        return apps

    def update_counter(self):

        self.counter.setText(
            f"Selected : {len(self.selected_apps())}"
        )

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