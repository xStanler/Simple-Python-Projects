import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()
window.set_caption("Bezier")
width, height = window.size

pointA = pyglet.shapes.Circle(20, height//2, 6, color=(227, 84, 84))
pointB = pyglet.shapes.Circle(width-20, height//2, 6, color=(227, 84, 84))
pointC = pyglet.shapes.Circle(200, height//2+200, 6, color=(227, 84, 84))
pointD = pyglet.shapes.Circle(width-200, height//2-200, 6, color=(227, 84, 84))

label = pyglet.text.Label('Enter mode (key): \n1. Linear Bezier \n2. Quadratic Bezier \n3. Static Bezier', font_name="Consolas", font_size=14, x=10, y =height - 20, width=200, multiline=True)

@window.event
def on_key_press(symbol, modifiers):
    global mode
    if symbol == ord('1'):
        mode = 1
    elif symbol == ord('2'):
        mode = 2
    elif symbol == ord('3'):
        mode = 3
mode = 1

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


def bezier_linear(A, B, t):
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
    # show_points(points)
    pointA.draw()
    pointB.draw()

def bezier_quadratic(A, B, C, t):
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
def bezier_cubic(A, B, C, D, t):
    xA, yA = A
    xB, yB = B
    xC, yC = C
    xD, yD = D

    points = []

    i = t
    while i < 1:
        x1 = (1-i)*((1-i)*xA + i*xC) + i*((1-i)*xC + i*xB)
        x2 = (1-i)*((1-i)*xC + i*xD) + i*((1-i)*xD + i*xB)

        y1 = (1-i)*((1-i)*yA + i*yC) + i*((1-i)*yC + i*yB)
        y2 = (1-i)*((1-i)*yC + i*yD) + i*((1-i)*yD + i*yB)

        x = ((1-t)*x1) + (t*x2)
        y = ((1-t)*y1) + (t*y2)

        points.insert(0, (x, y))

    show_lines(points, A, B)
    pointA.draw()
    pointB.draw()
    pointC.draw()
    pointD.draw()

t = 0.05

@window.event
def on_draw():
    window.clear()
    label.draw()
    if mode == 1:
        bezier_linear(pointA.position, pointB.position, t)
    elif mode == 2:
        bezier_quadratic(pointA.position, pointB.position, pointC.position, t)
    elif mode == 3:
        bezier_cubic(pointA.position, pointB.position, pointC.position, pointD.position, t)


pyglet.app.run()