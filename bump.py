import configparser

# Read the version from setup.cfg
config = configparser.ConfigParser()
config.read("setup.cfg")

# Parse the version string
major, minor, patch = map(int, config["metadata"]["version"].split("."))

# Increment the minor version
minor += 1

# Format the new version string
new_version = f"{major}.{minor}.{patch}"

# Update the version in setup.cfg
config["metadata"]["version"] = new_version
with open("setup.cfg", "w") as configfile:
    config.write(configfile)

print(f"Bumping to version {new_version} to trigger auto-deploy")
