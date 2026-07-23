from phoenix.core.inspection_engine import InspectionEngine


class DeviceDashboard:

    def load(self):

        report = InspectionEngine().inspect()

        return {
            "Model": report.device.model,
            "Manufacturer": report.device.manufacturer,
            "Android": report.device.android_version,
            "Battery": f"{report.battery.level}%",
            "RAM Free": f"{report.memory.available_kb // 1024} MB",
            "Storage": len(report.storage),
        }