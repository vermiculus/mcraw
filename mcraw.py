#!/usr/bin/env python
# -*- mode: python -*-

for f in ['util', 'recipe', 'item', 'database']:
    execfile(f + '.py')
    message('debug', 'Imported {}', f)

import sys, os

mcrawdir = r'C:\Users\Sean\AppData\Roaming\.minecraft\mcraw'

# Most file operations work from within the McRaw directory.  By
# changing the working directory, we can simplify much of the file
# operations throughout the rest of the program.  If the user really
# needs to specify absolute filenames (which isn't likely, as I far as
# I can see), they can specify absolute filepaths.

os.chdir(mcrawdir)

def mcr(s = 'mcraw.cfg'):
    message('trace', 'in path generator')
    return '{}/{}'.format(mcrawdir, s)

def __configure(section, option, value):
    message('trace', 'in configuration')
    from ConfigParser import RawConfigParser
    parser = RawConfigParser()
    with open(mcr(), 'w+') as configuration:
        parser.readfp(configuration)
        configuration.seek(0)
        if not parser.has_section(section):
            parser.add_section(section)
        parser.set(section, option, value)
        parser.write(configuration)

# Process options
def setup():
    message('trace', 'in setup')
    def install():
        message('trace', 'in install')

    def createdb(db_name = sys.argv[3], \
                     file_name = sys.argv[3] + '.mcraw' if '--file' not in sys.argv \
                     else sys.argv[1 + sys.argv.index('--file')]):
        """
        Create a database.
        """
        message('trace', 'in createdb')

        message('status', \
                'Creating new database `{}` as `{}`.  ' + \
                    'Note relative file names will be handled ' + \
                    'according to $MCRAWDIR, `{}`', db_name, file_name, mcrawdir)
        
        with open(mcr(file_name), 'w') as f:
            f.write('meta name {}\n'.format(db_name))

        __configure('databases', db_name, file_name)

    def database():
        message('trace', 'in database')

    def validate():
        message('trace', 'in validate')

    locals()[sys.argv[2]]()
def info():
    message('trace', 'in info')

def reduce():
    message('trace', 'in reduce')

def item():
    message('trace', 'in item')
    def add():
        message('trace', 'in add')

    def rename():
        message('trace', 'in rename')

    def delete():
        message('trace', 'in delete')

    locals()[sys.argv[2]]()

def recipe():
    message('trace', 'in recipe')
    def add():
        message('trace', 'in add')

    def delete():
        message('trace', 'in delete')

    locals()[sys.argv[2]]()

def help2():
    message('trace', 'in help')


import sys


if __name__ == '__main__':
    message('debug', 'enter input')
    my_args = raw_input('? ')
    sys.argv = [sys.argv[0]] + my_args.split()


if len(sys.argv) > 1:
    try:
        locals()[sys.argv[1]]()
    except KeyError:
        message('status', 'Command not supported.')
else:
    message('status', 'No arguments given.')

