from phoenix.capability.capability_engine import CapabilityEngine
from phoenix.models.device_info import DeviceInfo


def test_capability():

    device = DeviceInfo(
        serial="123",
        model="ASUS",
        manufacturer="asus",
        android_version="6.0",
        firmware="",
        fingerprint="",
        abi="armeabi-v7a",
    )

    engine = CapabilityEngine()

    apps = engine.recommend_apps(device)

    assert len(apps) >= 3