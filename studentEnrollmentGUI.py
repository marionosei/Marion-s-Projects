#PERCENT OF GRAD AND UNDERGRAD GUI APPLICATION

from graphics import *

win = GraphWin("Student Enrollment GUI Application", 450, 400)
win.setCoords(0.0, 0.0, 4.0, 4.0)

#Draw the interface

Text(Point(1,3.5), "Number of undergrad students: ").draw(win)
Text(Point(1,3), "Number of grad students: ").draw(win)
Text(Point(1,1), "Percentage of undergrad students: ").draw(win)
Text(Point(1,0.5), "Percentage of grad students: ").draw(win)
inputUndergrad = Entry(Point(2.8,3.5), 5)
inputUndergrad.setText("")
inputUndergrad.draw(win)
inputGrad = Entry(Point(2.8,3), 5)
inputGrad.setText("")
inputGrad.draw(win)
outputUndergrad = Text(Point(2.8,1),"")
outputUndergrad.draw(win)
outputGrad = Text(Point(2.8,0.5),"")
outputGrad.draw(win)
button = Text(Point(2,2.0),"Convert It")
button.draw(win)
Rectangle(Point(1.5,1.5), Point(2.5,2.5)).draw(win)

#wait for a mouse click
win.getMouse()

#convert input
totalStudents = int(inputUndergrad.getText()) + int(inputGrad.getText())
undergraduatePercentage = float((int(inputUndergrad.getText()) / (int(totalStudents))) * 100)
gradPercentage = float((int(inputGrad.getText()) / (int(totalStudents))) * 100)

#display output and change button
outputUndergrad.setText(round(undergraduatePercentage,0))
outputGrad.setText(round(gradPercentage,0))
button.setText("Quit")

#wait for click and then quit
win.getMouse()
win.close()
