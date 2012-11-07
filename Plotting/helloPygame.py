import helloPygame, sys
from helloPygame.locals import *

# Setup pygame
helloPygame.init()

# Intialize a 640x480 pixel screen
screen = helloPygame.display.set_mode((640,480))

# Draw a red rectangle at coordinate (200, 100) of size (100, 50)
RED = (255, 0, 0) # RGB
GREEN = (0, 255, 0)
helloPygame.draw.rect(screen, RED, (200, 100, 100, 50))

# set up fonts
basicFont = helloPygame.font.SysFont(None, 48)

# Draw green text on the center of the screen
text = basicFont.render('Hello world!', True, GREEN)
textpos = text.get_rect()
textpos.centerx = screen.get_rect().centerx
textpos.centery = screen.get_rect().centery
screen.blit(text, textpos)

# Update display to show the drawn items
helloPygame.display.update()

# Enter GUI loop
while True:
    for event in helloPygame.event.get():
        if event.type == QUIT:
            helloPygame.quit()
            sys.exit()