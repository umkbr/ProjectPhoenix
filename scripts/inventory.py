from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.services.package_service import PackageService


packages = PackageService().list_packages()

apps = InventoryEngine().build(packages)

for app in apps:

    print(app)