from phoenix.capability.capability_engine import CapabilityEngine
from phoenix.services.device_service import DeviceService

device = DeviceService().read()

engine = CapabilityEngine()

print("=" * 60)
print("RECOMMENDED APPS")
print("=" * 60)

for app in engine.recommend_apps(device):
    print(app["name"])