from phoenix.analyzer.package_analyzer import PackageAnalyzer


def test_webstorage():

    analyzer = PackageAnalyzer()

    result = analyzer.analyze(
        ["com.asus.webstorage"]
    )

    assert len(result) == 1
    assert result[0].action == "disable"