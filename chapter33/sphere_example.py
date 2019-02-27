from OpenGL.GLUT import *
from OpenGL.GL import *
import sys


#  Initialize material property and light source.
def init():
    light_ambient = [0.0, 0.0, 0.0, 1.0]
    light_diffuse = [1.0, 1.0, 1.0, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]
    #  light_position is NOT default value
    light_position = [1.0, 1.0, 1.0, 0.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(20.0, 1.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(-0.75, 0.5, 0.0);
    glRotatef(90.0, 1.0, 0.0, 0.0)
    glutSolidTorus(0.275, 0.85, 15, 15)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.75, -0.5, 0.0);
    glRotatef(270.0, 1.0, 0.0, 0.0)
    glutSolidCone(1.0, 2.0, 15, 15)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.75, 0.0, -1.0)
    glutSolidSphere(1.0, 15, 15)
    glPopMatrix()

    glPopMatrix()
    glFlush()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if w <= h:
        glOrtho(-2.5, 2.5, -2.5 * h / w,
                2.5 * h / w, -10.0, 10.0)
    else:
        glOrtho(-2.5 * w / h,
                2.5 * w / h, -2.5, 2.5, -10.0, 10.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard(key, x, y):
    if key == chr(27):
        sys.exit(0)


#  Main Loop
#  Open window with initial window size, title bar,
#  RGBA display mode, and handle input events.

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow('scene')
init()
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutDisplayFunc(display)
glutMainLoop()
