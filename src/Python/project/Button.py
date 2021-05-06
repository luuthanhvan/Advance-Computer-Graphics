from OpenGL.GL import *
from OpenGL.GLU import *

class Button:
    def __init__(self, vertices, color):
        self.vertices = vertices
        self.color = color
    
    def draw(self):
        glBegin(GL_POLYGON)
        glColor3f(self.color['r'], self.color['g'], self.color['b'])
        
        # glVertex2f(-0.9, 0.9)
        # glVertex2f(-0.7, 0.9)
        # glVertex2f(-0.7, 0.8)
        # glVertex2f(-0.9, 0.8)
        glVertex2f(self.vertices['top_left'][0], self.vertices['top_left'][1])
        glVertex2f(self.vertices['top_right'][0], self.vertices['top_right'][1])
        glVertex2f(self.vertices['bottom_left'][0], self.vertices['bottom_left'][1])
        glVertex2f(self.vertices['bottom_right'][0], self.vertices['bottom_right'][1])

        glEnd()
        glFlush()
