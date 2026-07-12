from phoenix.services.battery_service import BatteryService

battery = BatteryService().read()

print("=" * 50)
print("BATTERY REPORT")
print("=" * 50)

print(battery)