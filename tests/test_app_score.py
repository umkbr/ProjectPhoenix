from phoenix.capability.capability_engine import CapabilityEngine
from phoenix.models.device_info import DeviceInfo


def test_score():

    device = DeviceInfo(
        serial="1",
        model="PadFone",
        manufacturer="ASUS",
        android_version="6.0",
        firmware="",
        fingerprint="",
        abi="armeabi-v7a",
    )

    app = {
        "name": "Firefox ESR",
        "min_android": 5,
        "max_android": 8,
    }

    engine = CapabilityEngine()

    result = engine.score_app(device, app)

    assert result.compatible
    assert result.score == 100