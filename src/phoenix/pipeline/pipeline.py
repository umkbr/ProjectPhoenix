from phoenix.core.inspection_engine import InspectionEngine
from phoenix.health.health_engine import HealthEngine
from phoenix.intelligence.intelligence_engine import IntelligenceEngine
from phoenix.recommendation.recommendation_engine import RecommendationEngine


class PhoenixPipeline:

    def __init__(self):

        self.inspection = InspectionEngine()

        self.health = HealthEngine()

        self.intelligence = IntelligenceEngine()

        self.recommendation = RecommendationEngine()

    def run(self):

        report = self.inspection.inspect()

        health = self.health.evaluate(report)

        intelligence = self.intelligence.classify(report)

        recommendations = self.recommendation.recommend(
            report.device
        )

        return {
            "report": report,
            "health": health,
            "intelligence": intelligence,
            "recommendations": recommendations,
        }