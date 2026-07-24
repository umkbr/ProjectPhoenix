from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.executor.debloat_executor import DebloatExecutor


class DebloatEngine:

    def __init__(self):

        self.inventory = InventoryEngine()
        self.executor = DebloatExecutor()

    def removable(self, apps):

        return [
            app
            for app in apps
            if app.safe_disable
        ]

    def recommend(self, apps):

        return self.removable(apps)

    def analyze(self, packages):

        apps = self.inventory.build(packages)

        return self.removable(apps)

    def commands(self, apps):

        commands = []

        for app in self.removable(apps):

            commands.append(
                self.executor.disable(app.package)
            )

        return commands

    # ---------- NEW ----------

    def preview(self, apps):

        return self.commands(apps)

    def execute(self, apps):

        commands = self.commands(apps)

        return self.executor.execute(commands)