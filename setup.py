from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='locano',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'requests[socks]',
    ],
    entry_points={
        'console_scripts': [
            'locano=locano.locano:main',
        ],
    },
    author='raj yadav',
    author_email='raajyadav@myyahoo.com',
    description='locano - Automate IP address changes using Tor',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rajyadav-cyber/locano',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
