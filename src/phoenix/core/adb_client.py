from __future__ import annotations

import shutil
import subprocess
from typing import List


class ADBClient:
    """Wrapper untuk Android Debug Bridge."""

    def __init__(self, executable: str = "adb") -> None:
        self.executable = executable

    def is_available(self) -> bool:
        return shutil.which(self.executable) is not None

    def run(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [self.executable, *args],
            capture_output=True,
            text=True,
            timeout=10,
        )

    def version(self) -> str:
        return self.run("version").stdout.strip()

    def devices(self) -> List[str]:
        result = self.run("devices")

        devices = []

        for line in result.stdout.splitlines():
            if "\tdevice" in line:
                devices.append(line.split()[0])

        return devices
        