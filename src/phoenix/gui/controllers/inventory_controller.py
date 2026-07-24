from phoenix.inventory.inventory_engine import InventoryEngine


class InventoryController:

    def __init__(self):

        self.engine = InventoryEngine()

    def load(self):

        return self.engine.scan()