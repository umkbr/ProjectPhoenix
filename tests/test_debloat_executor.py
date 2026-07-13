from phoenix.executor.debloat_executor import DebloatExecutor


def test_disable():

    executor = DebloatExecutor()

    cmd = executor.disable(
        "com.asus.weathertime"
    )

    assert cmd == (
        "pm disable-user --user 0 "
        "com.asus.weathertime"
    )


def test_enable():

    executor = DebloatExecutor()

    cmd = executor.enable(
        "com.asus.weathertime"
    )

    assert cmd == (
        "pm enable "
        "com.asus.weathertime"
    )


def test_dry_run():

    executor = DebloatExecutor()

    cmd = executor.dry_run(
        "com.asus.weathertime"
    )

    assert "disable-user" in cmd