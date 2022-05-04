from setuptools import setup

setup(
    name="YouTube-Driver",
    version="0.1",
    packages=["YouTube-Driver"],
    license="MIT",
    author="Muhammad Haroon",
    author_email="mharoon@ucdavis.edu",
    url="https://github.com/ucdavis-noyce/YouTube-Driver",
    download_url="https://github.com/ucdavis-noyce/YouTube-Driver/archive/refs/tags/v0.1.tar.gz",
    description="Programmatically interact with YouTube's interface.",
    package_dir={"": "src"},
    install_requires=[
        'selenium',
        'pyvirtualdisplay'
    ]
)