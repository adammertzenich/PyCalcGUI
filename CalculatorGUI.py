# -*- coding: utf-8 -*-
from __future__ import division # Use python 3 division
from Tkinter import *
from random import *
import Tkinter,tkMessageBox,math

# Meta Data
Name = 'Calculator Project'
Description = 'This project is to create a GUI based calculator using Tkinter'
Repository = 'https://github.com/adammertzenich/PyCalcGUI'
Version = '2.2.0' # Major, Minor, Patch
Author = 'Adam Mertzenich'
def about(): # about button fires about() which displays the about message box
    tkMessageBox.showinfo("About", "Project Name: " + Name + "\n" + "Author: " + Author + "\n" + "Description: " + Description + "\n" + "Version: " + Version + "\n" + "Repository: " + Repository)
# End Meta Data

# Begin Settings
titles = ['Calculator Project', '3-- Fork', 'made with h̶a̶t̶e̶ love',
          'git guud', 'now with math', '99% from natural flavours',
          'gluten free', 'dairy free', 'free bugs']

windowTitle = titles[randint(0,len(titles)-1)] # gets random integer between 0 and the length of the titles string

# User Settings
displayColor = 'lightblue'

# Canvas Properties
canvasHeight = 4
canvasWidth = 4
canvasBGColor = 'white'

# Canvas Grid Settings
gridRow = 10
gridColumn = 10
gridRowspan = 10
# End Settings

# Begin Setup
# Prevent row and rowspan from being certain values
if gridRowspan <= 0:
    gridRowspan = 1
if gridRow < 0:
    gridRow = 0
if gridColumn < 0:
    gridColumn = 0

# define root and create the main window
root = Tkinter.Tk()
root.wm_title(windowTitle)

root.resizable(0,0)

# Create and place canvas using settings
canvas = Tkinter.Canvas(root, height=canvasHeight, width=canvasWidth, background=canvasBGColor) # Uses variables defined above to create the canvas
canvas.grid(row=gridRowspan, column=gridColumn, rowspan=gridRowspan)
# End Setup

'''
    Begin Calculator
'''

operator = '' # default operator to empty string
operationOne = '' # first number to be entered and used
operationTwo = '' # second number to be entered and used
answer = '' # answer that will be displayed later after math is done
operatorUsed = False # defaulting the operatorUsed to False
operatorDisplay = '' # Display set to nothing so no operator/other display will be shown
trashcan = ''

# resets values to default when called in the clear() function
def reset():
    global operator,operationOne,operationTwo,answer,operatorUsed,operatorDisplay
    operator = '' # default operator to empty string
    operationOne = '' # first number to be entered and used
    operationTwo = '' # second number to be entered and used
    answer = '' # answer that will be displayed later after math is done
    operatorUsed = False # defaulting the operatorUsed to False
    operatorDisplay = ''

# ran when a button is pressed to modify the operations
def number(num):
    global operationOne,operationTwo,operatorUsed,operator,operatorDisplay
    if operatorUsed:
        operationTwo = int(str(operationTwo) + str(num))
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))
    else:
        operationOne = int(str(operationOne) + str(num))
        display.delete(0, END)
        display.insert(0, str(operationOne))
        
def numSubtract(trashcan):
    global operationOne,operationTwo,operatorUsed,operator,operatorDisplay
    if operationOne == '':
        return
    if operationTwo == '':
        return
    
    if operatorUsed == True:
        operationTwo = int(operationTwo / 10)
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))        
    else:
        operationOne = int(operationOne / 10)
        display.delete(0, END)
        display.insert(0, str(operationOne))  
root.bind('<BackSpace>', numSubtract) # backspace to trigger numSubtract function

# ran when add button is pressed
def addition(trashcan):
    global operator,operatorUsed,operatorDisplay
    if operatorUsed == True:
        # when operator is used and is used again equals() is executed
        operator = 'add'
        operatorDisplay = '+'
        equals(trashcan)
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))
    else:
        operator = 'add'
        operatorDisplay = '+'
        operatorUsed = True
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))

# ran when the subtract button is pressed
def subtraction(trashcan):
    global operator,operatorUsed,operatorDisplay
    if operatorUsed == True:
        operatorDisplay = '-'
        operator = 'subtract'
        equals(trashcan)
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))
    else:
        operatorDisplay = '-'
        operator = 'subtract'
        operatorUsed = True
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))

# ran when the divide button is pressed
def division(trashcan):
    global operator,operatorUsed,operatorDisplay
    if operatorUsed == True:
        operatorDisplay = '/'
        operator = 'divide'
        equals(trashcan)
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))
    else:
        operatorDisplay = '/'
        operator = 'divide'
        operatorUsed = True
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))

# ran when the multiply button is pressed
def multiplication(trashcan):
    global operator,operatorUsed,operatorDisplay
    if operatorUsed == True:
        operatorDisplay = '*'
        operator = 'multiple'
        equals(trashcan)
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))
    else:
        operatorDisplay = '*'
        operator = 'multiple'
        operatorUsed = True
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))

def power(): # ran when using the power button, allows finding exponents (ex. 50^2)
    global operator,operatorUsed,operatorDisplay
    if operatorUsed == True:
        operatorDisplay = '^'
        operator = 'power'
        equals(trashcan)
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))
    else:
        operatorDisplay = '^'
        operator = 'power'
        operatorUsed = True
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo))

def sqrt(): # gets the square root of the answer
    global operator,operatorUsed,operatorDisplay
    operatorDisplay = '√'
    operator = 'sqrt'
    equals(trashcan)
    
def pi(): # gets pi
    global operator,operatorUsed,operatorDisplay
    operatorDisplay = 'π'
    operator = 'pi'
    equals(trashcan)

# ran when the decimal button is pressed, work in progress
def decimal():
    global operationOne,operationTwo,operatorUsed,operator
    if operatorUsed == False:
        print 'work in progress'
    if operatorUsed == True:
        print 'work in progress'

# ran when equals button is pressed, edits the display and resets/modifies needed values
def equals(event):
    global operationOne,operationTwo,answer,operator,operatorDisplay

    if operator == 'add':
        answer = float(operationOne) + float(operationTwo)
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo) + " " + "=" + " " + str(answer))
        operationOne = answer
        operationTwo = ''
    if operator == 'subtract':
        answer = float(operationOne) - float(operationTwo)
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo) + " " + "=" + " " + str(answer))
        operationOne = answer
        operationTwo = ''
    if operator == 'multiple':
        answer = float(operationOne) * float(operationTwo)
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo) + " " + "=" + " " + str(answer))
        operationOne = answer
        operationTwo = ''
    if operator == 'divide':
        answer = float(operationOne) / float(operationTwo)
        display.delete(0, END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo) + " " + "=" + " " + str(answer))
        operationOne = answer
        operationTwo = ''
    if operator == 'power':
        answer = float(operationOne) ** float(operationTwo)
        display.delete(0,END)
        display.insert(END, str(operationOne)+ " " + operatorDisplay + " " + str(operationTwo) + " " + "=" + " " + str(answer))
        operationOne = answer
        operationTwo = ''
    if operator == 'sqrt':
        answer = float(math.sqrt(answer))
        display.delete(0,END)
        display.insert(END, operatorDisplay+ " " + str(operationOne) + " " + str(operationTwo) + " " + "=" + " " + str(answer))
        operationOne = answer
        operationTwo = ''
    if operator == 'pi': # π
        answer = math.pi
        display.delete(0,END)
        display.insert(END, answer)
        operationOne = answer
        operationTwo = ''
    if operationOne == 1337:
        answer = '1337 h4x0r 1nj3c7 (1ien7'
        display.delete(0,END)
        display.insert(END, answer)        

# resets to defaults and clears display, runs reset() function
def clear(trashcan):
    global operatorUsed,operationOne,operationTwo,answer,operator,operatorDisplay
    reset()
    display.delete(0, END)
    operatorUsed = False


####
# Create calculator buttons
####

# Decimal button executes decimal() function and will be used to allow decimal calculations
buttonDecimal = Button(root, text='.', command=decimal)
buttonDecimal.grid(row=5, column=1)

# Define buttons 0-9 that execute their respected number() functions
numberZero = Button(root, text='0', command=lambda: number(0)) # lambda used to allow each button to run a function with a specific number
numberZero.grid(row=5, column=0)
root.bind('0', lambda event: number(num=0))

numberOne = Button(root, text='1', command=lambda: number(1))
numberOne.grid(row=4, column=0)
root.bind('1', lambda event: number(num=1))

numberTwo = Button(root, text='2', command=lambda: number(2))
numberTwo.grid(row=4, column=1)
root.bind('2', lambda event: number(num=2))

numberThree = Button(root, text='3', command=lambda: number(3))
numberThree.grid(row=4, column=2)
root.bind('3', lambda event: number(num=3))

numberFour = Button(root, text='4', command=lambda: number(4))
numberFour.grid(row=3, column=0)
root.bind('4', lambda event: number(num=4))

numberFive = Button(root, text='5', command=lambda: number(5))
numberFive.grid(row=3, column=1)
root.bind('5', lambda event: number(num=5))

numberSix = Button(root, text='6', command=lambda: number(6))
numberSix.grid(row=3, column=2)
root.bind('6', lambda event: number(num=6))

numberSeven = Button(root, text='7', command=lambda: number(7))
numberSeven.grid(row=2, column=0)
root.bind('7', lambda event: number(num=7))

numberEight = Button(root, text='8', command=lambda: number(8))
numberEight.grid(row=2, column=1)
root.bind('8', lambda event: number(num=8))

numberNine = Button(root, text='9', command=lambda: number(9))
numberNine.grid(row=2, column=2)
root.bind('9', lambda event: number(num=9))

# Clear Buttom
buttonClear = Button(root, text='Clear', command=lambda: clear(trashcan))
buttonClear.grid(row=1, column=0)
root.bind('c', clear)

# Subtract Button
buttonSubtract = Button(root, text='-', command=lambda: subtraction(trashcan))
buttonSubtract.grid(row=3, column=3)
root.bind('-', subtraction)

# Addition Button
buttonAdd = Button(root, text='+', command=lambda: addition(trashcan))
buttonAdd.grid(row=4, column=3)
root.bind('+', addition)

# Divide Button
buttonDivide = Button(root, text='÷', command=lambda: division(trashcan))
buttonDivide.grid(row=1, column=3)
root.bind('/', division)

# Multiply Button
buttonMultiply = Button(root, text='x', command=lambda: multiplication(trashcan))
buttonMultiply.grid(row=2, column=3)
root.bind('*', multiplication)

# Power Button
buttonPower = Button(root, text='^', command=power)
buttonPower.grid(row=2, column=4)

# Sqrt Button
buttonSqrt = Button(root, text='√', command=sqrt)
buttonSqrt.grid(row=3, column=4)

# π Button
buttonPi = Button(root, text='π', command=pi)
buttonPi.grid(row=4, column=4)

# Equals Button
buttonEquals = Button(root, text='=', command=lambda: equals(trashcan))
buttonEquals.grid(row=5, column=3)
root.bind('<Return>', equals)
root.bind('=', equals)

buttonAbout = Button(root, text='About', command=about)
buttonAbout.grid(row=1, column=6)

# Create text that will be changed to display the answer (no longer used)
# answerDisplay = canvas.create_text(100, 100, text='No Answer')

# Answer Display
display = Tkinter.Entry(root, width = 18, bg = displayColor, justify = CENTER)
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