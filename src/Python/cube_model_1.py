# Import PyGame library 
import pygame
from pygame.locals import *

# Import OpenGL library
from OpenGL.GL import *
from OpenGL.GLU import *

# Define 8 vertices of a Cube
verticies = (
    (1, -1, -1), # vertex 0
    (1, 1, -1), # vertex 1
    (-1, 1, -1), # vertex 2
    (-1, -1, -1), # vertex 3
    (1, -1, 1), # vertex 4
    (1, 1, 1), # vertex 5
    (-1, -1, 1), # vertex 6
    (-1, 1, 1) # vertex 7
)

# Define 12 edges which connect all vertices of the Cube
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

# Define 6 surfaces of the Cube (a surface is a collection of 4 vertex)
surfaces = (
    (0, 1, 2, 3), # behind 
    (3, 2, 7, 6), # left
    (6, 7, 5, 4), # front
    (4, 5, 1, 0), # right
    (1, 5, 7, 2), # up
    (4, 0, 3, 6) # down
)

# Define colors of the Cube
colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)


def Cube():
    # draw surfaces and colors of the Cube
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()

    # draw vetices and edges of the Cube
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    # Using PyGame window to display the OpenGL object
    pygame.init()
    display = (800,600) # specify the size of the window for display
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # gluPerspective(): set up a perspective projection matrix
    # Learn more at https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/gluPerspective.xml
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5) # z = -5: translate the cube away from the screen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

# Calling main function
if __name__ == "__main__":
    main()