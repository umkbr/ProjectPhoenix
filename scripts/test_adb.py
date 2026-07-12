from phoenix.core.adb_client import ADBClient

adb = ADBClient()

print("=" * 50)
print("PROJECT PHOENIX")
print("=" * 50)

print("ADB Available :", adb.is_available())
print("Devices       :", adb.devices())
print("Model         :", adb.getprop("ro.product.model"))
print("Firmware      :", adb.getprop("ro.build.display.id"))
print("Fingerprint   :", adb.getprop("ro.build.fingerprint"))