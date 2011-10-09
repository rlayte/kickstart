from fabric.api import local


def symlink(file_name, link):
    local('sudo ln -sf %s %s' % (file_name, link))


def nginx():
    symlink('/projects/roomd/server/local/nginx.conf', '/etc/nginx/sites-available/flat_finder.conf')
    symlink('/etc/nginx/sites-available/flat_finder.conf', '/etc/nginx/sites-enabled/flat_finder.conf')
    local('sudo /etc/init.d/nginx restart')


def install_requirements():
    local('pip install -r requirements.pip')


def install():
    nginx()
    install_requirements()
