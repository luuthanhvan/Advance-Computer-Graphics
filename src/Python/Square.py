from OpenGL.GL import *
from OpenGL.GLUT import *

def draw1():
    glColor3d(0.0, 0.8, 1.0)
    glBegin(GL_POLYGON)
    glVertex2d(-0.5, -0.5)
    glVertex2d( 0.5, -0.5)
    glVertex2d( 0.5, 0.5)
    glVertex2d(-0.5, 0.5)
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"Square Program")
glutInitWindowSize(100, 100)   # Set the window's initial width & height
glutDisplayFunc(draw1)
glutMainLoop()

