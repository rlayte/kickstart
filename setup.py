from setuptools import setup, find_packages

setup(
    name = 'kickstart',
    include_package_data = True,
    packages = ['kickstarter'],
    scripts = ['kickstart.py'],
    install_requires = ['PyYAML'],
    url = 'http://pypi.python.org/pypi/kickstart',
    version = '0.282',
    description = 'Framework agnostic setup script',
    author = 'Richard Layte',
    author_email = 'rich.layte@gmail.com'
)
