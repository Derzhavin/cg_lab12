from dataclasses import dataclass
from OpenGL.GL import *
import OpenGL

@dataclass
class Model:
    primitive: GLenum
    transparency: GLenum
    sfactor: GLenum
    dfactor: GLenum
    clipping_x: int
    clipping_y: int
    clipping_width: int
    clipping_height: int