from phoenix.knowledge.app_catalog import AppCatalog

catalog = AppCatalog()

print("=" * 60)
print("APPLICATION CATALOG")
print("=" * 60)

for app in catalog.load():
    print(app["name"])