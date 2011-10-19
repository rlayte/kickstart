## Basic usage
    
    $ [sudo] pip install kickstart
    $ kickstart.py hello-world

This will create a skeleton project within the current working directory. The default is a Flask app - see below for details on how to change this.


## Using a different template

To use a different template pass a template name to the `-t` flag - e.g.

    $ kickstart.py hello-django -t django

To list all currently installed templates run the command with `-l`

    $ kickstart.py -l
    flask
    django
    ...

To set the default template pass an installed template name to the `--default` parameter - e.g.

    $ kickstart.py --default django

This will then create a Django project without the need to specify the template

    $ kickstart.py hello-django


## Creating a custom template

If you set your projects up differently or use a framework that isn't supported you can create your own project templates.

    $ kickstart.py --add <path/to/django/template>

The path should point to a directory that contains the layout for your project with template variables to define any project specific settings. You have access to some default variables that are defined based on the project name and location:

    PROJECT_NAME: the name supplied to the kickstart.py command
    PROJECT_MODULE: same as project name, but parsed to be valid python
    PROJECT_ROOT: location of the created project

To use these in your template use Django/Jinja2 syntax. For example in your `fabfile.py` you could do something like:

    symlink('{{ PROJECT_ROOT }}/server/local/nginx.conf', '/etc/nginx/sites-available/{{ PROJECT_MODULE }}.conf')

Will render

    symlink('/projects/my-project/server/local/nginx.conf', '/etc/nginx/sites-available/my_project.conf')

If you need to render a variable in python code, to import app-specific modules for example, then use `__config_variable_name__`. e.g.

    from __config_project_name__ import app

Will render

    from my_project import app

Additionally, the template directory can also contain a `config.yaml` file that defines any extra values that need to be supplied during setup. For example, if you to define `HOST` and `PORT` for use in the nginx template you could create the following yaml file:

    name: my-template
    description: a simple example

    config:
        host: '0.0.0.0'
        port: '5000

If you now use this template you will be prompted to provide each of these settings (the values defined in the yaml file are used as default)

    $ kickstart.py my-project -t my-template
    $ host (leave blank for 0.0.0.0):
    $ port (leave blank for 5000):

You would then have access to those values as `HOST` and `PORT` in your project template files.

If you need to remove a template pass its name to the `--remove` flag

    $ kickstart.py --remove django
