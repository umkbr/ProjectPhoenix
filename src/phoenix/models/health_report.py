from dataclasses import dataclass

from phoenix.models.recommendation import Recommendation


@dataclass
class HealthReport:

    score: int

    status: str

    recommendations: list[Recommendation]