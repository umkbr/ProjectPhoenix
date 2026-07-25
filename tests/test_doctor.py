from phoenix.core.doctor import PhoenixDoctor


class FakeADB:

    def is_available(self):
        return True

    def devices(self):
        return ["device-123"]


def test_python_version():

    doctor = PhoenixDoctor()

    assert doctor.check_python() is not None


def test_git():

    doctor = PhoenixDoctor()

    assert isinstance(doctor.check_git(), bool)


def test_adb():

    doctor = PhoenixDoctor()

    assert isinstance(doctor.check_adb(), bool)


def test_device_uses_adb_client():

    doctor = PhoenixDoctor(adb_client=FakeADB())

    assert doctor.check_device() == "device-123"
