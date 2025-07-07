### Used for setting up the package metadata and dependencies
from setuptools import setup, find_packages
setup(
    name='my_library',
    version='0.1.0',
    author='Aravind Raman',
    packages=find_packages(),
    install_requires=[],  # Add your dependencies here
    description='A simple Python library example',
#    long_description=open('README.md').read(),
#    long_description_content_type='text/markdown',  # Use markdown for long description
)