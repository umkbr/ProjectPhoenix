from phoenix.services.package_service import PackageService

service = PackageService()

packages = service.read()

print("=" * 50)
print("INSTALLED PACKAGES")
print("=" * 50)

for package in packages:
    print(package)