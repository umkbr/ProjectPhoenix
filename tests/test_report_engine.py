from phoenix.report.report_engine import ReportEngine


def test_report():

    engine = ReportEngine()

    report = engine.render(
        model="PadFone S",
        score=82,
        recommendations=[]
    )

    assert "PadFone" in report
    assert "82" in report