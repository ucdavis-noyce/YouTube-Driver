from setuptools import setup
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="YouTube-Driver",
    version="1.0.1",
    packages=["ytdriver"],
    license="MIT",
    author="Muhammad Haroon",
    author_email="mharoon@ucdavis.edu",
    url="https://github.com/ucdavis-noyce/YouTube-Driver",
    download_url="https://github.com/ucdavis-noyce/YouTube-Driver/archive/refs/tags/v1.0.1.tar.gz",
    description="Programmatically interact with YouTube's interface.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={"": "src"},
    install_requires=[
        'selenium',
        'pyvirtualdisplay'
    ]
)