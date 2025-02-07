#!/usr/bin/env python3
import sys
import toml
from pathlib import Path

def bump_version(version_type='minor'):
    """
    Bump the version in pyproject.toml
    version_type can be 'major', 'minor', or 'patch'
    """
    try:
        pyproject_path = Path("pyproject.toml")
        if not pyproject_path.exists():
            print("Error: pyproject.toml not found")
            sys.exit(1)

        # Read the current version
        config = toml.load(pyproject_path)
        current_version = config["project"]["version"]
        major, minor, patch = map(int, current_version.split("."))

        # Update the appropriate version number
        if version_type == 'major':
            major += 1
            minor = 0
            patch = 0
        elif version_type == 'minor':
            minor += 1
            patch = 0
        elif version_type == 'patch':
            patch += 1
        else:
            print(f"Error: Invalid version type '{version_type}'")
            sys.exit(1)

        # Format the new version string
        new_version = f"{major}.{minor}.{patch}"
        
        # Update the version in pyproject.toml
        config["project"]["version"] = new_version
        
        # Write back to pyproject.toml while preserving formatting
        with open(pyproject_path, "w") as configfile:
            toml.dump(config, configfile)
        
        print(f"Version bumped from {current_version} to {new_version}")
        return new_version

    except Exception as e:
        print(f"Error updating version: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    version_type = sys.argv[1] if len(sys.argv) > 1 else 'minor'
    bump_version(version_type)
