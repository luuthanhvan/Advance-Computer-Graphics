'''
    Draw a square OpenGL program in Python
'''

from OpenGL.GL import *
from OpenGL.GLUT import *

def drawSquare():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.8, 1.0)
    glVertex2f(-0.5,-0.5) # top-left position
    glVertex2f( 0.5,-0.5) # top-right position
    glVertex2f( 0.5, 0.5) # bottom-right position
    glVertex2f(-0.5, 0.5) # bottom-left position
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow(b"Square Program")
    glutInitWindowSize(100, 100)
    glutDisplayFunc(drawSquare)
    glutMainLoop()

if __name__=="__main__":
    main()