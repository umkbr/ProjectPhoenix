from phoenix.database.package_database import PackageDatabase
from phoenix.models.installed_app import InstalledApp
from phoenix.services.package_service import PackageService


class InventoryEngine:

    def __init__(self):

        self.database = PackageDatabase()
        self.package_service = PackageService()

    def scan(self):

        packages = self.package_service.read()

        return self.build(packages)

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
                        category=info.get(
                            "category",
                            "unknown",
                        ),
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