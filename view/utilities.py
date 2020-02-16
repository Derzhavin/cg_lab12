from OpenGL.GL import *


def str_func_to_gl_const(string):
    if string == 'GL_NEVER': return GL_NEVER
    if string == 'GL_EQUAL': return GL_EQUAL
    if string == 'GL_LEQUAL': return GL_LEQUAL
    if string == 'GL_GREATER': return GL_GREATER
    if string == 'GL_NOTEQUAL': return GL_NOTEQUAL
    if string == 'GL_GEQUAL': return GL_GEQUAL
    if string == 'GL_ALWAYS': return GL_ALWAYS
    if string == 'GL_LESS': return GL_LESS
    
    
def str_to_fact(string):
    if string =='GL_ZERO': return GL_ZERO
    if string =='GL_ONE': return GL_ONE
    if string =='GL_DST_COLOR': return GL_DST_COLOR
    if string =='GL_ONE_MINUS_DST_COLOR': return GL_ONE_MINUS_DST_COLOR
    if string =='GL_SRC_ALPHA': return GL_SRC_ALPHA
    if string =='GL_ONE_MINUS_DST_ALPHA': return GL_ONE_MINUS_DST_ALPHA
    if string =='GL_SRC_ALPHA_SATURATE': return GL_SRC_ALPHA_SATURATE
    if string =='GL_SRC_COLOR': return GL_SRC_COLOR
    if string =='GL_ONE_MINUS_SRC_COLOR': return GL_ONE_MINUS_SRC_COLOR
    if string =='GL_ONE_MINUS_SRC_ALPHA': return GL_ONE_MINUS_SRC_ALPHA
    if string =='GL_DST_ALPHA': return GL_DST_ALPHA