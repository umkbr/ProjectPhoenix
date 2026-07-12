from phoenix.services.device_service import DeviceService

device = DeviceService().read()

print("=" * 50)
print("PROJECT PHOENIX DEVICE REPORT")
print("=" * 50)

print(device)