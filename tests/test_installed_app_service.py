from phoenix.services.installed_app_service import InstalledAppService


def test_installed_apps():

    service = InstalledAppService()

    apps = service.read()

    assert isinstance(apps, list)

    assert len(apps) > 0

    assert apps[0].package != ""