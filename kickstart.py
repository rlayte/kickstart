#! /usr/bin/env python
import os, sys, shutil, re, yaml
from optparse import OptionParser

import kickstarter

parser = OptionParser()
parser.add_option("-t", "--template", dest="template", help="default project template", default="default")
parser.add_option("-a", "--add-template", dest="add", help="install new template")
parser.add_option("-r", "--remove-template", dest="remove", help="remove a template")
parser.add_option("-d", "--default", dest="default_template", help="set default template")
(options, args) = parser.parse_args()

template_dir = os.path.join(kickstarter.__path__[0], 'templates', options.template)


def set_default():
    templates_dir = os.path.join(kickstarter.__path__[0], 'templates')
    shutil.rmtree('%s/default' % templates_dir)
    shutil.copytree('%s/%s' % (templates_dir, options.default_template), '%s/%s' % (templates_dir, 'default'))
    shutil.copytree('%s/default/%s' % (templates_dir, options.default_template), '%s/default/default' % templates_dir)
    shutil.rmtree('%s/default/%s' % (templates_dir, options.default_template))


def create_template():
    templates_dir = os.path.join(kickstarter.__path__[0], 'templates')
    shutil.copytree(options.add, '%s/%s' % (templates_dir, options.add))


def remove_template():
    templates_dir = os.path.join(kickstarter.__path__[0], 'templates')
    shutil.rmtree('%s/%s' % (templates_dir, options.remove))


def create_project(name, template):
    config = {}
    config['project'] = re.sub('\-', '_', args[0])
    config['project_module'] = re.sub('\-', '_', args[0])
    config['project_name'] = args[0]
    config['project_root'] = '%s/%s' % (os.getcwd(), args[0])

    def replace_variable(match):
        key = match.groups(1)[0].lower()
        return config[key]

    def config_prompt(template):
        if os.path.exists('%s/%s' % (template, 'config.yaml')):
            c = open('%s/%s' % (template, 'config.yaml'), 'r')
            parsed_conf = re.sub('{{\s*(\w+)\s*}}', args[0], c.read())
            c.close()

            conf = yaml.load(parsed_conf)
            for option in conf:
                default = conf[option]
                value = str(raw_input('%s (leave blank for %s): ' % (option, default)))
                config[option.lower()] = value if value != '' else default

    def copy_template():
        config_prompt(template)
        shutil.copytree(template, name)
        shutil.copytree('%s/%s' % (name, options.template), '%s/%s' % (name, config['project'])) 
        shutil.rmtree('%s/%s' % (name, options.template))

        if os.path.exists('%s/%s' % (name, 'config.yaml')):
            os.remove('%s/%s' % (name, 'config.yaml'))

        for dirname, dirnames, files in os.walk(name):
            for filename in files:
                f = open('%s/%s' % (dirname, filename), 'r')
                lines = f.readlines()
                f.close()

                first_pass = [re.sub('{{\s*(\w+)\s*}}', replace_variable, line) for line in lines]
                new_lines = [re.sub('__config_(\w+)__', replace_variable, line) for line in first_pass]

                f = open('%s/%s' % (dirname, filename), 'w')
                f.write(''.join(new_lines))
                f.close()

    if os.path.exists('./%s' % name):
        override = raw_input('%s already exists. Override? [y/n]: ' % name)

        if override == 'y':
            shutil.rmtree('./%s' % name)
            copy_template()
        else:
            print 'Aborting'
    else:
        copy_template()

if options.add:
    create_template()
elif options.remove:
    remove_template()
elif options.default_template:
    set_default()
else:
    create_project(args[0], template_dir)
