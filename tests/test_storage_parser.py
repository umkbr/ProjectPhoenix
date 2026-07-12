from phoenix.parsers.storage_parser import StorageParser


def test_parser():

    parser = StorageParser()

    text = """Filesystem Size Used Free Blksize
/data 10.0G 4.0G 6.0G 4096
"""

    result = parser.parse(text)

    assert len(result) == 1

    assert result[0].filesystem == "/data"

    assert result[0].used_kb > 0

    assert result[0].usage_percent == 40