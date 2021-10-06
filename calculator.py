'''
This is the calculator app, which performs math calculation 
Author : Jacek Jarosz (based on Udemy course)
Copyrights : Sep 2021

'''
import re

print('The calculator')
print("To quit type 'quit'")

previous = 0
run = True

def perform_Math(): ## function definition
    global run
    global previous
    equation = ""
    
    if previous == 0:   ## executed only once on the begining
        equation = input("Enter equation ")
    else:
        equation = input(str(previous))

    if equation == 'quit':  ## program ends condition
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '',equation)
        if previous == 0:
            previous = eval(equation)  ## result of the first calculation
        else:
            previous = eval(str(previous)+equation)  ## taking into account the result of previous calculation
        



## loop with function execution
while run:
    perform_Math()

