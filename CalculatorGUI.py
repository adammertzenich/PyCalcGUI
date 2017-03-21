# -*- coding: utf-8 -*-
from __future__ import division # Use python 3 division
from Tkinter import *
import Tkinter

import tkMessageBox,math,time


# Meta Data
Name = 'Calculator Project'
Description = 'This project is to create a GUI based calculator using Tkinter'
Repository = 'https://github.com/adammertzenich/PyCalcGUI'
Version = '2.5.2'
Author = 'Adam Mertzenich'
def about(): # about button fires about() which displays the about message box
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
# Variable Handlers (prevent gridRow, gridColumn, and gridRowspan variables from being uncompatable values)
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
canvas = Tkinter.Canvas(root, height=canvasHeight, width=canvasWidth, background=canvasBGColor) # Uses variables defined above to create the canvas
canvas.grid(row=gridRowspan, column=gridColumn, rowspan=gridRowspan)

####
# Begin Calculator
####

operator = '' # default operator to empty string
operationOne = '0' # first number to be entered and used
operationTwo = '0' # second number to be entered and used
answer = '0' # answer that will be displayed later after math is done
operatorUsed = False # defaulting the operatorUsed to False


# Checks what number button is pressed and uses it
def number(num):
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed:
        operationTwo = int(str(operationTwo) + str(num))
        canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
        display.delete(0, Tkinter.END)
        display.insert(Tkinter.END, str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    else:
        operationOne = int(str(operationOne) + str(num))
        canvas.itemconfig(answerDisplay, text=str(operationOne))
        display.delete(0, Tkinter.END)
        display.insert(0, str(operationOne))


# define setting operators for commands
def addition():
    global operator,operatorUsed
    if operatorUsed == True:
        # when operator is used and is used again equals() is executed
        equals()
    else:
        operatorUsed = True
    operator = 'add'
    canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    display.delete(0, Tkinter.END)
    display.insert(Tkinter.END, str(operationOne)+ " " + str(operator) + " " + str(operationTwo))

def subtraction():
    global operator,operatorUsed
    if operatorUsed == True:
        equals()
    else:
        operatorUsed = True
    operator = 'subtract'
    canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    display.delete(0, Tkinter.END)
    display.insert(Tkinter.END, str(operationOne)+ " " + str(operator) + " " + str(operationTwo))

def division():
    global operator,operatorUsed
    if operatorUsed == True:
        equals()
    else:
        operatorUsed = True
    operator = 'divide'
    canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    display.delete(0, Tkinter.END)
    display.insert(Tkinter.END, str(operationOne)+ " " + str(operator) + " " + str(operationTwo))

def multiplication():
    global operator,operatorUsed
    if operatorUsed == True:
        equals()
    else:
        operatorUsed = True
    operator = 'multiple'
    canvas.itemconfig(answerDisplay, text=str(operationOne)+ " " + str(operator) + " " + str(operationTwo))
    display.delete(0, Tkinter.END)
    display.insert(Tkinter.END, str(operationOne)+ " " + str(operator) + " " + str(operationTwo))

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

# Sets all used variables to empty strings or zero and resets the display.
def clear():
    global operatorUsed,operationOne,operationTwo,answer,operator
    operator = '' # default operator to empty string
    operationOne = '0'
    operationTwo = '0'
    operatorUsed = '0'
    answer = ''
    canvas.itemconfig(answerDisplay, text='No Answer')
    display.delete(0, END)
    operatorUsed = False





####
# Create calculator buttons
####

# Decimal button executes decimal() function and will be used to allow decimal calculations
buttonDecimal = Button(root, text='.', command=decimal)
buttonDecimal.grid(row=5, column=1)

# Define buttons 0-9 that execute their respected number() functions
numberZero = Button(root, text='0', command=lambda: number(0))
numberZero.grid(row=5, column=0)

numberOne = Button(root, text='1', command=lambda: number(1))
numberOne.grid(row=4, column=0)

numberTwo = Button(root, text='2', command=lambda: number(2))
numberTwo.grid(row=4, column=1)

numberThree = Button(root, text='3', command=lambda: number(3))
numberThree.grid(row=4, column=2)

numberFour = Button(root, text='4', command=lambda: number(4))
numberFour.grid(row=3, column=0)

numberFive = Button(root, text='5', command=lambda: number(5))
numberFive.grid(row=3, column=1)

numberSix = Button(root, text='6', command=lambda: number(6))
numberSix.grid(row=3, column=2)

numberSeven = Button(root, text='7', command=lambda: number(7))
numberSeven.grid(row=2, column=0)

numberEight = Button(root, text='8', command=lambda: number(8))
numberEight.grid(row=2, column=1)

numberNine = Button(root, text='9', command=lambda: number(9))
numberNine.grid(row=2, column=2)

# Clear Buttom
buttonClear = Button(root, text='Clear', command=clear)
buttonClear.grid(row=1, column=0)

# Divide Button
buttonDivide = Button(root, text='÷', command=division)
buttonDivide.grid(row=1, column=3)

# Multiply Button
buttonMultiply = Button(root, text='x', command=multiplication)
buttonMultiply.grid(row=2, column=3)

# Subtract Button
buttonSubtract = Button(root, text='-', command=subtraction)
buttonSubtract.grid(row=3, column=3)

# Addition Button
buttonAdd = Button(root, text='+', command=addition)
buttonAdd.grid(row=4, column=3)

# Equals Button
buttonEquals = Button(root, text='=', command=equals)
buttonEquals.grid(row=5, column=3)

buttonAbout = Button(root, text='About', command=about)
buttonAbout.grid(row=1, column=6)

# Create text that will be changed to display the answer
answerDisplay = canvas.create_text(100, 100, text='No Answer')

# Answer Display
display = Tkinter.Entry(root, width = 20, bg = "white")
display.grid(row = 0, column = 0, columnspan = 5)


# Enter event loop
root.mainloop()

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