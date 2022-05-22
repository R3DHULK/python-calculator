from tkinter import *
import mathanswerVariableGlobal = ""
answerLabelForSquareRoot = ""root = Tk()
root.title('Calculator App')answerEntryLabel = StringVar()
Label(root, font=('futura', 25, 'bold'),
textvariable = answerEntryLabel,
justify = LEFT, height=2, width=7).grid(columnspan=4, ipadx=120)answerFinalLabel = StringVar()
Label(root, font=('futura', 25, 'bold'),
textvariable = answerFinalLabel,
justify = LEFT, height=2, width=7).grid(columnspan = 4 , ipadx=120)
def changeAnswerEntryLabel(entry):
    global answerVariableGlobal
    global answerLabelForSquareRoot
    
    answerVariableGlobal = answerVariableGlobal + str(entry)
    answerLabelForSquareRoot = answerVariableGlobal
    answerEntryLabel.set(answerVariableGlobal)
def clearAnswerEntryLabel():
    global answerVariableGlobal
    global answerLabelForSquareRoot    answerLabelForSquareRoot = answerVariableGlobal
    answerVariableGlobal = ""
    answerEntryLabel.set(answerVariableGlobal)def evaluateSquareRoot():
    global answerVariableGlobal
    global answerLabelForSquareRoot    try:
        sqrtAnswer = math.sqrt(eval(str(answerLabelForSquareRoot)))
        clearAnswerEntryLabel()
        answerFinalLabel.set(sqrtAnswer)
    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        try:
            sqrtAnswer = math.sqrt(eval(str(answerVariableGlobal)))
            clearAnswerEntryLabel()
            answerFinalLabel.set(sqrtAnswer)        except(ValueError,SyntaxError,TypeError,ZeroDivisionError):
            clearAnswerEntryLabel()
            answerFinalLabel.set("Error!")def evaluateAnswer():
    global answerVariableGlobal
    try:
       eval(answerVariableGlobal)
       evaluatedValueAnswerLabelGlobal= str(eval(answerVariableGlobal)    # This line should be alligned                 properly without any indentation error
       clearAnswerEntryLabel()
       answerFinalLabel.set(evaluatedValueAnswerLabelGlobal)

    except(ValueError,SyntaxError,TypeError, ZeroDivisionError):
        clearAnswerEntryLabel()
        answerFinalLabel.set("Error!")
def allClear():
    global answerVariableGlobal
    global answerLabelForSquareRoot    answerVariableGlobal = ""
    answerLabelForSquareRoot = ""
    answerEntryLabel.set("")
    answerFinalLabel.set("")def createButton(txt,x,y):
    Button(root, font=('futura', 15, 'bold'),
           padx=16,pady=16,text = str(txt),
           command = lambda:changeAnswerEntryLabel(txt),
           height = 2, width=9).grid(row = x , column = y, sticky=E)buttons = ['AC','√','%','/','7','8','9','*','4','5','6','-','1','2','3','+','','','.','']buttonsListTraversalCounter = 0for i in range(3,8):
    for j in range(0,4):
        createButton(buttons[buttonsListTraversalCounter],i,j)
        buttonsListTraversalCounter =buttonsListTraversalCounter + 1

Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "√",
       command = lambda:evaluateSquareRoot(),
       height=2, width=9).grid(row = 3 , column = 1, sticky = E)Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "AC",
       command = lambda:allClear(),
       height=2, width=9).grid(row = 3 , column = 0 , sticky = E)
Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "0",
       command = lambda:changeAnswerEntryLabel(0),
       height=2, width=21).grid(row = 7 , column = 0 ,
       columnspan=2 , sticky = E)
Button(root,font=('futura', 15, 'bold'),
       padx=16,pady=16, text = "=",
       command = lambda:evaluateAnswer(),
       height=2, width=9).grid(row = 7 , column = 3, sticky = E)root.mainloop()