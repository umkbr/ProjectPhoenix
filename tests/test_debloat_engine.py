from phoenix.debloat.debloat_engine import DebloatEngine


def test_debloat():

    engine = DebloatEngine()

    packages = [
        "com.asus.webstorage",
        "com.asus.zencircle",
        "com.android.systemui",
    ]

    result = engine.analyze(packages)

    assert isinstance(result, list)

    assert len(result) >= 2

    assert any(app.safe_disable for app in result)