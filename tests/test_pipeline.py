from phoenix.pipeline.pipeline import PhoenixPipeline


def test_pipeline():

    pipeline = PhoenixPipeline()

    result = pipeline.run()

    assert result["report"] is not None

    assert result["health"] is not None

    assert result["intelligence"] is not None

    assert result["recommendations"] is not None