from setuptools import setup, find_packages


setup(
    name = 'kickstart',
    description = 'Framework agnostic setup script',
    include_package_data = True,
    packages = ['kickstarter'],
    scripts = ['kickstart.py'],
    install_requires = ['PyYAML'],
    url = 'https://github.com/rlayte/kickstart',
    version = '0.294',
    author = 'Richard Layte',
    author_email = 'rich.layte@gmail.com'
)
