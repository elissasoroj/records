
#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="records",
    version="0.0.1",
    author="Elissa Sorojsrisom",
    author_email="ess2239@columbia.edu",
    license="GPLv3",
    description="Get records from GBIF",
    install_requires = ["requests", "pandas"],
    classifiers=["Programming Language :: Python :: 3"],
)
