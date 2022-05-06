# convert_gui.py
# program to convert celsius to farenheit using a simple graphical interface

from graphics import *

win = GraphWin("Celsius Converter", 450, 400)
win.setCoords(0.0, 0.0, 4.0, 4.0)

# Draw the interface
Text(Point(1.5,3), "   Celsius Temperature:").draw(win)
Text(Point(1.5,1), "Fahrenheit Temperature:").draw(win)
inputCelcius = Entry(Point(2.8,3), 5)
inputCelcius.setText("0.0")
inputCelcius.draw(win)
outputCelcius = Text(Point(2.8,1),"")
outputCelcius.draw(win)
button = Text(Point(2,2.0),"Convert It")
button.draw(win)
Rectangle(Point(1.5,1.5), Point(2.5,2.5)).draw(win)

# wait for a mouse click
win.getMouse()

# convert input
celsius = float(inputCelcius.getText())
fahrenheit = 9.0/5.0 * celsius + 32

# display output and change button
outputCelcius.setText(round(fahrenheit,2))
button.setText("Quit")

# wait for click and then quit
win.getMouse()
win.close()
