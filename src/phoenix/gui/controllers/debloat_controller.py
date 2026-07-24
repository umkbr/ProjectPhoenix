from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.debloat.debloat_engine import DebloatEngine
from phoenix.history.transaction_manager import TransactionManager


class DebloatController:

    def __init__(self):

        self.inventory = InventoryEngine()
        self.engine = DebloatEngine()
        self.history = TransactionManager()

    def load(self):

        apps = self.inventory.scan()

        return self.engine.removable(apps)

    def preview(self, apps):

        return self.engine.preview(apps)

    def execute(self, apps):

        if not apps:
            return None, []

        results = self.engine.execute(apps)

        transaction_id = self.history.save(results)

        return transaction_id, results