# PyGame template.
 
# Import standard modules.
import sys
 
# Import non-standard modules.
import pygame
from pygame.locals import *

from path import *

path = []
interpolatedPath = []
finalPath = []

# Config
trajName = "joe"

#Spacing 
spacing = 20

# Smoothing Function Parameters
smoothing = 0.9
weight = 0.1
tolerance = 0.132
 
def update(dt):
  """
  Update game. Called once per frame.
  dt is the amount of time passed since last frame.
  If you want to have constant apparent movement no matter your framerate,
  what you can do is something like
  
  x += v * dt
  
  and this will scale your velocity based on time. Extend as necessary."""
  
  # Go through events that are passed to the script by the window.
  for event in pygame.event.get():
    # We need to handle these events. Initially the only one you'll want to care
    # about is the QUIT event, because if you don't handle it, your game will crash
    # whenever someone tries to exit.

    if event.type == MOUSEBUTTONUP:
        path.append([pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]])
        newPath = interpolate(path, spacing)

        for i in range(len(newPath)):
            interpolatedPath.append(newPath[i])

            print("########NEW#############")
            for i in range(len(path)):
              str1 = ".addWaypoint(new Pose2D(" #VAL
              str2 = ", " #VAL
              str3 = ", 0));"
          
              newPos = normalize(path[i], 648)
          
              x = newPos[0]
              y = newPos[1]
          
              print(trajName + str1 + str(x) + str2 + str(y) + str3)

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_r:
        runPyGame()


    if event.type == QUIT:
      pygame.quit() # Opposite of pygame.init
      sys.exit() # Not including this line crashes the script on Windows. Possibly
      # on other operating systems too, but I don't know for sure.
    # Handle other events as you wish.
 
def draw(screen):
  """
  Draw things to the window. Called once per frame.
  """
  #screen.fill((0, 0, 0)) # Fill the screen with black.

  bg = pygame.image.load("Frieght_Frenzy_Field_Cool.bmp")

  screen.blit(bg, (0, 0))

  for i in range(0, len(path)):
    pygame.draw.circle(screen, (255, 255, 255), (path[i][0], path[i][1]), 4)
  for i in range(0, len(interpolatedPath)):
    pygame.draw.circle(screen, (255, 255, 255), (interpolatedPath[i][0], interpolatedPath[i][1]), 2)
   
  # Redraw screen here.
  # Flip the display so that the things we drew actually show up.
  pygame.display.flip()
 
def runPyGame():
  # Initialise PyGame.
  pygame.init()
  
  # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
  fps = 60.0
  fpsClock = pygame.time.Clock()
  
  # Set up the window.
  width, height = 648, 648
  screen = pygame.display.set_mode((width, height))
  
  # screen is the surface representing the window.
  # PyGame surfaces can be thought of as screen sections that you can draw onto.
  # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
  
  # Main game loop.
  dt = 1/fps # dt is the time since last frame.
  while True: # Loop forever!
    update(dt) # You can update/draw here, I've just moved the code for neatness.
    draw(screen)

    dt = fpsClock.tick(fps)

runPyGame()