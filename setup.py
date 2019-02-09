from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='bitfinex-tencars',
    version='1.3',
    packages=['bitfinex'],
    url='https://github.com/akcarsten/bitfinex',
    license='',
    author='Carsten Klein',
    author_email='https://www.linkedin.com/in/carsten-klein/',
    description='Bitfinex REST API client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
