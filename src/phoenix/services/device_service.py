from phoenix.core.adb_client import ADBClient
from phoenix.core.exceptions import DeviceNotFoundError
from phoenix.models.device_info import DeviceInfo


class DeviceService:

    def __init__(self):
        self.adb = ADBClient()

    def read(self):

        devices = self.adb.devices()

        if not devices:
            raise DeviceNotFoundError("No Android device connected.")

        serial = devices[0]

        return DeviceInfo(
            serial=serial,
            model=self.adb.getprop("ro.product.model"),
            manufacturer=self.adb.getprop("ro.product.manufacturer"),
            android_version=self.adb.getprop("ro.build.version.release"),
            firmware=self.adb.getprop("ro.build.display.id"),
            fingerprint=self.adb.getprop("ro.build.fingerprint"),
            abi=self.adb.getprop("ro.product.cpu.abi"),
        )