import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from stl import mesh
pygame.init()

FPS = 60
clock = pygame.time.Clock()

display = pygame.display.set_mode((800, 800), DOUBLEBUF | OPENGL,24)

gluPerspective(45,1,1,500)
glClearColor(0.0,0.5,0.5,1)


stl_path = 'D:/cansat/UI/New GUI/3d/assem.stl'

stl_model = mesh.Mesh.from_file(stl_path)

vectors = stl_model.vectors
normals = stl_model.normals
print(len(vectors))

glLineWidth(4)
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)

    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)

    glBegin(GL_TRIANGLES)
    glColor3f(1,1,1)
    for triangle in vectors:
        for vertex in triangle:
            glVertex3fv(vertex)
            print(vertex)
    glEnd()

    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)

    glBegin(GL_TRIANGLES)
    glColor3f(0,0,0)
    for triangle in vectors:
        for vertex in triangle:
            glVertex3fv(vertex)
            print(vertex)
    glEnd()



    pygame.display.flip()
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(FPS)
