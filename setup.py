
from setuptools import setup, find_packages

setup(
    name='shoestring',
    version='0.0.1',
    description='A minimalist SPA e-commerce app for Django',
    author='Curtis Maloney',
    author_email='curtis@tinbrain.net',
    packages=find_packages(exclude=['proj.*']),
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
    ],
    install_requires=[
        'Django>=1.7',
    ],
    test_suite='tests',
)
