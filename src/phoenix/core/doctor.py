import platform
import shutil

from phoenix.core.adb_client import ADBClient


class PhoenixDoctor:

    def __init__(self, adb_client=None):
        self.adb = adb_client or ADBClient()

    def check_python(self):
        return platform.python_version()

    def check_git(self):
        return shutil.which("git") is not None

    def check_adb(self):
        return self.adb.is_available()

    def check_fastboot(self):
        return shutil.which("fastboot") is not None

    def check_device(self):
        if not self.check_adb():
            return None

        try:
            devices = self.adb.devices()

            if devices:
                return devices[0]

        except Exception:
            return None

        return None


def main():

    doctor = PhoenixDoctor()

    print("=" * 50)
    print("PROJECT PHOENIX DOCTOR")
    print("=" * 50)

    print(f"Python    : {doctor.check_python()}")
    print(f"Git       : {'OK' if doctor.check_git() else 'NOT FOUND'}")
    print(f"ADB       : {'OK' if doctor.check_adb() else 'NOT FOUND'}")
    print(f"Fastboot  : {'OK' if doctor.check_fastboot() else 'NOT FOUND'}")

    device = doctor.check_device()

    if device:
        print(f"Device    : {device}")
    else:
        print("Device    : NOT CONNECTED")


if __name__ == "__main__":
    main()
