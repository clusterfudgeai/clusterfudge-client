#!/usr/bin/env python3

import configparser
import shutil
import subprocess

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

print(f"Deploying version {new_version}")

# Delete current contents of dist directory
shutil.rmtree("./dist", ignore_errors=True)

# Build the package
subprocess.run(["python3", "-m", "build"], check=True)

# Upload to PyPI using twine
subprocess.run(["twine", "upload", "dist/*"], check=True)
