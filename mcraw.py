#!/bin/python

database_path = "./items_db.pkl"

# used in recipe concatenation.
add_dict=lambda a,b:{i:a.get(i,0)+b.get(i,0) for i in set(a)|set(b)}

# My best idea ever!
output_streams = {
    "status": True,
    "debug": True,
    "comment": False}

def message(stream, msg, *args):
    """
    If stream is defined and enabled in output_streams, then print to
    stdout the stream and the message formatted with its arguments.
    """
    if stream not in output_streams:
        raise Error("I can't find the '{}' stream.".format(stream))
    print("{}: {}".format(stream, msg.format(*args)))

class Item:
    """
    Any item in Minecraft.
    """
    def __init__(self, id=None, natural=False, recipes=list()):
        """
        Dependencies is a dictionary of item-strings to numbers.  If
        the dictionary is empty, this implies that it is a raw
        material and is found naturally.

        It is an error for both natural to be false and recipes to be
        empty.  Thus, items must be created with at least one of them
        set.

        Keyword arguments:
           
                 id -- any Python object to be used as identification
                       (default None)

            natural -- if this is a naturally occurring resource
                       (default False)

            recipes -- a collection of recipes that can create this
                       item (default list())
        """
        message("debug", "Creating item (id={}, natural={}, recipes={})",\
                    str(id), bool(natural), bool(recipes))
        if not natural and len(recipes) is 0: # I prefer not to use
                                              # 'not recipes' because
                                              # I want to ensure
                                              # recipes is a
                                              # collection
            raise Error(\
                "The {} item is not natural and has no known recipes.".format(\
                    str(name)))
        self.id = id
        self.natural = natural
        self.recipes = recipes
    
    def reduce(self):
        """
        Reduce this item into a list of its raw dependencies.

        For each recipe in 'recipes', it again calls 'reduce' on each
        item in that recipe.  The recursion stops if and only if it
        encounters a natural item.  This is the base case.

        A list of super-recipes (recipes consisting only of naturally
        found items) is returned.
        """
        if natural:
            return self
        # else
        for recipe in self.recipes:
            for item in recipe:
                itemrecipes = item.reduce()

class Recipe:
    """
    A Minecraft recipe.
    """
    pass

def read_database(path):
    """Reads the passed file in as a database"""
    pass

def write_database(path):
    """Writes the current state of the database to path"""
    pass