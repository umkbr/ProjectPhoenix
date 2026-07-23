from phoenix.core.adb_client import ADBClient


class PackageService:

    def __init__(self):

        self.adb = ADBClient()

    def read(self):

        output = self.adb.shell(
            "pm list packages"
        )

        packages = []

        for line in output.splitlines():

            if line.startswith("package:"):

                packages.append(
                    line.replace(
                        "package:",
                        ""
                    ).strip()
                )

        return packages

    def disabled(self):

        output = self.adb.shell(
            "pm list packages -d"
        )

        packages = []

        for line in output.splitlines():

            if line.startswith("package:"):

                packages.append(
                    line.replace(
                        "package:",
                        ""
                    ).strip()
                )

        return packages

    def version(self, package):

        output = self.adb.shell(
            f"dumpsys package {package}"
        )

        for line in output.splitlines():

            line = line.strip()

            if line.startswith("versionName="):

                return line.replace(
                    "versionName=",
                    ""
                )

        return "Unknown"

    # kompatibilitas
    def list_packages(self):

        return self.read()