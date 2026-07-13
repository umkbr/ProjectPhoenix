from dataclasses import dataclass


@dataclass
class AppInfo:
    name: str
    package: str
    version: str
    source: str