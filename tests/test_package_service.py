from phoenix.services.package_service import PackageService


def test_version():

    service = PackageService()

    version = service.version(
        "com.android.systemui"
    )

    assert isinstance(version, str)