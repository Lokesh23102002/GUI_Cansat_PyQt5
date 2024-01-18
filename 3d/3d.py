import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

FPS = 60
clock = pygame.time.Clock()

display = pygame.display.set_mode((1200, 800), DOUBLEBUF | OPENGL,24)

gluPerspective(45,1,1,500)
glClearColor(0.0,0.5,0.5,1)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)

    glRotatef(1,3,1,1)



    pygame.display.flip()
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(FPS)
