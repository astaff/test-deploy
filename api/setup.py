import os
from setuptools import setup, find_packages

DISTNAME = 'opentrons_server'
LICENSE = 'Apache 2.0'
AUTHOR = "Opentrons"
EMAIL = "engineering@opentrons.com"
DOWNLOAD_URL = ''
PACKAGES = find_packages(where='.', exclude=["tests.*", "tests"])

HERE = os.path.abspath(os.path.dirname(__file__))


if __name__ == "__main__":
    setup(
        name=DISTNAME,
        license=LICENSE,
        author=AUTHOR,
        author_email=EMAIL,
        maintainer=AUTHOR,
        maintainer_email=EMAIL,
        packages=PACKAGES,
        zip_safe=False,
        include_package_data=True
    )
