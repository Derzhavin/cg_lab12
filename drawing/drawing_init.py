from OpenGL.GL import *
from OpenGL.GLUT import *


def init_gl(gl_widget):
    gl_widget.initializeGL()
    gl_widget.paintGL = paint_gl
    gl_widget.initializeGL = initialize_gl


def paint_gl():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)

def initialize_gl():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_DEPTH_TEST)
