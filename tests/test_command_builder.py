from phoenix.executor.command_builder import CommandBuilder


def test_disable_command():

    builder = CommandBuilder()

    cmd = builder.disable(
        "com.asus.webstorage"
    )

    assert (
        cmd
        ==
        "adb shell pm disable-user com.asus.webstorage"
    )


def test_uninstall_command():

    builder = CommandBuilder()

    cmd = builder.uninstall(
        "com.asus.webstorage"
    )

    assert (
        cmd
        ==
        "adb shell pm uninstall --user 0 com.asus.webstorage"
    )