from dataclasses import dataclass


@dataclass
class InstalledApp:
    package: str
    name: str
    vendor: str
    category: str
    installed: bool
    safe_disable: bool