from setuptools import setup

setup(
    name="YouTube-Driver",
    version="0.1",
    packages=["ytdriver"],
    author="Muhammad Haroon",
    author_email="m_haroon96@hotmail.com",
    description="Programmatically interact with YouTube's interface.",
    install_requires=[
        'selenium',
        'pyvirtualdisplay'
    ]
)