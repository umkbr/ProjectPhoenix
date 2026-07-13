from phoenix.compatibility.compatibility_engine import CompatibilityEngine
from phoenix.models.device_info import DeviceInfo


def test_best_apps():

    device = DeviceInfo(
        serial="1",
        model="PadFone",
        manufacturer="ASUS",
        android_version="6.0",
        firmware="",
        fingerprint="",
        abi="armeabi-v7a",
    )

    apps = CompatibilityEngine().best_apps(device)

    assert len(apps) > 0