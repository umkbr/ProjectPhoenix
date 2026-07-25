from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.debloat.debloat_engine import DebloatEngine
from phoenix.history.transaction_manager import TransactionManager
from phoenix.utils.logger import logger

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

        try:

            result = self.engine.execute(apps)

        except Exception as e:

            logger.exception(e)

            raise

        transaction_id = self.history.save(results)

        return transaction_id, results