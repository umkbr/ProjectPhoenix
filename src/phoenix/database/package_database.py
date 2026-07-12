from phoenix.database.database import PACKAGES
from phoenix.database.json_loader import load

class PackageDatabase:

    def __init__(self):
        self.apps = load(PACKAGES / "asus_system_apps.json")

    def find(self, package_name):
        for app in self.apps:
            if app["package"] == package_name:
                return app
        return None