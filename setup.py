import os
from setuptools import setup
from nvpy import nvpy

setup(
    name = "myscript",
    version = "1.0",
    author = "Charl P. Botha",
    author_email = "cpbotha@vxlabs.com",
    description = "Demo of packaging a Python script as DEB",
    license = "BSD",
    url = "https://github.com/clouy4next",
    packages=['myscript'],
    entry_points = {
        'console_scripts' : ['myscript = myscript.myscript:main']
    },
    data_files = [
        ('share/applications/', ['vxlabs-myscript.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)