from setuptools import setup

setup(
    name = "mdprint",
    version = "0.1.0",
    description = "Print markdown",
    author = "JeffTheK",
    url = "https://github.com/JeffTheK/mdprint",
    packages = ["mdprint"],
    entry_points = {
        'console_scripts': [
            'mdprint = mdprint.__main__:main'
        ]
    },
)