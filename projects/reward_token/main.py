#!/usr/bin/env python3

import os
import sys

from solid import *
from solid.utils import *

# add root dir to PYTHONPATH
__script_path = os.path.abspath(__file__)         # nopep8
__project_dir = os.path.dirname(__script_path)    # nopep8
__projects_dir = os.path.dirname(__project_dir)   # nopep8
sys.path.append(os.path.dirname(__projects_dir))  # nopep8
from libs.chamfer import chamfer

import star

if __name__ == '__main__':
    # coin parameters
    coin_size = 25
    coin_thickness = 2
    coin_chamfer = 1
    # star parameters
    star_size = 9
    star_inner_size = star_size / 2.5
    star_thickness = 0.4
    star_points = 5
    # velcro parameters
    velcro_size = 20
    velcro_thickness = 1
    # tolerance
    tolerance = 0.2

    # define bodies
    coin_body = chamfer.chamferCylinder(r=coin_size / 2,
                                        h=coin_thickness,
                                        ch=coin_chamfer,
                                        ch2=0)
    star_body = star.body(n=star_points,
                          outer=star_size,
                          inner=star_inner_size,
                          h=star_thickness)

    star_cut = star.body(n=star_points,
                         outer=star_size + tolerance,
                         inner=star_inner_size + tolerance,
                         h=star_thickness)
    segments = chamfer.circleSegments(r=velcro_size / 2)
    velcro_cut = cylinder(r=velcro_size / 2,
                          h=velcro_thickness,
                          segments=segments)
    velcro_cut = up(coin_thickness - velcro_thickness)(velcro_cut)

    coin_body = difference()(coin_body, star_cut)
    coin_body = difference()(coin_body, velcro_cut)

    obj = coin_body + star_body
    scad_render_to_file(star_body, os.path.join(__project_dir, 'star.scad'))
    scad_render_to_file(coin_body, os.path.join(__project_dir, 'coin.scad'))
