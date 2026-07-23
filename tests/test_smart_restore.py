from phoenix.restore.smart_restore import SmartRestore


def test_restore_keyword():

    restore = SmartRestore()

    restore.backup.load = lambda: [

        "com.asus.weathertime",

        "com.asus.zencircle",

        "com.android.systemui",

    ]

    commands = restore.restore("weather")

    assert len(commands) == 1

    assert commands[0].startswith(
        "pm enable"
    )


def test_restore_all():

    restore = SmartRestore()

    restore.backup.load = lambda: [

        "com.asus.weathertime",

        "com.asus.zencircle",

    ]

    commands = restore.restore_all()

    assert len(commands) == 2