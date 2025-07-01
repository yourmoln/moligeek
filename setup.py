from setuptools import setup, find_packages

import os
info = {}
PATH = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(PATH, "moligeek/__version__.py"), 'r', encoding='utf8') as f:
    exec(f.read(), info)

with open(os.path.join(PATH, "README.md"), 'r', encoding='utf8') as f:
    long_description = f.read()
with open('requirements.txt', 'r') as file:
    lines = file.readlines()
    requires = [line.strip() for line in lines]



setup(
    name = info['__name__'],
    version = info['__version__'],
    author = info['__author__'],
    author_email = info['__author_email__'],
    description = info['__description__'],
    license = info["__license__"],
    url = info['__url__'], 
    python_requires = ">=3.8",

    packages=find_packages(),
    include_package_data = True,
    long_description = long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,

    classifiers = [
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.8',
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],

    install_requires=requires,

    tests_require=[
        'pytest>=3.3.1',
        'pytest-cov>=2.5.1',
    ],
    entry_points={
        'console_scripts': [
            'moligeek = moligeek:run',
        ],
    }
)