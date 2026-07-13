from phoenix.capability.capability_engine import CapabilityEngine


class CompatibilityEngine:

    def __init__(self):
        self.engine = CapabilityEngine()

    def best_apps(self, device):

        apps = self.engine.recommend_apps(device)

        apps.sort(
            key=lambda app: app.score,
            reverse=True,
        )

        return apps