/* 
Compile: gcc -o output/square square.c -lGL -lGLU -lglut
Run: ./output/square
*/


/* 
    Draw a square OpenGL program in C
*/

#include <GL/glut.h>

void drawSquare(void){
    glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_POLYGON);
    glColor3f(0.0, 0.8, 1.0);
    glVertex2f(-0.5,-0.5); // top-left position
    glVertex2f( 0.5,-0.5); // top-right postion
    glVertex2f( 0.5, 0.5); // bottom-right postion
    glVertex2f(-0.5, 0.5); // bottom-left postion
    glEnd();    

    glFlush();
}

int main(int argc, char** argv){
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutCreateWindow("Square Program");
    glutInitWindowSize(100, 100);
    glutDisplayFunc(drawSquare);
    glutMainLoop();
    return 0;
}