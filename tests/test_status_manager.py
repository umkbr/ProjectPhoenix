from phoenix.status.status_manager import StatusManager


def test_status():

    manager = StatusManager()

    manager.package.disabled = lambda: [
        "com.asus.weathertime"
    ]

    class App:

        def __init__(self, name, package):

            self.name = name
            self.package = package

    manager.inventory.scan = lambda: [

        App(
            "Weather",
            "com.asus.weathertime",
        ),

        App(
            "SystemUI",
            "com.android.systemui",
        ),
    ]

    result = manager.status()

    assert result[0]["disabled"] is True

    assert result[1]["disabled"] is False