from phoenix.database.loader import DeviceKnowledgeLoader


def test_padfone_database():

    loader = DeviceKnowledgeLoader()

    data = loader.load("asus", "ASUS_T00N")

    assert data is not None
    assert data["marketing_name"] == "ASUS PadFone S"
    assert data["memory"]["ram_mb"] == 2048