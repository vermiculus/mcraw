#!/bin/python

for f in ['util', 'recipe', 'item', 'database']:
    execfile(f + '.py')
    message('debug', 'Imported {}', f)

# Process options
def setup():
    message('trace', 'in setup')
    def install():
        message('trace', 'in install')

    def createdb():
        message('trace', 'in createdb')

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

def help():
    message('trace', 'in help')


import sys
locals()[sys.argv[1]]()
