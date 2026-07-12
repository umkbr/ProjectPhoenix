from dataclasses import dataclass

from phoenix.models.device_info import DeviceInfo
from phoenix.models.battery_info import BatteryInfo
from phoenix.models.memory_info import MemoryInfo
from phoenix.models.storage_info import StorageInfo


@dataclass
class InspectionReport:

    device: DeviceInfo

    battery: BatteryInfo

    memory: MemoryInfo

    storage: list[StorageInfo]

    recommendations: list