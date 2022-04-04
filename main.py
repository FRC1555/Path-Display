from tkinter import *

import pyglet
from pyglet import shapes
from pyglet.window import Window, key, mouse

from path import *

path = []
interpolatedPath = []
newPath = []

# TODO: Segment the code more, maybe seperate into classes and/or seperate files?
# TODO: Add JSON Config reading, writing system for Universal config settings
# TODO: Start Working On Diologe Boxes for Editing Config on the fly in app not in JSON file
# TODO: Migrate to borderless window with custom button for [min], [exit], [file], etc...

#### Add all to JSON later ####

# Settings Color(s)
background = (42, 44, 45) ## Very Dark Gray
border = (34, 34, 35)

# Point Color(s)
truePointColor = (255, 255, 255)
interpolatedPoinColor = (0, 255, 255)

# Point Sizes
truePointSize = 4
interpolatedPointSize = 2

# Config
trajName = "Jimbo"

#Spacing 
spacing = 20

# Smoothing Function Parameters
smoothing = 0.9
weight = 0.1
tolerance = 0.132

###############################

ws = Tk()
window = pyglet.window.Window(645, 324, style=Window.WINDOW_STYLE_DEFAULT) # 900 - 648 for settingscol
window.set_caption('Path Creator')
batch = pyglet.graphics.Batch()

#Draws the paths using midpoint formula
def drawPaths():
    for i in range(0, len(path)):
        newPath = interpolate(path, spacing)
        for i in range(len(newPath)):
            interpolatedPath.append(newPath[i])

    for i in range(0, len(interpolatedPath)):
        point = shapes.Circle(interpolatedPath[i][0], interpolatedPath[i][1], interpolatedPointSize, color=interpolatedPoinColor, batch=batch)  
        batch.draw()


    for i in range(0, len(path)):
        point = shapes.Circle(path[i][0], path[i][1], truePointSize, color=truePointColor, batch=batch)
        batch.draw()
        interpolatedPath.clear()

def drawSettingOverlay():
    box = shapes.Rectangle(647, 0, 900-647, 648, color=border, batch=batch)
    batch.draw()

@window.event
def on_draw():
    window.clear()
    batch.draw()

    background = pyglet.image.load("FRC2022Field.bmp")
    background.blit(0, 0)

    drawPaths()

    #drawSettingOverlay()

@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        interpolatedPath.clear()
        path.append([x, y])

@window.event
def on_key_press(symbol, modifiers):
    # Symbolic names:
    if symbol == key.ESCAPE:
        pyglet.app.exit()
    # Alphabet keys:
    elif symbol == key.BACKSPACE:
        if 1 == len(path):
            path.clear()
            interpolatedPath.clear()
        else:
            path.pop()

    # Number keys:
    elif symbol == key.R:
        path.clear()
        interpolatedPath.clear()

    elif symbol == key.F12:
        #message = """
        #    Words
        #"""
#
        #text_box = Text(
        #    ws,
        #    height=12,
        #    width=40
        #)
        #text_box.pack(expand=True)
        #text_box.insert('end', message)
        #text_box.config(state='disabled')
#
        #ws.mainloop()
        pass #Do Something soon?
    # Number keypad keys:
    elif symbol == key.RETURN:
        print("########NEW#############")
        for i in range(len(path)):
          str1 = ".addWaypoint(new Point(" #VAL
          str2 = ", " #VAL
          str3 = "));"
        
          newPos = path[i]
        
          x = newPos[0]
          y = newPos[1]
        
          print(trajName + str1 + str(x) + str2 + str(y) + str3)

def run():

    pyglet.app.run()

run()
