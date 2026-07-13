from phoenix.knowledge.app_catalog import AppCatalog
from phoenix.models.app_score import AppScore


class CapabilityEngine:

    def __init__(self):
        self.catalog = AppCatalog()

    def score_app(self, device, app):

        score = 100
        reasons = []

        android = float(".".join(device.android_version.split(".")[:2]))

        if android < app["min_android"]:
            score -= 40
            reasons.append("Android version too low")

        if android > app["max_android"]:
            score -= 40
            reasons.append("Android version too high")

        compatible = score >= 70

        return AppScore(
            name=app["name"],
            score=max(score, 0),
            compatible=compatible,
            reasons=reasons,
        )

    def recommend_apps(self, device):

        results = []

        for app in self.catalog.load():

            result = self.score_app(device, app)

            if result.compatible:
                results.append(result)

        return results