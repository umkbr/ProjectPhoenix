import argparse

from phoenix.core.inspection_engine import InspectionEngine
from phoenix.health.health_engine import HealthEngine
from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.report.report_engine import ReportEngine
from phoenix.recommendation.recommendation_engine import RecommendationEngine
from phoenix.debloat.debloat_engine import DebloatEngine
from phoenix.executor.adb_executor import ADBExecutor
from phoenix.history.history_manager import HistoryManager
from phoenix.status.status_manager import StatusManager

def inspect():

    report = InspectionEngine().inspect()

    print(report)


def doctor():

    inspection = InspectionEngine().inspect()

    health = HealthEngine().evaluate(
        inspection
    )

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


def debloat(apply=False):

    apps = InventoryEngine().scan()

    engine = DebloatEngine()

    safe_apps = engine.recommend(apps)

    commands = engine.commands(apps)

    print()
    print("=" * 40)
    print("PROJECT PHOENIX")
    print("=" * 40)

    print()

    if not apply:

        print("PREVIEW MODE")
        print()

        print(
            f"{len(commands)} commands will be executed."
        )

        print()

        for command in commands:

            print(command)

        print()
        print(
            "Run again with --apply to execute."
        )

        return

    print("EXECUTING...")
    print()

    executor = ADBExecutor()

    executor.run_many(commands)

    for app in safe_apps:

        print(f"✔ {app.name}")

    print()
    print("Done.")

def history():

    manager = HistoryManager()

    items = manager.list()

    print()
    print("=" * 40)
    print("TRANSACTION HISTORY")
    print("=" * 40)

    print()

    for item in items:

        print(item["id"])
        print(
            f"Packages : {item['packages']}"
        )
        print(
            f"Success  : {item['success']}"
        )
        print("-" * 40)

def status():

    manager = StatusManager()

    items = manager.status()

    print()
    print("=" * 40)
    print("PACKAGE STATUS")
    print("=" * 40)
    print()

    for item in items[:25]:

        icon = "✖" if item["disabled"] else "✔"

        state = (
            "Disabled"
            if item["disabled"]
            else "Enabled"
        )

        print(
            f"{icon} "
            f"{item['name']:<25} "
            f"{state}"
        )

def update_device(self, report):

    if report is None:

        text = (
            "Status : Disconnected\n"
            "\n"
            "No device detected."
        )

    else:

        text = (
            f"Status : Connected\n\n"
            f"Model : {report.device.model}\n"
            f"Android : {report.device.android_version}\n"
            f"Serial : {report.device.serial}"
        )

    self.after(
        0,
        lambda: self.device_label.config(
            text=text
        )
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
            "recommend",
            "debloat",
            "history",
            "status",
        ]
    )

    parser.add_argument(

        "--apply",

        action="store_true",

        help="Execute generated commands"

    )

    args = parser.parse_args()

    if args.command == "inspect":

        inspect()

    elif args.command == "doctor":

        doctor()

    elif args.command == "inventory":

        inventory()

    elif args.command == "recommend":

        recommend()

    elif args.command == "debloat":

        debloat(
            apply=args.apply
        )

    elif args.command == "battery":

        print("Battery module coming soon")

    elif args.command == "memory":

        print("Memory module coming soon")

    elif args.command == "storage":

        print("Storage module coming soon")

    elif args.command == "history":
        history()
    
    elif args.command == "status":
        status()

if __name__ == "__main__":

    main()