from phoenix.services.package_service import PackageService
from phoenix.inventory.inventory_engine import InventoryEngine


class StatusManager:

    def __init__(self):

        self.package = PackageService()
        self.inventory = InventoryEngine()

    def status(self):

        disabled = set(
            self.package.disabled()
        )

        apps = self.inventory.scan()

        result = []

        for app in apps:

            result.append(
                {
                    "name": app.name,
                    "package": app.package,
                    "disabled": app.package in disabled,
                }
            )

        return result