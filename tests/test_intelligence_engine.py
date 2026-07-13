from phoenix.intelligence.intelligence_engine import IntelligenceEngine
from phoenix.models.device_info import DeviceInfo
from phoenix.models.memory_info import MemoryInfo
from phoenix.models.inspection_report import InspectionReport


def test_classifier():

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
        battery=None,
        memory=MemoryInfo(
            total_kb=2048000,
            free_kb=0,
            available_kb=0,
            buffers_kb=0,
            cached_kb=0,
        ),
        storage=[],
        recommendations=[],
    )

    result = IntelligenceEngine().classify(report)

    assert result.android_class == "legacy"