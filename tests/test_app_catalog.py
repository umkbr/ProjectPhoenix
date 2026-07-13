from phoenix.knowledge.app_catalog import AppCatalog


def test_catalog():

    catalog = AppCatalog()

    apps = catalog.load()

    assert len(apps) >= 3