from setuptools import setup

setup(
    name="YouTube-Driver",
    version="1.0.0",
    packages=["ytdriver"],
    license="MIT",
    author="Muhammad Haroon",
    author_email="mharoon@ucdavis.edu",
    url="https://github.com/ucdavis-noyce/YouTube-Driver",
    download_url="https://github.com/ucdavis-noyce/YouTube-Driver/archive/refs/tags/v1.0.0.tar.gz",
    description="Programmatically interact with YouTube's interface.",
    package_dir={"": "src"},
    install_requires=[
        'selenium',
        'pyvirtualdisplay'
    ]
)