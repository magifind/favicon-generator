from setuptools import setup, find_packages

setup(
    name="favicon_generator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "cairosvg",
        "Pillow",
    ],
    entry_points={
        "console_scripts": [
            "favicon-generator=favicon_generator.main:main",
        ],
    },
)
