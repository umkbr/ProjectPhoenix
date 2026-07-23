from phoenix.core.inspection_engine import InspectionEngine
from phoenix.health.health_engine import HealthEngine
from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.recommendation.recommendation_engine import RecommendationEngine
from phoenix.debloat.debloat_engine import DebloatEngine


def show_doctor(parent):

    report = InspectionEngine().inspect()

    health = HealthEngine().evaluate(report)

    lines = [
        f"Health Score : {health.score}",
        "",
    ]

    for item in health.recommendations:
        lines.append(f"• {item.title}")

    parent.output.show_text(
        "Doctor",
        lines,
    )


def show_inventory(parent):

    apps = InventoryEngine().scan()

    parent.output.show_text(
        "Inventory",
        [app.name for app in apps],
    )


def show_recommend(parent):

    report = InspectionEngine().inspect()

    apps = RecommendationEngine().recommend(
        report.device
    )

    parent.output.show_text(
        "Recommendations",
        [
            f"{app.name} ({app.score})"
            for app in apps
        ],
    )


def show_debloat(parent):

    apps = InventoryEngine().scan()

    safe = DebloatEngine().recommend(apps)

    parent.output.show_text(
        "Safe to Disable",
        [
            app.name
            for app in safe
        ],
    )


def show_history(parent):

    parent.output.show_text(
        "History",
        [
            "History feature coming soon."
        ],
    )