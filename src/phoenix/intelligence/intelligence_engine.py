from phoenix.intelligence.device_classifier import DeviceClass


class IntelligenceEngine:

    def classify(self, report):

        ram_mb = report.memory.total_kb / 1024

        if ram_mb < 1024:
            ram = "low"

        elif ram_mb < 3072:
            ram = "medium"

        else:
            ram = "high"

        android = float(
            ".".join(
                report.device.android_version.split(".")[:2]
            )
        )

        if android < 7:
            android_class = "legacy"

        elif android < 10:
            android_class = "modern"

        else:
            android_class = "current"

        return DeviceClass(
            performance="legacy",
            ram_class=ram,
            android_class=android_class,
            storage_class="normal",
        )