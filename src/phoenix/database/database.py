from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

DATABASE = ROOT / "database"

HARDWARE = DATABASE / "hardware"

PACKAGES = DATABASE / "packages"

FIRMWARE = DATABASE / "firmware"

PARTITIONS = DATABASE / "partitions"