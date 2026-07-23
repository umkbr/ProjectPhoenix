from phoenix.services.package_service import PackageService


class PackageManager:

    def __init__(self):

        self.service = PackageService()

    def installed(self):

        return self.service.read()

    def disabled(self):

        return self.service.disabled()

    def search(self, keyword):

        return [
            package
            for package in self.installed()
            if keyword.lower() in package.lower()
        ]