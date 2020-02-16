from OpenGL.GL import *

from .utilities import *


def init_gl_widget(gl_widget, model):
    gl_widget.initializeGL()
    gl_widget.paintGL = lambda: paint_gl(model, gl_widget)
    gl_widget.initializeGL = initialize_gl
    gl_widget.resizeGL = lambda w, h: resize_gl(gl_widget)


def initialize_gl():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_DEPTH_TEST)


def paint_gl(model, gl_widget):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_SCISSOR_TEST)
    glEnable(GL_ALPHA_TEST)
    glEnable(GL_BLEND)

    glBlendFunc(str_to_fact(model.s_factor), str_to_fact(model.d_factor))
    glAlphaFunc(str_func_to_gl_const(model.func), model.ref / 100)

    _, _, w, h = gl_widget.geometry().getRect()

    glScissor(int(model.clipping_x * w / 100),
              int(model.clipping_y * h / 100),
              int(w * model.clipping_width / 100),
              int(h * model.clipping_height / 100)
              )

    draw_primitive(model)

    glDisable(GL_BLEND)
    glDisable(GL_ALPHA_TEST)
    glDisable(GL_SCISSOR_TEST)


def resize_gl(gl_widget):
    glViewport(*gl_widget.geometry().getRect())
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 200, 0, 100, 0, 200)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw_primitive(model):
    if model.primitive == 'GL_POINTS':
        points()
    elif model.primitive == 'GL_LINES':
        lines()
    elif model.primitive == 'GL_LINE_STRIP':
        line_strip()
    elif model.primitive == 'GL_LINE_LOOP':
        line_loop()
    elif model.primitive == 'GL_TRIANGLES':
        triangles()
    elif model.primitive == 'GL_TRIANGLE_STRIP':
        triangle_strip()
    elif model.primitive == 'GL_TRIANGLE_FAN':
        triangle_fan()
    elif model.primitive == 'GL_QUADS':
        quads()
    elif model.primitive == 'GL_QUAD_STRIP':
        quad_strip()
    elif model.primitive == 'GL_POLYGON':
        polygon()


def points():
    glPointSize(6)
    glBegin(GL_POINTS)
    glColor4f(0.2, 0.0, 0.58, 0.2)
    glVertex2f(50, 50)
    glColor4f(1.0, 0.0, 0.6, 0.4)
    glVertex2f( 100, 45)
    glColor4f(0.0, 1.0, 0.0, 0.6)
    glVertex2f(150, 90)
    glColor4f(0.0, 0.0, 0.0, 0.8)
    glVertex2f( 190, 65)
    glColor4f(1.0, 0.0, 0.0, 1.0)
    glVertex2f(30, 80)
    glEnd()


def lines():
    glLineWidth(4)
    glBegin(GL_LINES)

    glColor4f(1.0, 0.0, 0.6, 0.2)
    glVertex2f(100, 45)
    glColor4f(0.0, 1.0, 0.0, 0.4)
    glVertex2f(150, 90)

    glColor4f(0.0, 0.0, 0.0, 0.6)
    glVertex2f(190, 65)
    glColor4f(1.0, 0.0, 0.0, 0.8)
    glVertex2f(30, 80)

    glColor4f(0.0, 0.0, 0.0, 1.0)
    glVertex2f(10, 10)
    glVertex2f(150, 50)
    glEnd()


def line_strip():
    glLineWidth(4)
    glBegin(GL_LINE_STRIP)
    glColor4f(1.0, 0.0, 0.6, 1.0)
    glVertex2f( 100, 45)
    glColor4f(0.0, 1.0, 0.0, 0.8)
    glVertex2f(150, 90)

    glColor4f(0.0, 0.0, 0.0, 0.6)
    glVertex2f( 190, 65)
    glColor4f(1.0, 0.0, 0.0, 0.4)
    glVertex2f(30, 80)

    glColor4f(0.0, 0.0, 0.0, 0.2)
    glVertex2f(10, 10)
    glVertex2f( 150, 50)
    glEnd()


def line_loop():
    glLineWidth(4)
    glBegin(GL_LINE_LOOP)

    glColor4f(1.0, 0.0, 0.6, 1.0)
    glVertex2f( 100, 45)
    glColor4f(0.0, 1.0, 0.0, 0.8)
    glVertex2f(150, 90)
    glColor4f(0.0, 0.0, 0.0, 0.6)
    glVertex2f( 190, 65)
    glColor4f(1.0, 0.0, 0.0, 0.4)
    glVertex2f(30, 80)
    glColor4f(0.0, 0.0, 0.0, 0.2)
    glVertex2f(10, 10)
    glColor4f(1.0, 1.0, 0.0, 0.1)
    glVertex2f( 150, 50)
    glEnd()


def triangles():
    glBegin(GL_TRIANGLES)

    glColor4f(1.0, 0.0, 0.6, 1.0)
    glVertex2f( 100, 45)
    glColor4f(0.0, 1.0, 0.0, 0.8)
    glVertex2f(150, 90)
    glColor4f(0.0, 0.0, 0.0, 0.6)
    glVertex2f( 190, 65)

    glColor4f(1.0, 0.0, 0.0, 0.4)
    glVertex2f(30, 80)
    glColor4f(0.0, 0.0, 0.0, 0.2)
    glVertex2f(10, 10)
    glColor4f(1.0, 1.0, 0.0, 0.1)
    glVertex2f( 150, 50)

    glEnd()


def triangle_strip():
    glBegin(GL_TRIANGLE_STRIP)

    glColor4f(1.0, 0.0, 0.6, 1.0)
    glVertex2f( 100, 45)
    glColor4f(0.0, 1.0, 0.0, 0.8)
    glVertex2f(150, 90)
    glVertex2f( 190, 65)

    glColor4f(1.0, 0.0, 0.0, 0.4)
    glVertex2f(30, 80)
    glColor4f(1.0, 1.0, 0.0, 0.1)

    glEnd()


def triangle_fan():
    glBegin(GL_TRIANGLE_FAN)

    glColor4f(1.0, 0.0, 0.6, 0.4)
    glVertex2f( 100, 45)
    glVertex2f(50, 50)

    glColor4f(0.0, 1.0, 0.0, 0.6)
    glVertex2f(150, 90)
    glVertex2f( 190, 65)

    glEnd()


def quads():
    glBegin(GL_QUADS)

    glColor4f(1.0, 0.0, 0.6, 0.1)
    glVertex2f( 10, 10)
    glVertex2f(10, 20)
    glVertex2f( 20, 20)
    glVertex2f(20, 10)

    glColor4f(0.0, 0.0, 0.0, 0.1)
    glVertex2f( 100, 45)
    glVertex2f(50, 50)
    glVertex2f(70, 60)
    glVertex2f( 110, 60)

    glColor4f(0.2, 0.0, 0.58, 0.1)
    glVertex2f(90, 70)
    glVertex2f(150, 90)
    glVertex2f( 190, 65)
    glVertex2f( 100, 45)

    glEnd()


def quad_strip():
    glBegin(GL_QUAD_STRIP)

    glColor4f(0.0, 0.0, 0.0, 0.1)
    glVertex2f( 30, 10)
    glColor4f(1.0, 0.0, 0.6, 0.9)
    glVertex2f(10, 40)
    glVertex2f( 30, 70)
    glVertex2f(60, 70)

    glColor4f(0.0, 0.0, 0.0, 0.1)
    glVertex2f(80, 40)
    glVertex2f(60, 10)

    glEnd()


def polygon():
    glBegin(GL_POLYGON)

    glColor4f(1.0, 0.0, 0.6, 0.9)
    glVertex2f( 30, 10)
    glVertex2f(10, 40)
    glVertex2f( 30, 70)
    glVertex2f(60, 70)

    glColor4f(0.0, 0.0, 0.0, 0.1)
    glVertex2f(80, 40)
    glVertex2f(60, 10)

    glEnd()
