from setuptools import setup

setup(
    name='commitizer',
    version='1.0',
    description='Generate patterns and keep your GitHub contribution streak going',
    author='S P Sharan, Barath Kumar S',
    author_email='spsharan2000@gmail.com',
    packages=['commitizer'],
    entry_points={
        'console_scripts': ['commitizer=commitizer.cli:main'],
    },
)
