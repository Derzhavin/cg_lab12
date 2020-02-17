from dataclasses import dataclass


@dataclass
class Model:
    primitive: str
    func: str
    ref: int
    s_factor: str
    d_factor: str
    clipping_x: int
    clipping_y: int
    clipping_width: int
    clipping_height: int