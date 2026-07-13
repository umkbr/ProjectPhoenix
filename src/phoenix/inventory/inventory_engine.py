from phoenix.database.package_database import PackageDatabase
from phoenix.models.installed_app import InstalledApp


class InventoryEngine:

    def __init__(self):

        self.database = PackageDatabase()

    def build(self, packages):

        apps = []

        for package in packages:

            info = self.database.find(package)

            if info:

                apps.append(
                    InstalledApp(
                        package=package,
                        name=info["name"],
                        vendor="ASUS",
                        category=info.get("category", "unknown"),
                        installed=True,
                        safe_disable=info["safe_disable"],
                    )
                )

            else:

                apps.append(
                    InstalledApp(
                        package=package,
                        name=package,
                        vendor="Unknown",
                        category="Unknown",
                        installed=True,
                        safe_disable=False,
                    )
                )

        return apps