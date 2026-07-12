from phoenix.services.device_service import DeviceService
from phoenix.services.battery_service import BatteryService
from phoenix.analyzer.package_analyzer import PackageAnalyzer
from phoenix.models.inspection_report import InspectionReport


class DeviceInspector:

    def __init__(self):

        self.device_service = DeviceService()
        self.battery_service = BatteryService()
        self.package_analyzer = PackageAnalyzer()

    def inspect(self):

        device = self.device_service.read()

        battery = self.battery_service.read()

        with open("resources/packages.txt") as f:

            packages = [
                line.strip().replace("package:", "")
                for line in f
            ]

        recommendations = self.package_analyzer.analyze(packages)

        return InspectionReport(
            device=device,
            battery=battery,
            recommendations=recommendations,
        )