# -*- coding: utf-8 -*-
from __future__ import division # Use python 3 division
from Tkinter import *

import Tkinter,tkMessageBox,math


# Meta Data
Name = 'Calculator Project'
Description = 'This project is to create a GUI based calculator using Tkinter'
Repository = 'https://github.com/adammertzenich/PyCalcGUI'
Version = '2.5.0'
Author = 'Adam Mertzenich'

def about():
    tkMessageBox.showinfo("About", "Project Name: " + Name + "\n" + "Author: " + Author + "\n" + "Description: " + Description + "\n" + "Version: " + Version + "\n" + "Repository: " + Repository)

# End Meta Data
####
# Canvas Variables/Settings
####
windowTitle = 'Calculator Project -' + ' v' + Version + ' - By: ' + Author 

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

'''
      ( \
       \ \
       / /                |\\
      / /     .-`````-.   / ^`-.
      \ \    /         \_/  {|} `o
       \ \  /   .---.   \\ _  ,--'
        \ \/   /     \,  \( `^^^
         \   \/\      (\  )
          \   ) \     ) \ \
ooga booga ) /__ \__  ) (\ \___
          (___)))__))(__))(__)))
'''

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
# Note: Consider using a new version of the old workspace variable to concactate strings and convert to floats.

operator = '' # default operator to empty string
operationOne = '0' # first number to be entered and used
operationTwo = '0' # second number to be entered and used
answer = '0' # answer that will be displayed later after math is done
operatorUsed = False # defaulting the operatorUsed to False


# define setting operators for commands
def addition():
    global operator,operatorUsed
    operator = 'add'
    if operatorUsed == True:
        # when operator is used and is used again equals() is executed
        equals()
    else:
        operatorUsed = True
    canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def subtraction():
    global operator,operatorUsed
    operator = 'subtract'
    if operatorUsed == True:
        equals()
    else:
        operatorUsed = True
    canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def division():
    global operator,operatorUsed
    operator = 'divide'
    if operatorUsed == True:
        equals()
    else:
        operatorUsed = True
    canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def multiplication():
    global operator,operatorUsed
    operator = 'multiple'
    if operatorUsed == True:
        equals()
    else:
        operatorUsed = True
    canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))

# define numbers
def zero():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(0))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(0))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def one():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(1))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(1))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def two():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(2))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(2))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def three():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(3))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(3))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def four():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(4))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(4))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def five():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(5))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(5))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def six():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(6))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(6))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def seven():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(7))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(7))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def eight():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(8))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(8))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def nine():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        operationOne = int(str(operationOne) + str(9))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
    if operatorUsed == True:
        operationTwo = int(str(operationTwo) + str(9))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
def decimal():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        print 'work in progress'
    if operatorUsed == True:
        print 'work in progress'
def equals():
    global operationOne,operationTwo,answer,operator

    # check the operator and set the answer to operationOne (operator) operationTwo + change the answerDisplay to show the correct answer
    if operator == 'add':
        answer = float(operationOne) + float(operationTwo)
        canvas.itemconfig(answerDisplay, text=answer)
        operationOne = answer
        operationTwo = '0'
    if operator == 'subtract':
        answer = float(operationOne) - float(operationTwo)
        canvas.itemconfig(answerDisplay, text=answer)
        operationOne = answer
        operationTwo = '0'
    if operator == 'multiple':
        answer = float(operationOne) * float(operationTwo)
        canvas.itemconfig(answerDisplay, text=answer)
        operationOne = answer
        operationTwo = ''
    if operator == 'divide':
        answer = float(operationOne) / float(operationTwo)
        canvas.itemconfig(answerDisplay, text=answer)
        operationOne = answer
        operationTwo = ''

# Sets all used variables to empty strings and configures the answerDisplay to display no answer
def clear():
    global operatorUsed,operationOne,operationTwo,answer,operator
    operator = '' # default operator to empty string
    operationOne = '0'
    operationTwo = '0'
    operatorUsed = '0'
    answer = ''
    canvas.itemconfig(answerDisplay, text='No Answer')
    operatorUsed = False

####
# Create calculator buttons
####
numberZero = Button(root, text='0', command=zero)
numberZero.grid(row=4, column=0)

# '.' button that will be used to perform calculations on decimals.

buttonDecimal = Button(root, text='.', command=decimal)
buttonDecimal.grid(row=4, column=1)

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

buttonAbout = Button(root, text='About', command=about)
buttonAbout.grid(row=0, column=6)

# Create text that will be changed to display the answer
answerDisplay = canvas.create_text(100, 100, text='No Answer')

# Enter event loop
root.mainloop()