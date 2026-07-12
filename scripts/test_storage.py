from phoenix.services.storage_service import StorageService

service = StorageService()

items = service.read()

print("=" * 60)

print("STORAGE")

print("=" * 60)

for item in items:

    print(item)