import math

from solid import *


def body(n: int, outer: float, inner: float, h: int) -> OpenSCADObject:
    points = []
    outer_inc = 360 / n
    inner_inc = outer_inc / 2
    def x(r, a): return r * math.cos(math.radians(a))
    def y(r, a): return r * math.sin(math.radians(a))
    for i in range(n):
        m1 = outer_inc * i
        points.append([
            x(outer, 90 + m1),
            y(outer, 90 + m1)
        ])
        m2 = inner_inc + m1
        points.append([
            x(inner, 90 + m2),
            y(inner, 90 + m2)
        ])
    star = polygon(points)
    star = linear_extrude(height=h)(star)
    return star
