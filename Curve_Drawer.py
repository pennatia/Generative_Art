import math
import cairo
from PIL import Image
import numpy as np
import random

WIDTH, HEIGHT = 500, 500

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1)
pat.add_color_stop_rgba(1, 1 , 1, 1, 1)  # First stop, 50% opacity

ctx.rectangle(0, 0 , 1, 1)  # Rectangle(x0, y0, x1, y1)
ctx.set_source(pat)
ctx.fill()


times = 1
for i in range(times):
    s_x = random.uniform(0,1)
    s_y = random.uniform(0,1)
    ctx.move_to(s_x,s_y)
    ctx.curve_to(random.uniform(0,1), random.uniform(0,1), 0.5, 0.5, random.uniform(0,1), random.uniform(0,1))
    ctx.curve_to(random.uniform(0,1), random.uniform(0,1), 0.5, 0.5, random.uniform(0,1), random.uniform(0,1))
    ctx.curve_to(random.uniform(0,1), random.uniform(0,1), 0.5, 0.5, random.uniform(0,1), random.uniform(0,1))
    ctx.curve_to(random.uniform(0,1), random.uniform(0,1), 0.5, 0.5, random.uniform(0,1), random.uniform(0,1))
    ctx.curve_to(random.uniform(0,1), random.uniform(0,1), 0.5, 0.5, random.uniform(0,1), random.uniform(0,1))
    ctx.curve_to(random.uniform(0,1), random.uniform(0,1), 0.5, 0.5, random.uniform(0,1), random.uniform(0,1))
    ctx.curve_to(random.uniform(0,1), random.uniform(0,1), 0.5, 0.5, random.uniform(0,1), random.uniform(0,1))
    ctx.curve_to(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1), random.uniform(0,1), s_x, s_y)
    #ctx.curve_to(0, 1, 0.9, 1, 1, 0)
    #ctx.close_path()
    ctx.set_source_rgba(0, 0, 0, 1)
    ctx.set_line_width(0.002)
    #ctx.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
    ctx.fill()
    #ctx.stroke()
    

# Arc(cx, cy, radius, start_angle, stop_angle)
##ctx.arc(0.5, 0.5, 0.5, 0, 2*math.pi)
#ctx.line_to(200, 200)  # Line to (x,y)
# Curve(x1, y1, x2, y2, x3, y3)
#ctx.curve_to(60, 50, 80, 50, 100, 30)
#ctx.close_path()


surface.write_to_png("example.png")  # Output to PNG
s = Image.open('example.png')
s.show()