from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.debloat.debloat_engine import DebloatEngine


class DebloatController:

    def __init__(self):

        self.inventory = InventoryEngine()
        self.engine = DebloatEngine()

    def load(self):

        apps = self.inventory.scan()

        return self.engine.removable(apps)

    def preview(self, apps):

        return self.engine.commands(apps)