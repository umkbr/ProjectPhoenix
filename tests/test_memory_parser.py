from phoenix.parsers.memory_parser import MemoryParser


def test_parser():
    parser = MemoryParser()

    text = """MemTotal: 2048000 kB
MemFree: 512000 kB
MemAvailable: 1024000 kB
Buffers: 64000 kB
Cached: 256000 kB
"""

    result = parser.parse(text)

    assert result.total_kb == 2048000
    assert result.free_kb == 512000
    assert result.available_kb == 1024000
    assert result.cached_kb == 256000