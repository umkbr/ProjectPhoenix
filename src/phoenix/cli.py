import argparse

from phoenix.core.inspection_engine import InspectionEngine
from phoenix.health.health_engine import HealthEngine
from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.report.report_engine import ReportEngine
from phoenix.recommendation.recommendation_engine import RecommendationEngine

def inspect():
    report = InspectionEngine().inspect()
    print(report)


def doctor():
    inspection = InspectionEngine().inspect()
    health = HealthEngine().evaluate(inspection)

    output = ReportEngine().render(
        model=inspection.device.model,
        score=health.score,
        recommendations=[
            r.title
            for r in health.recommendations
        ],
    )

    print(output)


def inventory():

    apps = InventoryEngine().scan()

    safe = [
        app
        for app in apps
        if app.safe_disable
    ]

    keep = [
        app
        for app in apps
        if not app.safe_disable
    ]

    print()
    print(f"Installed apps : {len(apps)}")

    print()
    print("SAFE TO DISABLE")
    print("-" * 40)

    for app in safe[:15]:
        print(f"✔ {app.name}")

    print()
    print("KEEP")
    print("-" * 40)

    for app in keep[:15]:
        print(f"✔ {app.name}")

def recommend():

    inspection = InspectionEngine().inspect()

    recommendations = (
        RecommendationEngine()
        .recommend(inspection.device)
    )

    print()
    print("PROJECT PHOENIX RECOMMENDATION")
    print("-" * 40)
    print()

    print(f"Compatible Apps ({len(recommendations)})")
    print()

    for app in recommendations:
        print(
            f"✔ {app.name} "
            f"(Score {app.score})"
        )

def main():

    parser = argparse.ArgumentParser(
        prog="phoenix",
        description="Project Phoenix Android Inspector"
    )

    parser.add_argument(
        "command",
        choices=[
            "inspect",
            "battery",
            "memory",
            "storage",
            "doctor",
            "inventory",
            "recommend"
        ]
    )

    args = parser.parse_args()

    if args.command == "inspect":
        inspect()

    elif args.command == "doctor":
        doctor()

    elif args.command == "inventory":
        inventory()

    elif args.command == "battery":
        print("Battery module coming soon")

    elif args.command == "memory":
        print("Memory module coming soon")

    elif args.command == "storage":
        print("Storage module coming soon")
   
    elif args.command == "recommend":
        recommend()


if __name__ == "__main__":
    main()