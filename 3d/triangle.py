import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from stl import mesh
import numpy as np
import pandas as pd
from time import sleep
pygame.init()

FPS = 60
clock = pygame.time.Clock()
display = pygame.display.set_mode((600, 400), DOUBLEBUF | OPENGL, 24)
df = pd.read_csv('D:/cansat/UI/New GUI/DATA.csv')
x = list(df['EULERX'])
y = list(df['EULERY'])
z = list(df['EULERZ'])
tim = list(df['TIME_STAMPING'])
gluPerspective(60, 1, 1, 1000)
glClearColor(0.0, 0.5, 0.5, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_LIGHT1)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
# glEnable(GL_COLOR_MATERIAL)
glTranslatef(0, 0, -500)
# Set light position behind the camera
running = True
rotation_angle = 0.5  # Initial rotation angle (in degrees)
depth = 500
start = 3319
stl_path = 'D:/cansat/UI/New GUI/3d/assem.stl'
stl_model = mesh.Mesh.from_file(stl_path)

# Flatten the vectors array for VBO
flat_vertices = np.array(stl_model.vectors).flatten()
center = np.mean(stl_model.vectors.reshape((-1, 3)), axis=0)
# Generate VBO
vbo = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, flat_vertices, GL_STATIC_DRAW)
glBindBuffer(GL_ARRAY_BUFFER, 0)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()  # Push the current matrix onto the matrix stack

    # Apply rotation around the Y-axis
    
    glRotatef(rotation_angle, 1, 1, 1)
    glLightfv(GL_LIGHT0, GL_POSITION, (100, 100, 100, 1))
    glLightfv(GL_LIGHT1, GL_POSITION, (-100, -100, 100, 1))
    # Translate to the object's center

    glTranslatef(-center[0], -center[1], -center[2])

    glEnableClientState(GL_VERTEX_ARRAY)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glVertexPointer(3, GL_FLOAT, 0, None)

    
    glColor3f(1, 1, 1)
    glDrawArrays(GL_TRIANGLES, 0, len(flat_vertices) // 3)

    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # glColor3f(0, 0, 0)
    # glDrawArrays(GL_TRIANGLES, 0, len(flat_vertices) // 3)
    # glDisableClientState(GL_VERTEX_ARRAY)

    glPopMatrix()  # Pop the matrix stack to revert to the previous transformation

    pygame.display.flip()
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(FPS)
    rotation_angle += 0.5


    
    
    
