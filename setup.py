from setuptools import setup, find_packages
import os

LICENSE_FILE = 'LICENSE'
README_FILE = 'README.md'
README_TYPE = 'text/markdown'

if os.path.exists(README_FILE):
    with open(README_FILE, 'r') as f:
        readme_txt = f.read()
else:
    readme_txt = ''

if os.path.exists(LICENSE_FILE):
    with open(LICENSE_FILE, 'r') as f:
        license_txt = f.read()
else:
    license_txt = ''

setup(
    name='template',
    version='x.x.x',
    description='',
    long_description=readme_txt,
    long_description_content_type=README_TYPE,
    author='Michael Valdron',
    author_email='michael.valdron@email.com',
    url='https://github.com/michael-valdron/python-lib-template',
    license=license_txt,
    packages=find_packages(include=('src/*', 'tests/*')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)