from phoenix.analyzer.device_inspector import DeviceInspector

inspector = DeviceInspector()

report = inspector.inspect()

print("=" * 60)
print("PROJECT PHOENIX")
print("=" * 60)

print()

print(report.device)

print()

print(report.battery)

print()

print("Recommendations")

for item in report.recommendations:
    print("-", item.package, item.action)