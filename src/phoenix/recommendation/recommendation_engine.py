from phoenix.capability.capability_engine import CapabilityEngine


class RecommendationEngine:

    def __init__(self):
        self.engine = CapabilityEngine()

    def recommend(self, device):

        apps = self.engine.recommend_apps(device)

        apps.sort(
            key=lambda app: app.score,
            reverse=True,
        )

        return apps