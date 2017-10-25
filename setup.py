"""
    A setuptools based setup module.
    See:
        https://packaging.python.org/en/latest/distributing.html
        https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages


# To use a consistent encoding
from codecs import open


# Permit work wiht path and file i/o
from os import path


here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jaiminho',
    version='0.0.2',
    description='A sample Python project',
    long_description=long_description,
    url='https://github.com/pypa/sampleproject',
    author='The Python Packaging Authority',
    author_email='pypa-dev@googlegroups.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6.3',
    ],
    keywords='sample setuptools development reuso-de-software',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'env', 'packaging.python.org', 'pip_server'], ),
    install_requires=['peppercorn', 'pygments', 'boto3'],
    extras_require={
        'dev': ['check-manifest', 'wheel'],
        'test': ['coverage', 'behave'],
    },
    package_data={
        'sample': ['package_data.dat'],
    },
    data_files=[('my_data', ['data/data_file'])],
    entry_points={
        'console_scripts': [
            'sample=sample:main',
            'jaiminho=cli.app:main',
        ],
    },
    python_requires='~=3.3',
)
