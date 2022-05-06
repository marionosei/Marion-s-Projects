# Random Integer Number Calculator

from graphics import *

win = GraphWin("Random Integer Number Calculator")
win.setCoords(0.0, 0.0, 4.0, 4.0)
win.setBackground("cyan")

#Draw the interface
Text(Point(2,3.5), "Lets Generate a random number!").draw(win)
Text(Point(2,3.1), "Enter a start and end number: ").draw(win)
start = Entry(Point(.75,2.5), 5)
start.setText("0")
start.draw(win)
end = Entry(Point(3.25,2.5), 5)
end.setText("0")
end.draw(win)
genNum = Text(Point(2.8,1),"")
genNum.draw(win)
button = Text(Point(2,2.0),"Generate")
button.draw(win)
center = Point(2, 2)
purpleCircle = Circle(center, 0.75)
purpleCircle.draw(win)

#wait for a mouse click
win.getMouse()


#Variable and error message
startNum = start.getText()
endNum = end.getText()
str = "startNum" and "endNum";
Text(Point(2,0.5), "Close window and try again").draw(win)

#Display output and change button
import random
number = genNum.setText(random.randint(int(startNum), int(endNum)))
genNum.setText(number)
button.setText("Exit")

#wait for click and then quit
win.getMouse()
win.close()
