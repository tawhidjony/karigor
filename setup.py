from setuptools import setup, find_packages

setup(
    name="karigor",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer[all]>=0.9.0",
        "rich>=13.0.0",
        "questionary>=2.0.0",
        "inflect>=7.5.0",
    ],
    entry_points={
        "console_scripts": [
            "karigor=karigor.main:app",
        ],
    },
)