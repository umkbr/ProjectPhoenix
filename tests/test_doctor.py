from phoenix.core.doctor import PhoenixDoctor


def test_python_version():

    doctor = PhoenixDoctor()

    assert doctor.check_python() is not None


def test_git():

    doctor = PhoenixDoctor()

    assert isinstance(doctor.check_git(), bool)


def test_adb():

    doctor = PhoenixDoctor()

    assert isinstance(doctor.check_adb(), bool)