from phoenix.core.adb_client import ADBClient


class SafetyGuard:

    def __init__(self):

        self.adb = ADBClient()

    def battery_level(self):

        output = self.adb.shell(
            "dumpsys battery"
        )

        for line in output.splitlines():

            line = line.strip()

            if line.startswith("level:"):

                return int(
                    line.replace(
                        "level:",
                        ""
                    ).strip()
                )

        return 0

    def battery_ok(self):

        return self.battery_level() >= 20

    def device_connected(self):

        return self.adb.connected()