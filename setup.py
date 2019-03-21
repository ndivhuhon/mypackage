from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='This library helps to publish functions for recursion and sorting',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/ndivhuhon/mypackage',
    author='Ndivhuho',
    author_email='ndivhuhon@gmail.com'
    )
