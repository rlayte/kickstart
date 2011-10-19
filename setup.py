from setuptools import setup, find_packages

setup(
    name = 'kickstart',
    description = 'Framework agnostic setup script',
    long_description = open('README.md').read(),
    include_package_data = True,
    packages = ['kickstarter'],
    scripts = ['kickstart.py'],
    install_requires = ['PyYAML'],
    url = 'https://github.com/rlayte/kickstart',
    version = '0.292',
    author = 'Richard Layte',
    author_email = 'rich.layte@gmail.com'
)
