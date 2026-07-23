from phoenix.gui.text_dialog import TextDialog

from phoenix.core.inspection_engine import InspectionEngine
from phoenix.health.health_engine import HealthEngine
from phoenix.inventory.inventory_engine import InventoryEngine
from phoenix.recommendation.recommendation_engine import RecommendationEngine
from phoenix.debloat.debloat_engine import DebloatEngine
from phoenix.gui.device_dialog import DeviceDialog

def show_doctor(parent):

    report = InspectionEngine().inspect()

    health = HealthEngine().evaluate(report)

    text = (
        "PROJECT PHOENIX\n\n"
        f"Health Score : {health.score}\n\n"
    )

    for r in health.recommendations:
        text += f"• {r.title}\n"

    TextDialog(
        "Doctor",
        text,
    ).exec()


def show_inventory(parent):

    apps = InventoryEngine().scan()

    text = (
        "PROJECT PHOENIX\n"
        "========================\n\n"
        f"Installed Apps : {len(apps)}\n\n"
    )

    for app in apps:
        text += f"✓ {app.name}\n"

    TextDialog(
        "Inventory",
        text,
    ).exec()


def show_recommend(parent):

    report = InspectionEngine().inspect()

    apps = RecommendationEngine().recommend(
        report.device
    )

    text = "Compatible Apps\n\n"

    for app in apps:
        text += (
            f"✓ {app.name}"
            f" (Score {app.score})\n"
        )

    TextDialog(
        "Recommendation",
        text,
    ).exec()


def show_debloat(parent):

    apps = InventoryEngine().scan()

    safe = DebloatEngine().recommend(apps)

    text = "Safe To Disable\n\n"

    for app in safe:
        text += f"✓ {app.name}\n"

    TextDialog(
        "Debloat",
        text,
    ).exec()


def show_history(parent):

    TextDialog(
        "History",
        "Coming Soon",
    ).exec()

def show_device(parent):

    dialog = DeviceDialog()

    dialog.exec()