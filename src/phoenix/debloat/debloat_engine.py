from phoenix.inventory.inventory_engine import InventoryEngine


class DebloatEngine:

    def __init__(self):
        self.inventory = InventoryEngine()

    def removable(self, apps):

        return [
            app
            for app in apps
            if app.safe_disable
        ]

    def analyze(self, packages):

        apps = self.inventory.build(packages)

        return self.removable(apps)