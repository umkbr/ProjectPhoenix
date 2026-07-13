from phoenix.inventory.inventory_engine import InventoryEngine


def test_inventory():

    engine = InventoryEngine()

    apps = engine.build(
        [
            "com.asus.weathertime",
            "com.unknown.app",
        ]
    )

    assert len(apps) == 2

    assert apps[0].safe_disable is True

    assert apps[1].safe_disable is False