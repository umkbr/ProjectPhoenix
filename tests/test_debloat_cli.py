from phoenix.debloat.debloat_engine import DebloatEngine
from phoenix.models.installed_app import InstalledApp


def test_commands():

    apps = [
        InstalledApp(
            package="com.asus.weathertime",
            name="Weather",
            vendor="ASUS",
            category="Tools",
            installed=True,
            safe_disable=True,
        ),
        InstalledApp(
            package="com.android.systemui",
            name="SystemUI",
            vendor="Google",
            category="System",
            installed=True,
            safe_disable=False,
        ),
    ]

    engine = DebloatEngine()

    commands = engine.commands(apps)

    assert len(commands) == 1

    assert commands[0] == (
        "pm disable-user --user 0 "
        "com.asus.weathertime"
    )