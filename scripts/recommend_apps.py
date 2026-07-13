from phoenix.services.device_service import DeviceService
from phoenix.recommendation.recommendation_engine import RecommendationEngine

device = DeviceService().read()

engine = RecommendationEngine()

apps = engine.recommend(device)

print("=" * 60)
print("RECOMMENDED APPS")
print("=" * 60)

for app in apps:
    print(f"{app.name}")
    print(f"Score : {app.score}")
    print(f"Compatible : {app.compatible}")

    if app.reasons:
        for reason in app.reasons:
            print(" -", reason)

    print()