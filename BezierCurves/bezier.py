import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()
width, height = window.size

pointA = pyglet.shapes.Circle(20, height//2, 6, color=(227, 84, 84))
pointB = pyglet.shapes.Circle(width-20, height//2, 6, color=(227, 84, 84))
pointC = pyglet.shapes.Circle(200, height//2+200, 6, color=(227, 84, 84))

@window.event
def on_mouse_motion(x, y, dx, dy):
    pointC.x = x
    pointC.y = y

@window.event
def show_lines(points, A, B):
    points.insert(0, B)
    points.append(A)

    point_len = len(points)
    for i in range(1, point_len):
        x1, y1 = points[i]
        x2, y2 = points[i-1]

        line = pyglet.shapes.Line(x1, y1, x2, y2, 4, (50, 50, 50))
        line.draw()

@window.event
def show_points(points):
    for point in points:
        x, y = point
        im = pyglet.shapes.Circle(x, y, 6, color=(255, 255, 255))
        im.draw()


def bezier_linear(A, B):
    t = 0.05
    xA, yA = A
    xB, yB = B

    points = []

    i = t
    while i < 1:
        x = xA + ((xB - xA) * i)
        y = yA + ((yB-yA) * i)
        points.insert(1, (x, y))
        i+=t

    #displaying
    show_lines(points, A, B)
    show_points(points)
    pointA.draw()
    pointB.draw()

def bezier_quadratic(A, B, C):
    t = 0.05

    points = []

    xA, yA = A
    xB, yB = B
    xC, yC = C

    i = t
    while i < 1:
        x = (1-i)*((1-i)*xA + i*xC) + i*((1-i)*xC + i*xB)
        y = (1-i)*((1-i)*yA + i*yC) + i*((1-i)*yC + i*yB)

        points.insert(0, (x, y))

        i+=t

    show_lines(points, A, B)
    # show_points(points)
    pointA.draw()
    pointB.draw()
    pointC.draw()

@window.event
def on_draw():
    window.clear()
    # bezier_linear(pointA.position, pointB.position)
    bezier_quadratic(pointA.position, pointB.position, pointC.position)


pyglet.app.run()