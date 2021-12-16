import pyglet

window = pyglet.window.Window(648, 648, caption='Path Creator', resizable=False)

@window.event
def on_draw():
    window.clear()

    background = pyglet.image.load("Frieght_Frenzy_Field_Cool.bmp")
    background.blit(0, 0)
    



def run():
    pyglet.app.run()

run()