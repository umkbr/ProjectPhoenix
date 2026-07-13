from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.debloat.debloat_engine import DebloatEngine


def test_recommend():

    apps = [
        type(
            "App",
            (),
            {
                "name": "Weather",
                "package": "com.asus.weathertime",
                "safe_disable": True,
            },
        ),
        type(
            "App",
            (),
            {
                "name": "SystemUI",
                "package": "com.android.systemui",
                "safe_disable": False,
            },
        ),
    ]

    engine = DebloatEngine()

    result = engine.recommend(apps)

    assert len(result) == 1

    assert result[0].package == "com.asus.weathertime"