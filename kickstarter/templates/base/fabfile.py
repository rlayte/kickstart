from fabric.api import local


def symlink(file_name, link):
    local('sudo ln -sf %s %s' % (file_name, link))


def nginx():
    symlink('{{ PROJECT_ROOT }}/server/local/nginx.conf', '/etc/nginx/sites-available/{{ PROJECT_MODULE }}.conf')
    symlink('/etc/nginx/sites-available/{{ PROJECT_MODULE }}.conf', '/etc/nginx/sites-enabled/{{ PROJECT_MODULE }}.conf')
    local('sudo /etc/init.d/nginx restart')


def install_requirements():
    local('pip install -r requirements.pip')


def install_environment():
    local('pip install -e .')


def install(env):
    install_requirements()
    install_environment()
    local('sudo chmod 755 run.py')
    nginx()
