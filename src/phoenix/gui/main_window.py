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

from phoenix.history.history_manager import (
    HistoryManager,
)

from phoenix.restore.restore_manager import (
    RestoreManager,
)

from phoenix.gui.controllers.quick_optimize_controller import (
    QuickOptimizeController,
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

        self.doctor.refresh_button.clicked.connect(
            self.refresh_device
        )

        self.doctor.optimize_button.clicked.connect(
            self.quick_optimize
        )

        self.dashboard.refresh_button.clicked.connect(
            self.refresh_device
        )

        self.dashboard.quick_optimize_button.clicked.connect(
            self.quick_optimize
        )

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_device)
        self.timer.start(2000)

        self.refresh_device()

        self.restore.restore_button.clicked.connect(
            self.restore_transaction
        )

        self.quick_controller = QuickOptimizeController()

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

        self.restore.restore_button.clicked.connect(
            self.restore_transaction
        )

    def refresh_device(self):

        try:

            report = self.inspection.inspect()

            health = self.health_engine.evaluate(report)

            self.doctor.update_report(health)

            self.doctor.update_device_info(
                report
            )

            self.doctor.optimize_button.setEnabled(
                True
            )

            apps = self.inventory_controller.load()

            self.inventory.update_inventory(apps)

            debloat_apps = self.debloat_controller.load()

            recommended = 0

            for app in debloat_apps:

                if getattr(
                    app,
                    "recommended",
                    False,
                ):

                    recommended += 1

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

            from datetime import datetime

            self.dashboard.update_statistics(

                installed=len(
                    debloat_apps
                ),

                recommended=recommended,

                last_action=datetime.now().strftime(
                    "%H:%M:%S"
                ),

            )

                device_text=device_text,

                battery=report.battery.level,

                ram_percent=ram_percent,

                storage_percent=storage.usage_percent,

                health_score=health.score,

                ram_text=f"{free_ram // 1024} MB Free",

                storage_text=f"{storage.available_kb // 1024} MB Free",

            )

            self.history.refresh()

            transactions = self.history_manager.list()

            self.restore.update_transactions(
                transactions
            )

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

            self.dashboard.update_statistics(

                installed=0,

                recommended=0,

                last_action="-",

            )

            self.dashboard.set_connected(False)

            self.doctor.optimize_button.setEnabled(
                False
            )
            self.doctor.model_label.setText("--")
            self.doctor.android_label.setText("--")
            self.doctor.battery_label.setText("--")
            self.doctor.memory_label.setText("--")
            self.doctor.storage_label.setText("--")
    def preview_debloat(self):

        apps = self.debloat.selected_apps()

        commands = self.debloat_controller.preview(apps)

        self.debloat.show_preview(commands)

    def _execute_apps(self, apps, title):

        if not apps:
            return

        if not ConfirmationDialog.confirm(
            self,
            apps,
        ):
            return

        progress = ProgressDialog(self)

        progress.show()

        self.repaint()

        tx_id, results = self.debloat_controller.execute(
            apps
        )

        progress.finish()
        progress.close()

        if tx_id is None:
            return

        ok = 0
        failed = 0

        lines = [

            f"Transaction : {tx_id}",

            "",

        ]

        for item in results:

            if item.success:
                ok += 1
            else:
                failed += 1

            status = (
                "OK"
                if item.success
                else "FAILED"
            )

            lines.append(
                f"[{status}] {item.package}"
            )

        lines.append("")
        lines.append(f"Success : {ok}")
        lines.append(f"Failed : {failed}")

        ResultDialog(

            title,

            "\n".join(lines),

        ).exec()

        self.history.refresh()

        self.refresh_device()


    def execute_debloat(self):

        apps = self.debloat.selected_apps()

        self._execute_apps(

            apps,

            "Debloat Result",

        )

    def restore_transaction(self):

        tx = self.restore.selected_transaction()

        if tx is None:
            return

        backup = self.history_manager.load(tx)

        if backup is None:
            return

        if not ConfirmationDialog.confirm(
            self,
            backup.results,
        ):
            return

        progress = ProgressDialog(self)

        progress.show()

        self.repaint()

        manager = RestoreManager(backup)

        result = manager.execute()

        progress.finish()

        progress.close()

        dialog = ResultDialog(

            "Restore Result",

            "\n".join(result),

        )

        dialog.exec()

        self.refresh_device()

    def quick_optimize(self):

        apps = self.debloat_controller.load()

        recommended = [

            app

            for app in apps

            if getattr(

                app,

                "recommended",

                False,

            )

        ]

        if not recommended:

            ResultDialog(

                "Quick Optimize",

                "No recommended applications found.",

            ).exec()

            return

        self._execute_apps(

            recommended,

            "Quick Optimize",

        )