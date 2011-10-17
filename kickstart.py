#! /usr/bin/env python
import os, sys, shutil, re, yaml
from optparse import OptionParser

import kickstart

parser = OptionParser()
parser.add_option("-t", "--template", dest="template", help="base project template", default="base")
parser.add_option("-c", "--config", dest="config", help="yaml file to provide setup variables", default="config.yaml")
(options, args) = parser.parse_args()

template_dir = os.path.join(kickstart.__path__[0], options.template)

config = {}
config['project'] = re.sub('\-', '_', args[0])
config['project_module'] = re.sub('\-', '_', args[0])
config['project_name'] = args[0]
config['project_root'] = '%s/%s' % (os.getcwd(), args[0])


def replace_variable(match):
    key = match.groups(1)[0].lower()
    return config[key]


def create_project(name, template):
    def copy_template():
        config_prompt(template, options.config)
        shutil.copytree(template, name)
        shutil.copytree('%s/%s' % (name, options.template), '%s/%s' % (name, config['project'])) 
        shutil.rmtree('%s/%s' % (name, options.template))
        os.remove('%s/%s' % (name, options.config))

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


def config_prompt(template, config_file):
    c = open('%s/%s' % (template, config_file), 'r')
    parsed_conf = re.sub('{{\s*(\w+)\s*}}', args[0], c.read())
    c.close()

    conf = yaml.load(parsed_conf)
    for option in conf:
        default = conf[option]
        value = str(raw_input('%s (leave blank for %s): ' % (option, default)))
        config[option.lower()] = value if value != '' else default


create_project(args[0], template_dir)
