from setuptools import setup

setup(
    name='pyfinity',
    version='0.0.1',
    packages=['pyfinity'],
    install_requires=[
        'requests',
        'importlib; python_version == "2.6"',
    ],
)