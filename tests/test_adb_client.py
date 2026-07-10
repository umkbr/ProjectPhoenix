from phoenix.core.adb_client import ADBClient


def test_adb_object():

    adb = ADBClient()

    assert adb is not None


def test_is_available():

    adb = ADBClient()

    assert isinstance(adb.is_available(), bool)


def test_devices_returns_list():

    adb = ADBClient()

    assert isinstance(adb.devices(), list)
    