from phoenix.models.inspection_report import InspectionReport

from phoenix.services.device_service import DeviceService
from phoenix.services.battery_service import BatteryService
from phoenix.services.memory_service import MemoryService
from phoenix.services.storage_service import StorageService


class InspectionEngine:

    def __init__(self):

        self.device = DeviceService()

        self.battery = BatteryService()

        self.memory = MemoryService()

        self.storage = StorageService()

    def inspect(self):

        return InspectionReport(
            device=self.device.read(),
            battery=self.battery.read(),
            memory=self.memory.read(),
            storage=self.storage.read(),
            recommendations=[],
        )