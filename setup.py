import os
from setuptools import setup, find_packages

project_name = 'fastbroker'

with open('VERSION') as v:
    project_version = v.read().strip()


def requirements():
    try:
        with open('requirements.txt') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(os.path.abspath(os.curdir))
        print(os.listdir('.'))
        raise


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name=project_name,
    version=project_version,
    python_requires='>=3.7.0',
    packages=find_packages('src'),
    url='https://github.com/cetanu/fastbroker',
    license='MIT',
    author='Vassilios Syrakis',
    author_email='cetanu@gmail.com',
    description='Open Service Broker framework built on FastAPI',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(),
    command_options={
        'build_sphinx': {
            'project': ('setup.py', project_name),
            'version': ('setup.py', project_version),
            'release': ('setup.py', project_version),
            'source_dir': ('setup.py', 'docs'),
            'config_dir': ('setup.py', 'docs'),
            'build_dir': ('setup.py', 'src/sovereign/docs'),
            'builder': ('setup.py', 'html')
        }
    }
)
