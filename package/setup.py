from setuptools import setup

# Dependencies installed via 'pip install -e .'
requires = [
    'pyramid',
    'waitress',
]

setup(
    name='tutorial',
    install_requires=requires,
)
