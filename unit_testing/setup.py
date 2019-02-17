from setuptools import setup

# Dependencies installed via 'pip install -e .'
requires = [
    'pyramid',
    'waitress',
]

# Dependencies installed via 'pip install -e ".[dev]"'
dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
]

setup(
    name='tutorial',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main'
        ],
    },
)
