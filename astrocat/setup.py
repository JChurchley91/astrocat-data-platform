from setuptools import find_packages, setup

setup(
    name="astrocat",
    packages=find_packages(exclude=["astrocat_tests"]),
    install_requires=["dagster", "dagster-cloud"],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
