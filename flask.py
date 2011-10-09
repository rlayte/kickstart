#! /usr/bin/env python

import os, sys, shutil, re


def create_project(name):
    if os.path.exists('./%s' % name):
        print '%s already exists' % name
    else:
        shutil.copytree('base', name)
        shutil.copytree('%s/base' % name, '%s/%s' % (name, name))
        shutil.rmtree('%s/base' % name)

        for dirname, dirnames, files in os.walk(name):
            for filename in files:
                f = open('%s/%s' % (dirname, filename), 'r')
                lines = f.readlines()
                f.close()

                new_lines = []
                for line in lines:
                    match = re.sub('{{\s*(\w+)\s*}}', name, line)
                    new_lines.append(match)

                f = open('%s/%s' % (dirname, filename), 'w')
                f.write(''.join(new_lines))
                f.close()


create_project(sys.argv[1])
