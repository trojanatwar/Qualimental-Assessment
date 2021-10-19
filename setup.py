from setuptools import setup

# List of dependencies installed via `pip install -e .`
# by virtue of the Setuptools `install_requires` value below.
requires = [
    'deform',
    'pyramid==2.0',
    'pyramid_chameleon',
    'pyramid_tm',
    'sqlalchemy',
    'waitress',
    'zope.sqlalchemy',
    'pyramid_heroku',
    'psycopg2-binary',
    'pyramid_debugtoolbar',
    'tqdm',
    'pyramid_openapi3'
]

# List of dependencies installed via `pip install -e ".[dev]"`
# by virtue of the Setuptools `extras_require` value in the Python
# dictionary below.
dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
    'webtest',
]

setup(
    name='qualimental.assessment.pythonbackend',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = src:main'
        ],
        'console_scripts': [
            'initialize_tutorial_db = src.initialise_db:main'
        ],
    },
)
