from phoenix.analyzer.package_analyzer import PackageAnalyzer

packages = []

with open("resources/packages.txt") as f:
    for line in f:
        packages.append(line.strip().replace("package:", ""))

analyzer = PackageAnalyzer()

recommendations = analyzer.analyze(packages)

for item in recommendations:
    print(item)