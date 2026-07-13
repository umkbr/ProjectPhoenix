from phoenix.recommendation.recommendation_engine import RecommendationEngine
from phoenix.models.device_info import DeviceInfo


def test_recommend():

    device = DeviceInfo(
        serial="1",
        model="PadFone",
        manufacturer="ASUS",
        android_version="6.0",
        firmware="",
        fingerprint="",
        abi="armeabi-v7a",
    )

    engine = RecommendationEngine()

    result = engine.recommend(device)

    assert len(result) > 0