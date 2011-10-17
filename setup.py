from setuptools import setup, find_packages

setup(
    name = 'kickstart',
    scripts = ['kickstart.py'],
    packages = find_packages(),
    url = 'http://pypi.python.org/pypi/kickstart',
    version = '0.22',
    install_requires = ['PyYAML'],
    description = 'Framework agnostic setup script',
    author = 'Richard Layte',
    author_email = 'rich.layte@gmail.com'
)
