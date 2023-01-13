# #!/usr/bin/env python
#
# # This has only been added to allow editable dev installs, pyproject.toml replaces setup.py
# # e.g. pip install -e .
#
# import setuptools
#
# if __name__ == "__main__":
#     setuptools.setup()
import setuptools
import distutils.text_file
from pathlib import Path
from typing import List


def _parse_requirements(filename: str) -> List[str]:
    return distutils.text_file.TextFile(filename=str(Path(__file__).with_name(filename))).readlines()


required = _parse_requirements('requirements.txt')

setuptools.setup(
    name="fastapi_keycloak",
    version="1.0.9",
    author="1Verse",
    description="FastAPI Keycloak",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "fastapi_keycloak"},
    packages=setuptools.find_packages(where="fastapi_keycloak"),
    install_requires=required
    )

