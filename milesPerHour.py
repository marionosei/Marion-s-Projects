# This program will calculate the hours it would take to reach a destination

from graphics import *

win = GraphWin('Amount of hours to travel a distance given the MPH', 450, 400)
win.setCoords(0.0, 0.0, 4.0, 4.0)

#draw logo
center = Point(0.5, 0.5)
purpleCircle = Circle(center, 0.25)
purpleCircle.setFill('gold')
purpleCircle.draw(win)

txt = Text(Point(0.5, 0.5), "Mari-lator")
txt.draw(win)

#Draw the interface

Text(Point(1,3.5), "Amount of miles: ").draw(win)
Text(Point(1,3.2), "Average speed (MPH): ").draw(win)
Text(Point(1,1), "Amount of time: ").draw(win)
inputMiles = Entry(Point(2.8, 3.5), 5)
inputMiles.setText("")
inputMiles.draw(win)
inputSpeed = Entry(Point(2.8, 3.2), 5)
inputSpeed.setText("")
inputSpeed.draw(win)
outputMiles = Text(Point(2.8,1), "")
outputMiles.draw(win)
button = Text(Point(2.0,2.0),"Calculate")
button.draw(win)
Rectangle(Point(1.5,1.5), Point(2.5,2.5)).draw(win)

#wait for a mouse click
win.getMouse()

#convert input
time = int(inputMiles.getText()) / int(inputSpeed.getText())
if time > 12:
    Text(Point(2.8, 0.5),'Break the trip into more than one day!').draw(win)

#display output and change button
outputMiles.setText(round(time,0)), 'hours'
button.setText("Quit")

#wait for click and then quit
win.getMouse()
win.close()
