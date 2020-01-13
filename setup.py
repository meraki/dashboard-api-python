"""Setup script for meraki"""

import os.path
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.md')) as fid:
    README = fid.read()

setup(
    name='meraki',
    version='0.70.5',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests'],
    keywords = ['meraki', 'dashboard', 'cisco'],
    description='Cisco Meraki Dashboard API library',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/meraki/dashboard-api-python',
    author='Cisco Meraki',
    author_email='api-feedback@meraki.net',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
