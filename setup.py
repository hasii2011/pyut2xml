import pathlib
from setuptools import setup

from pyut2xml import __version__ as pyut2xmlVersion

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
LICENSE = (HERE / 'LICENSE').read_text()

setup(
    name="pyut2xml",
    version=pyut2xmlVersion,
    author='Humberto A. Sanchez II',
    author_email='humberto.a.sanchez.ii@gmail.com',
    maintainer='Humberto A. Sanchez II',
    maintainer_email='humberto.a.sanchez.ii@gmail.com',
    description='Pyut decompressor and decompressor',
    long_description=README,
    long_description_content_type="text/markdown",
    license=LICENSE,
    url="https://github.com/hasii2011/pyut2xml",
    packages=[
        'pyut2xml'
    ],
    entry_points='''
        [console_scripts]
        pyut2xml=pyut2xml.pyut2xml:commandHandler
    ''',
    install_requires=['click==8.1.7'],
)
