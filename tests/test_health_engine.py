from phoenix.health.health_engine import HealthEngine
from phoenix.models.inspection_report import InspectionReport
from phoenix.models.device_info import DeviceInfo
from phoenix.models.battery_info import BatteryInfo
from phoenix.models.memory_info import MemoryInfo
from phoenix.models.storage_info import StorageInfo


def test_health():

    report = InspectionReport(
        device=DeviceInfo(
            serial="1",
            model="PadFone",
            manufacturer="ASUS",
            android_version="6.0",
            firmware="",
            fingerprint="",
            abi="armeabi-v7a",
        ),
        battery=BatteryInfo(
            level=100,
            status="2",
            health="2",
            temperature=25,
            voltage=4200,
        ),
        memory=MemoryInfo(
            total_kb=2048000,
            free_kb=100000,
            available_kb=100000,
            buffers_kb=0,
            cached_kb=0,
        ),
        storage=[
            StorageInfo(
                filesystem="/data",
                total_kb=100,
                used_kb=90,
                available_kb=10,
                usage_percent=90,
            )
        ],
        recommendations=[],
    )

    result = HealthEngine().evaluate(report)

    assert result.score < 100