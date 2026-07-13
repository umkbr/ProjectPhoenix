from dataclasses import dataclass

from phoenix.models.health_report import HealthReport
from phoenix.models.recommendation import Recommendation


@dataclass
class DoctorReport:

    health: HealthReport

    diagnosis: list[str]

    recommendations: list[Recommendation]

    summary: str