#!/usr/bin/env python
# -*- mode: python -*-

for f in ['util', 'recipe', 'item', 'database']:
    execfile(f + '.py')
    message('debug', 'Imported {}', f)

argerr = lambda cmd: message('error', 'Argument error.  \
Please see `{} {}` for usage information.'.format(sys.argv[0], cmd))

# Declare options
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

    def createdb():
        message('trace', 'in createdb')

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

def help():
    message('trace', 'in help')


# Process options
import sys
try:
    locals()[sys.argv[1]]()
except:
    argerr('help')


