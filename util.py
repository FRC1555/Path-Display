import pygame, sys
from pgu import gui

class SimpleDialog(gui.Dialog):
    def __init__(self):
        title = gui.Label("Spam")
        main = gui.Container(width=20, height=20)
        # I patched PGU to use new style classes.
        super(SimpleDialog, self).__init__(title, main, width=40, height=40)

    def close(self, *args, **kwargs):
        print("closing")
        return super(SimpleDialog, self).close(*args, **kwargs)