from dataclasses import dataclass


@dataclass(slots=True)
class BatteryInfo:
    level: int
    status: str
    health: str
    temperature: float
    voltage: int