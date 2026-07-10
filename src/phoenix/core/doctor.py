import platform
import shutil
import subprocess


class PhoenixDoctor:

    def check_python(self):
        return platform.python_version()

    def check_git(self):
        return shutil.which("git") is not None

    def check_adb(self):
        return shutil.which("adb") is not None

    def check_fastboot(self):
        return shutil.which("fastboot") is not None

    def check_device(self):
        if not self.check_adb():
            return None

        try:
            result = subprocess.run(
                ["adb", "devices"],
                capture_output=True,
                text=True,
                timeout=5
            )

            lines = result.stdout.splitlines()

            for line in lines:
                if "\tdevice" in line:
                    return line.split()[0]

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