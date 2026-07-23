from phoenix.package.package_manager import PackageManager


def test_search():

    manager = PackageManager()

    manager.installed = lambda: [
        "com.asus.weathertime",
        "com.android.systemui",
    ]

    result = manager.search("weather")

    assert len(result) == 1

    assert result[0] == "com.asus.weathertime"