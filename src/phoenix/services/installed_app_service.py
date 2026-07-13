from phoenix.services.package_service import PackageService
from phoenix.models.installed_app import InstalledApp


class InstalledAppService:

    def __init__(self):
        self.package = PackageService()

    def read(self):

        packages = self.package.read()

        apps = []

        for package in packages:

            apps.append(
                InstalledApp(
                    package=package,
                    name=package.split(".")[-1],
                    vendor=package.split(".")[1] if "." in package else "unknown",
                    category="unknown",
                    installed=True,
                    safe_disable=False,
                )
            )

        return apps