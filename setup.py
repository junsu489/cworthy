"""setup"""

from setuptools import find_packages, setup  # type: ignore [import-untyped]

setup(
    name="cworthy",
    version="0.1.0",
    packages=find_packages(include=["cworthy", "cworthy.*"]),
)
