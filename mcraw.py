#!/usr/bin/env python
# -*- mode: python -*-

for f in ['util', 'recipe', 'item', 'database']:
    execfile(f + '.py')
    message('debug', 'Imported {}', f)

<<<<<<< HEAD
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
=======
argerr = lambda cmd: message('error', 'Argument error.  \
Please see `{} {}` for usage information.'.format(sys.argv[0], cmd))

# Declare options
>>>>>>> c669d707e2c6b73c74c808f42f79a407df64fccf
def setup():
    """Perform relatively uncommon, menial setup tasks."""
    message('trace', 'in setup')
    def install():
        message('trace', 'in install')
        import os
        message('debug', 'imported os')
        message('input', 'Where would you like McRaw to keep its data files?')
        mcrawdir = raw_input('McRaw directory = ')
        os.environ['PATH'] += os.pathsep + mcrawdir
        
        # mcd: if the user gave the separator, don't add another to the arg
        mcd = lambda s: mcrawdir+s if mcrawdir[-1] is os.sep else mcrawdir+os.sep+s
        import shutil
        shutil.copyfile(sys.argv[0], mcd('mcraw'))

        os.chmod(sys.argv[0], 0755)

        message('status', 'Install complete.  You may now delete this directory.')

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
        interpreter = 'bash'
        script = 'validate.sh'
        
    try:
        locals()[sys.argv[2]]()
    except:
        argerr('help item')
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


# Process options
import sys
<<<<<<< HEAD


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

=======
try:
    locals()[sys.argv[1]]()
except:
    argerr('help')


>>>>>>> c669d707e2c6b73c74c808f42f79a407df64fccf
