from phoenix.core.inspection_engine import InspectionEngine

engine = InspectionEngine()

report = engine.inspect()

print("=" * 60)
print("PROJECT PHOENIX")
print("=" * 60)

print(report)