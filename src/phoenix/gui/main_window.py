from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QStackedWidget,
)

from PySide6.QtCore import QTimer

from phoenix.core.inspection_engine import InspectionEngine
from phoenix.health.health_engine import HealthEngine
from phoenix.models.health_report import HealthReport

from phoenix.gui.widgets.sidebar import Sidebar

from phoenix.gui.pages.dashboard import DashboardPage
from phoenix.gui.pages.doctor import DoctorPage
from phoenix.gui.pages.inventory import InventoryPage
from phoenix.gui.pages.debloat import DebloatPage
from phoenix.gui.pages.restore import RestorePage
from phoenix.gui.pages.history import HistoryPage
from phoenix.gui.pages.settings import SettingsPage

from phoenix.gui.controllers.inventory_controller import (
    InventoryController,
)

from phoenix.gui.controllers.debloat_controller import (
    DebloatController,
)

from phoenix.gui.dialogs.confirmation_dialog import (
    ConfirmationDialog,
)

from phoenix.gui.dialogs.progress_dialog import (
    ProgressDialog,
)

from phoenix.gui.result_dialog import (
    ResultDialog,
)


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Project Phoenix")
        self.resize(1200, 720)

        self.inspection = InspectionEngine()
        self.health_engine = HealthEngine()

        self.inventory_controller = InventoryController()
        self.debloat_controller = DebloatController()

        self.setup_ui()
        self.connect_navigation()



        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_device)
        self.timer.start(2000)

        self.refresh_device()

    def setup_ui(self):

        layout = QHBoxLayout()

        self.sidebar = Sidebar()

        self.stack = QStackedWidget()

        self.dashboard = DashboardPage()
        self.doctor = DoctorPage()
        self.inventory = InventoryPage()
        self.debloat = DebloatPage()
        self.restore = RestorePage()
        self.history = HistoryPage()
        self.settings = SettingsPage()

        self.stack.addWidget(self.dashboard)
        self.stack.addWidget(self.doctor)
        self.stack.addWidget(self.inventory)
        self.stack.addWidget(self.debloat)
        self.stack.addWidget(self.restore)
        self.stack.addWidget(self.history)
        self.stack.addWidget(self.settings)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack, 1)

        self.setLayout(layout)

    def connect_navigation(self):

        self.sidebar.dashboard_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.dashboard)
        )

        self.sidebar.doctor_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.doctor)
        )

        self.sidebar.inventory_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.inventory)
        )

        self.sidebar.debloat_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.debloat)
        )

        self.sidebar.restore_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.restore)
        )

        self.sidebar.history_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.history)
        )

        self.sidebar.settings_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.settings)
        )

        self.debloat.preview_button.clicked.connect(
            self.preview_debloat
        )

        self.debloat.execute_button.clicked.connect(
            self.execute_debloat
        )

    def refresh_device(self):

        try:

            report = self.inspection.inspect()

            health = self.health_engine.evaluate(report)

            self.doctor.update_report(health)

            apps = self.inventory_controller.load()

            self.inventory.update_inventory(apps)

            debloat_apps = self.debloat_controller.load()

            self.debloat.update_apps(debloat_apps)

            storage = report.storage[-1]

            total_ram = report.memory.total_kb
            free_ram = report.memory.available_kb

            used_ram = total_ram - free_ram

            ram_percent = int((used_ram / total_ram) * 100)

            device_text = (
                f"🟢 Connected\n\n"
                f"Model : {report.device.model}\n"
                f"Android : {report.device.android_version}"
            )

            self.dashboard.update_dashboard(

                device_text=device_text,

                battery=report.battery.level,

                ram_percent=ram_percent,

                storage_percent=storage.usage_percent,

                health_score=health.score,

                ram_text=f"{free_ram // 1024} MB Free",

                storage_text=f"{storage.available_kb // 1024} MB Free",

            )

            self.history.refresh()

        except Exception:

            self.inventory.update_inventory([])

            self.debloat.update_apps([])

            self.doctor.update_report(

                HealthReport(

                    score=0,

                    status="Disconnected",

                    recommendations=[],

                )

            )

            self.dashboard.update_dashboard(

                device_text="🔴 Disconnected",

                battery=0,

                ram_percent=0,

                storage_percent=0,

                health_score=0,

                ram_text="--",

                storage_text="--",

            )

    def preview_debloat(self):

        apps = self.debloat.selected_apps()

        commands = self.debloat_controller.preview(apps)

        self.debloat.show_preview(commands)

    def execute_debloat(self):

        apps = self.debloat.selected_apps()

        if not ConfirmationDialog.confirm(self, apps):
            return

        progress = ProgressDialog(self)
        progress.show()

        self.repaint()

        tx_id, results = self.debloat_controller.execute(apps)

        progress.finish()
        progress.close()

        if tx_id is None:
            return

        text = []

        text.append(f"Transaction : {tx_id}")
        text.append("")

        for item in results:

            status = "OK" if item.success else "FAILED"

            text.append(
                f"[{status}] {item.package}"
            )

        dialog = ResultDialog(
            "Debloat Result",
            "\n".join(text),
        )

        dialog.exec()

        self.history.refresh()