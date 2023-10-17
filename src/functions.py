from __init__ import *

def __Open_Link( name: str = ... ) -> object:
    open(name)


def __GetJoke():
    pyjokes.get_joke(language="en", category="all")


def __GetJokes():
    pyjokes.get_jokes(language="en", category="all")



open_link = __Open_Link
joke = __GetJoke
jokes = __GetJokes
