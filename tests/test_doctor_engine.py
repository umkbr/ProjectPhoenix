from phoenix.doctor.doctor_engine import DoctorEngine
from phoenix.models.health_report import HealthReport


def test_doctor():

    report = HealthReport(
        score=80,
        status="Good",
        recommendations=[],
    )

    result = DoctorEngine().diagnose(report)

    assert result.summary != ""
    assert result.health.score == 80