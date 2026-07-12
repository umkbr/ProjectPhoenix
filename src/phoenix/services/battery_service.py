from phoenix.core.adb_client import ADBClient
from phoenix.models.battery_info import BatteryInfo


class BatteryService:

    def __init__(self):
        self.adb = ADBClient()

    def read(self):

        output = self.adb.shell("dumpsys battery")

        values = {}

        for line in output.splitlines():

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            values[key.strip()] = value.strip()

        return BatteryInfo(
            level=int(values.get("level", 0)),
            status=values.get("status", ""),
            health=values.get("health", ""),
            temperature=float(values.get("temperature", 0)) / 10,
            voltage=int(values.get("voltage", 0)),
        )