from setuptools import setup

setup(
    name="YouTube-Driver",
    version="0.1",
    packages=["ytdriver"],
    license="MIT",
    author="Muhammad Haroon",
    author_email="mharoon@ucdavis.edu",
    url="https://github.com/ucdavis-noyce/YouTube-Driver",
    download_url="",
    description="Programmatically interact with YouTube's interface.",
    long_description="README.md",
    package_dir={"": "src"},
    install_requires=[
        'selenium',
        'pyvirtualdisplay'
    ]
)