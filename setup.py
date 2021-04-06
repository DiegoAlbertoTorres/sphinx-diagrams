from setuptools import setup, find_packages

setup(
    name='sphinx-diagrams',
    version='0.1.0',
    author='Jean-Martin Archer',
    author_email='jm@jmartin.ca',
    python_requires='>=3.6',
    install_requires=[
        'diagrams>=0.17'
    ],
    packages=find_packages(include=['sphinx_diagrams'])
)
