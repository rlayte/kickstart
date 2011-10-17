from distutils.core import setup

setup(
    name = 'kickstart',
    scripts = ['kickstart.py'],
    packages = ['kickstart'],
    url = 'http://pypi.python.org/pypi/kickstart',
    version = '0.21',
    install_requires = ['PyYAML'],
    description = 'Framework agnostic setup script',
    author = 'Richard Layte',
    author_email = 'rich.layte@gmail.com'
)
