from dataclasses import dataclass


@dataclass(slots=True)
class DeviceInfo:
    serial: str
    model: str
    manufacturer: str
    android_version: str
    firmware: str
    fingerprint: str
    abi: str