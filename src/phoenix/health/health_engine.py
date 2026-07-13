from phoenix.models.recommendation import Recommendation
from phoenix.models.health_report import HealthReport


class HealthEngine:

    def evaluate(self, report):

        recommendations = []

        # ----------------------------
        # Storage
        # ----------------------------

        for storage in report.storage:

            if (
                storage.filesystem == "/data"
                and storage.usage_percent >= 90
            ):

                recommendations.append(
                    Recommendation(
                        title="Storage Almost Full",
                        description="Internal storage usage is above 90%",
                        severity="high",
                        action="cleanup",
                    )
                )

        # ----------------------------
        # Memory
        # ----------------------------

        memory_percent = (
            report.memory.free_kb
            / report.memory.total_kb
        ) * 100

        if memory_percent < 10:

            recommendations.append(
                Recommendation(
                    title="Low Available RAM",
                    description="Less than 10% RAM is free",
                    severity="medium",
                    action="cleanup",
                )
            )

        # ----------------------------
        # Battery
        # ----------------------------

        if report.battery.temperature > 45:

            recommendations.append(
                Recommendation(
                    title="Battery Temperature High",
                    description="Battery temperature is above 45°C",
                    severity="high",
                    action="cooldown",
                )
            )

        # ----------------------------
        # Overall Health Score
        # ----------------------------

        score = 100

        score -= len(recommendations) * 10

        if score < 0:
            score = 0

        if score >= 90:
            status = "Excellent"
        elif score >= 75:
            status = "Good"
        elif score >= 50:
            status = "Warning"
        else:
            status = "Critical"

        return HealthReport(
            score=score,
            status=status,
            recommendations=recommendations,
        )