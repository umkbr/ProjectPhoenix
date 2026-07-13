from phoenix.debloat.debloat_engine import DebloatEngine
from phoenix.models.installed_app import InstalledApp


def test_safe_disable():

    engine = DebloatEngine()

    apps = [
        InstalledApp(
            package="com.asus.zencircle",
            name="ZenCircle",
            vendor="ASUS",
            category="Social",
            installed=True,
            safe_disable=True,
        )
    ]

    removable = engine.removable(apps)

    assert len(removable) == 1
    assert removable[0].package == "com.asus.zencircle"