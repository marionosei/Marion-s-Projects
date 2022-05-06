# simple graphics programming
from graphics import *
#draw a triangle
def drawTrianglePatch(win, color):
    triangle = Polygon(Point(200,70),Point(70,70),Point(135,10))
    triangle.setFill(color)
    triangle.draw(win)
w = 250
h = 250
win = GraphWin("Marion's Abode", w, h)
color = 'purple'
drawTrianglePatch(win, color)
# draw a square
aRectangle = Rectangle(Point(70,70), Point(200,200))
aRectangle.draw(win)
aRectangle.setFill('peachpuff')
txt = Text(Point(135, 80), "Marion")
txt.draw(win)

# draw a door
aRectangle = Rectangle(Point(160,140), Point(195,195))
aRectangle.draw(win)
aRectangle.setFill('brown')
# draw a circle
center = Point(190, 170)
purpleCircle = Circle(center, 4)
purpleCircle.setFill('gold')
purpleCircle.draw(win)
# draw a circle
center = Point(100, 120)
purpleCircle = Circle(center, 20)
purpleCircle.setFill('cyan')
purpleCircle.draw(win)
# draw a line
aLine = Line(Point(80,120), Point(120,120))
aLine.draw(win)
# draw a line
aLine = Line(Point(100,100), Point(100,140))
aLine.draw(win)
# pause for click inside window, then exit
win.getMouse()
win.close()
