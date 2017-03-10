# -*- coding: utf-8 -*-
'''
Name: Calculator Project
Version: 2.4.1
Description: This project is to create a GUI based calculator using Tkinter
Author: Adam Mertzenich

Changelog:
    v0.1:
        + Started Project
        + Added GUI
        + Created buttons/layout
        + Setup variables
    v0.2:
        + Defined operators (add, subtract, multiply, divide)
    v0.3:
        + Defined number imputs 0-9
        - Unused variables
    v0.8:
        + Operators (+, -, /, *) now change boolean operatorUsed to True from False
        + Defined equals that adds the first variable with the second variable
    v0.9:
        + Display answer variable
        + Equals now changes the displayed text
        + Made clear button work
        + Added 0-9 and operator commands to the buttons.
        * Known bug: When trying to add to the answer (ex. 5+5=10) when you add another number it adds to the first (ex. 5+5=10, 10+1=6)
    v1.0:
        + Fixed adding to first number by resetting the first number to the answer
        +- First working calculator version
    v1.5:
        + Bug fixes
    v2.0:
        + Re-organized some things.
        - Removed old workspace concatenation method
        + Alternative to previous workspace using concatenation method by converting previous number in the
          operation(One or Two) into a string and then back to an integer.
        +- Begin work on displaying numbers as you enter them.
    v2.1:
        + Add live input view
    v2.2:
        + Operators now change the view for better real time updatng
        * Known bug: Divide not working correctly. 9/6=1? Nope...
    v2.2.1
        + Fixed division not working by importing division from future.
        * Known bug: When operator changed after operationOne and Two have been chosen the second value become invisible (ex. 5+3, press - button, displays "5 subtract ", press another button (5) and it changes to 5 subtract 35
        * Known bug: Operator changes after one has been selected instead of putting it at the end (only 2 numbers can be operated on at once)
    v2.2.2
        Fix bug with changing operator causing operationTwo to not be visible in the display.
        * Known bug: Operator changes after one has been selected instead of putting it at the end (only 2 numbers can be operated on at once) Going to require changes to the concatenation .
    v2.2.3
        * v2.2.2 bugs not yet fixed
        +- Operators and Operations now default to empty strings.
    v2.2.4
        + Fixed bug where operationTwo was not reset after getting an answer (ex. 1+2=3, 3+1 would do 3+21)
    v2.2.4.2
        + Began work on doing math with unlimited number of operations (2+2+2+2 instead of 2+2=4+2=6+2=8)
    v2.2.5
        + Setup workspace reborn, and got rid of it. Beginning changing how operators work and equals so it can be used.
    v2.3
        + Added multi number calculations (2+2+2+2)
    v2.4
        +- Changelog now in commits to github.
    v2.4.1
        + Added more comments
'''
from __future__ import division
from Tkinter import *
import Tkinter,math,random


####
# Canvas Variables/Settings
####
windowTitle = 'Calculator Project v2.4.1'

# Canvas Properties
canvasHeight = 300
canvasWidth = 300
canvasBGColor = 'white'

# Canvas Grid Settings
gridRow = 10
gridColumn = 10
gridRowspan = 10

####
# Variable Handlers (prevent errors related to what is chosen in the canvas grid settings
####
if gridRowspan <= 0:
    gridRowspan = 1
if gridRow < 0:
    gridRow = 0
if gridColumn < 0:
    gridColumn = 0

####
# Create the main window
####
root = Tkinter.Tk()
root.wm_title(windowTitle)

####
# Create a canvas and place it
####
canvas = Tkinter.Canvas(root, height=canvasHeight, width=canvasWidth, background=canvasBGColor)
canvas.grid(row=gridRowspan, column=gridColumn, rowspan=gridRowspan)

####
# Setup math workspace
####
# workspace = '' # variable will be used when multi digit calculations are added
# RIP Workspace variable March 9th 2k17

operator = '' # default operator to addition
operationOne = '' # first number to be entered and used
operationTwo = '' # second number to be entered and used
answer = '' # answer that will be displayed later after math is done
operatorUsed = False # defaulting the operatorUsed to False


# define setting operators for commands
def addition():
    global operator
    global operatorUsed
    operator = 'add'
    if operatorUsed == True:
        # when operator is used and is used again equals() is executed
        equals()
    else:
        operatorUsed = True
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def subtraction():
    global operator
    global operatorUsed
    operator = 'subtract'
    if operatorUsed == True:
        equals()
    else:
        operatorUsed = True
    canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def division():
    global operator
    global operatorUsed
    operator = 'divide'
    if operatorUsed == True:
        equals()
    else:
        operatorUsed = True
    canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def multiplication():
    global operator
    global operatorUsed
    operator = 'multiple'
    if operatorUsed == True:
        equals()
    else:
        operatorUsed = True
    canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))

# define numbers
def zero():
    global operator
    global operationOne
    global operationTwo
    global operatorUsed
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(0))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(0))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    else:
        return 'you really messed something up! how did operatorUsed get set to a non boolean you fool!'
def one():
    global operator
    global operationOne
    global operationTwo
    global operatorUsed
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(1))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(1))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    else:
        return 'you really messed something up! how did operatorUsed get set to a non boolean you fool!'
def two():
    global operator
    global operationOne
    global operationTwo
    global operatorUsed
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(2))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(2))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    else:
        return 'you really messed something up! how did operatorUsed get set to a non boolean you fool!'
def three():
    global operator
    global operationOne
    global operationTwo
    global operatorUsed
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(3))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(3))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    else:
        return 'you really messed something up! how did operatorUsed get set to a non boolean you fool!'
def four():
    global operator
    global operationOne
    global operationTwo
    global operatorUsed
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(4))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(4))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    else:
        return 'you really messed something up! how did operatorUsed get set to a non boolean you fool!'
def five():
    global operator
    global operationOne
    global operationTwo
    global operatorUsed
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(5))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(5))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    else:
        return 'you really messed something up! how did operatorUsed get set to a non boolean you fool!'
def six():
    global operator
    global operationOne
    global operationTwo
    global operatorUsed
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(6))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(6))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    else:
        return 'you really messed something up! how did operatorUsed get set to a non boolean you fool!'
def seven():
    global operator
    global operationOne
    global operationTwo
    global operatorUsed
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(7))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(7))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    else:
        return 'you really messed something up! how did operatorUsed get set to a non boolean you fool!'
def eight():
    global operator
    global operationOne
    global operationTwo
    global operatorUsed
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(8))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(8))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    else:
        return 'you really messed something up! how did operatorUsed get set to a non boolean you fool!'
def nine():
    global operator
    global operationOne
    global operationTwo
    global operatorUsed
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(9))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(9))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    else:
        return 'you really messed something up! how did operatorUsed get set to a non boolean you fool!'
def equals():
    global operationOne
    global operationTwo
    global answer
    global operator

    # check the operator and set the answer to operationOne (operator) operationTwo + change the answerDisplay to show the correct answer
    if operator == 'add':
        answer = operationOne + operationTwo
        canvas.itemconfig(answerDisplay, text=answer)
    if operator == 'subtract':
        answer = operationOne - operationTwo
        canvas.itemconfig(answerDisplay, text=answer)
    if operator == 'multiple':
        answer = operationOne * operationTwo
        canvas.itemconfig(answerDisplay, text=answer)
    if operator == 'divide':
        answer = operationOne / operationTwo
        canvas.itemconfig(answerDisplay, text=answer)
    operationOne = answer # operationOne is now answer so we can do math to the answer instead of re entering it
    operationTwo = '' # empty string because operationTwo will be re-entered

# Sets all used variables to empty strings and configures the answerDisplay to display no answer
def clear():
    global operator
    global operationOne
    global operationTwo
    global operatorUsed
    global answer
    operator = '' # default operator to empty string
    operationOne = ''
    operationTwo = ''
    operatorUsed = ''
    answer = ''
    canvas.itemconfig(answerDisplay, text='No Answer')
    operatorUsed = False

####
# Create calculator buttons
####
numberZero = Button(root, text='0', command=zero)
numberZero.grid(row=4, column=0)

numberOne = Button(root, text='1', command=one)
numberOne.grid(row=3, column=0)

numberTwo = Button(root, text='2', command=two)
numberTwo.grid(row=3, column=1)

numberThree = Button(root, text='3', command=three)
numberThree.grid(row=3, column=2)

numberFour = Button(root, text='4', command=four)
numberFour.grid(row=2, column=0)

numberFive = Button(root, text='5', command=five)
numberFive.grid(row=2, column=1)

numberSix = Button(root, text='6', command=six)
numberSix.grid(row=2, column=2)

numberSeven = Button(root, text='7', command=seven)
numberSeven.grid(row=1, column=0)

numberEight = Button(root, text='8', command=eight)
numberEight.grid(row=1, column=1)

numberNine = Button(root, text='9', command=nine)
numberNine.grid(row=1, column=2)

# Clear Buttom
buttonClear = Button(root, text='Clear', command=clear)
buttonClear.grid(row=0, column=0)

# Divide Button
buttonDivide = Button(root, text='÷', command=division)
buttonDivide.grid(row=0, column=3)

# Multiply Button
buttonMultiply = Button(root, text='x', command=multiplication)
buttonMultiply.grid(row=1, column=3)

# Subtract Button
buttonSubtract = Button(root, text='-', command=subtraction)
buttonSubtract.grid(row=2, column=3)

# Addition Button
buttonAdd = Button(root, text='+', command=addition)
buttonAdd.grid(row=3, column=3)

# Equals Button
buttonEquals = Button(root, text='=', command=equals)
buttonEquals.grid(row=4, column=3)

# Create text that will be changed to display the answer
answerDisplay = canvas.create_text(100, 100, text='No Answer')

# Enter event loop
root.mainloop()