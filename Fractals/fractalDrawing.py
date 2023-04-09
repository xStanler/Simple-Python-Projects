import pyglet
import math
from pyglet.window import mouse



window = pyglet.window.Window()
window.set_caption("Fractals")
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


slide = pyglet.shapes.Rectangle(x = 10, y = 10, width = width-20, height = 10, color=(50, 50, 50))
knob = pyglet.shapes.Circle(x = 10, y = 15, radius = 7, color = (155, 155, 155))

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & mouse.LEFT:
        if x >= slide.x and x <= slide.x + slide.width and y >= 0 and y <= 2*slide.y + slide.height:
            knob.x = x



@window.event
def on_draw():
    window.clear()
    slide.draw()
    knob.draw()
    angle = round((knob.x-slide.x) / (slide.width), 2) * math.pi
    draw_fractal(width/2, 2*slide.y+slide.height, 400, angle, 0)

pyglet.app.run()