from phoenix.services.memory_service import MemoryService

print("=" * 60)
print("MEMORY")
print("=" * 60)

service = MemoryService()

print(service.read())