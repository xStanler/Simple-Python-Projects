import pyglet

win = pyglet.window.Window()
width, height = win.size
win.set_caption("Math Graphs")

@win.event
def draw_graph():
    points = []
    y = 0
    x_start = width // 2
    x = 0

    while height >= y+(height//2) >= 0 and width >= x+(width//2) >= 0:
        y = (x/12)**3
        # y = -1*x
        points.insert(0, (x+(width//2), y+(height//2)))
        print(x, y)
        x += 5

    x = 0
    y = 0

    while height >= y+(height//2) >= 0 and width >= x+(width//2) >= 0:
        y = (x/12)**3
        print(x, y)
        # y = -1*x
        points.insert(0, (x+(width//2), y+(height//2)))

        x -= 5

    for i in range(1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[i-1]
        if i == len(points)//2:
            continue
        line = pyglet.shapes.Line(x1, y1, x2, y2, 3, (92, 214, 92))
        line.draw()


@win.event
def draw_cartesian():
    oX = pyglet.shapes.Line(width//2, 0, width//2, height, 2, (255, 255, 255))
    oY = pyglet.shapes.Line(0, height//2, width, height//2, 2, (255, 255, 255))

    for i in range(0, height, height//6):
        line = pyglet.shapes.Line(0, i, width, i, 1, (255, 255, 255, 100))
        line.draw()

    for i in range(0, width, width//12):
        line = pyglet.shapes.Line(i, 0, i, height, 1, (255, 255, 255, 100))
        line.draw()

    oX.draw()
    oY.draw()

@win.event
def on_draw():
    win.clear()
    draw_cartesian()
    draw_graph()

pyglet.app.run()