import pyglet
import math

window = pyglet.window.Window()
width, height = window.size

@window.event
def draw_fractal(x, y, length, const_angle, angle=0):
    if length <= 1:
        return
    prev_x = x
    prev_y = y
    length = length/2

    x = math.sin(angle) * length
    y = math.cos(angle) * length

    line = pyglet.shapes.Line(prev_x, prev_y, prev_x + x, prev_y + y, width=1, color=(255, 255, 255, 255))

    line.draw()

    draw_fractal(prev_x + x, prev_y + y, length, const_angle, angle + const_angle)
    draw_fractal(prev_x + x, prev_y + y, length, const_angle, angle - const_angle)

angle = int(input("Type angle in deg: "))
angle = math.pi/(180/angle)
@window.event
def on_draw():
    window.clear()
    draw_fractal(width/2, 0, 400, angle, 0)

pyglet.app.run()