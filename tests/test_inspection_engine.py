from phoenix.core.inspection_engine import InspectionEngine


def test_engine():

    engine = InspectionEngine()

    report = engine.inspect()

    assert report.device is not None

    assert report.battery is not None

    assert report.memory is not None

    assert report.storage is not None