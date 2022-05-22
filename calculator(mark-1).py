import turtle

#Answers List.
Answ_List = []

#Calculator Screen.
SIZE_X=500
SIZE_Y=500  
turtle.setup(SIZE_X, SIZE_Y)
turtle.tracer(1,0)
t = turtle.Turtle()
tDel = t.clone()
t.hideturtle()
tDel.hideturtle()
t.left(90)

############################################################################################

#Drawing & Defining GUI Buttons.

#btn0
t.penup()
t.goto(-240,-240)
t.pendown()
t.goto(-240,-200)
t.goto(-177.5,-200)
t.goto(-177.5,-240)
t.goto(-240,-240)
t.penup()
t.goto(-220,-245)
t.write("0", font=('Courier', 30, 'bold'))

#btn1
t.penup()
t.goto(-240,-190)
t.pendown()
t.goto(-240,-150)
t.goto(-177.5,-150)
t.goto(-177.5,-190)
t.goto(-240,-190)
t.penup()
t.goto(-220,-195)
t.write("1", font=('Courier', 30, 'bold'))

#btn4
t.penup()
t.goto(-240,-140)
t.pendown()
t.goto(-240,-100)
t.goto(-177.5,-100)
t.goto(-177.5,-140)
t.goto(-240,-140)
t.penup()
t.goto(-220,-145)
t.write("4", font=('Courier', 30, 'bold'))

#btn7
t.penup()
t.goto(-240,-90)
t.pendown()
t.goto(-240,-50)
t.goto(-177.5,-50)
t.goto(-177.5,-90)
t.goto(-240,-90)
t.penup()
t.goto(-220,-95)
t.write("7", font=('Courier', 30, 'bold'))

#btn=
t.penup()
t.goto(-167.5,-240)
t.pendown()
t.goto(-167.5,-200)
t.goto(-105,-200)
t.goto(-105,-240)
t.goto(-167.5,-240)
t.penup()
t.goto(-147.5,-245)
t.write("=", font=('Courier', 30, 'bold'))

#btn2
t.penup()
t.goto(-167.5,-190)
t.pendown()
t.goto(-167.5,-150)
t.goto(-105,-150)
t.goto(-105,-190)
t.goto(-167.5,-190)
t.penup()
t.goto(-147.5,-195)
t.write("2", font=('Courier', 30, 'bold'))

#btn5
t.penup()
t.goto(-167.5,-140)
t.pendown()
t.goto(-167.5,-100)
t.goto(-105,-100)
t.goto(-105,-140)
t.goto(-167.5,-140)
t.penup()
t.goto(-147.5,-145)
t.write("5", font=('Courier', 30, 'bold'))

#btn8
t.penup()
t.goto(-167.5,-90)
t.pendown()
t.goto(-167.5,-50)
t.goto(-105,-50)
t.goto(-105,-90)
t.goto(-167.5,-90)
t.penup()
t.goto(-147.5,-95)
t.write("8", font=('Courier', 30, 'bold'))

#btn+
t.penup()
t.goto(-95,-240)
t.pendown()
t.goto(-95,-200)
t.goto(-32.5,-200)
t.goto(-32.5,-240)
t.goto(-95,-240)
t.penup()
t.goto(-75,-245)
t.write("+", font=('Courier', 30, 'bold'))

#btn3
t.penup()
t.goto(-95,-190)
t.pendown()
t.goto(-95,-150)
t.goto(-32.5,-150)
t.goto(-32.5,-190)
t.goto(-95,-190)
t.penup()
t.goto(-75,-195)
t.write("3", font=('Courier', 30, 'bold'))

#btn6
t.penup()
t.goto(-95,-140)
t.pendown()
t.goto(-95,-100)
t.goto(-32.5,-100)
t.goto(-32.5,-140)
t.goto(-95,-140)
t.penup()
t.goto(-75,-145)
t.write("6", font=('Courier', 30, 'bold'))

#btn9
t.penup()
t.goto(-95,-90)
t.pendown()
t.goto(-95,-50)
t.goto(-32.5,-50)
t.goto(-32.5,-90)
t.goto(-95,-90)
t.penup()
t.goto(-75,-95)
t.write("9", font=('Courier', 30, 'bold'))

#btn-
t.penup()
t.goto(-22.5,-240)
t.pendown()
t.goto(-22.5,-200)
t.goto(40,-200)
t.goto(40,-240)
t.goto(-22.5,-240)
t.penup()
t.goto(-0.5,-245)
t.write("-", font=('Courier', 30, 'bold'))

#btn*
t.penup()
t.goto(-22.5,-190)
t.pendown()
t.goto(-22.5,-150)
t.goto(40,-150)
t.goto(40,-190)
t.goto(-22.5,-190)
t.penup()
t.goto(-2.5,-202.5)
t.write("*", font=('Courier', 35, 'bold'))

#btn/
t.penup()
t.goto(-22.5,-140)
t.pendown()
t.goto(-22.5,-100)
t.goto(40,-100)
t.goto(40,-140)
t.goto(-22.5,-140)
t.penup()
t.goto(-0.5,-140)
t.write("/", font=('Courier', 25, 'bold'))

#btn^
t.penup()
t.goto(-22.5,-90)
t.pendown()
t.goto(-22.5,-50)
t.goto(40,-50)
t.goto(40,-90)
t.goto(-22.5,-90)
t.penup()
t.goto(-0.5,-95)
t.write("^", font=('Courier', 30, 'bold'))

############################################################################################

#Calculator Answer Screen.
t.goto(-240,-40)
t.pendown()
t.goto(-240,240)
t.goto(40,240)
t.goto(40,-40)
t.goto(-240,-40)
t.penup()

#Calculator Answer Screen Delete.
def delete():
    tDel.penup()
    tDel.fillcolor("white")
    tDel.begin_fill()
    tDel.goto(-235,-35)
    tDel.goto(-235,235)
    tDel.goto(35,235)
    tDel.goto(35,-35)
    tDel.goto(-235,-35)
    tDel.end_fill()
                

#Calculator History.
t.penup()
t.goto(50,250)
t.pendown()
t.goto(50,-250)
t.penup()
t.goto(90,215)
t.write("History", font=('Courier', 20, 'bold'))
t.goto(250,210)
t.pendown()
t.goto(50,210)
t.penup()
t.goto(60,180)


#Clear Calculator History.
def btnclear():
    t.penup()
    t.goto(240,-230)
    t.pendown()
    t.goto(180,-230)
    t.goto(180,-210)
    t.goto(240,-210)
    t.goto(240,-230)
    t.penup()
    t.goto(185,-230)
    t.write("Clear", font=("Courier", 12, 'bold'))
    t.goto(60,180)

def clear(x,y):
    if x > 180 and x < 240 and y > -230 and y < -210:
        t.fillcolor("white")
        t.begin_fill()
        t.goto(55,210)
        t.goto(250,210)
        t.goto(250,-250)
        t.goto(55,-250)
        t.goto(55,210)
        t.end_fill()
        t.goto(50,210)
        t.pendown()
        t.goto(250,210)
        t.penup()
        btnclear()
        print("\nCleared History! Press Enter To Continue")


turtle.onscreenclick(clear, 1)
turtle.listen
btnclear()        

#Defining The Calculator Operations And Their Functions.
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def power(x,y):
    return x ** y



#Welcome & Instructions Text.
print("HULK's Calculator!\nThe Operations That Are Available Are:")
print("1.Addition(+)\n2.Subtraction(-)\n3.Multiplication(*)\n4.Division(/)\n5.Exponent(^)")
input("\nPress Enter to Start")



#Defining The Calculation Function, Asking For The User's Input & Error Handling.
def calculate():
    try:
        delete()
        x = float(input("\nEnter Your First Number: "))
        tDel.penup()
        tDel.goto(-200,200)
        tDel.write(x, font=('Courier', 13, 'bold'))
        y = float(input("Enter Your Second Number: "))
        tDel.goto(-200,150)
        tDel.write(y, font=('Courier', 13, 'bold'))

        
    except ValueError:
        print("ERROR 'Integers Only'")
        calculate()
    else:
        try:            
            operation = input("Enter Your Operation Of Choice: ")
            tDel.goto(-200,175)
            tDel.write(operation, font=('Courier', 13, 'bold'))
            if operation in ('+', '-', '*', '/', '^'):

                if operation == '+':
                    Answ1 = add(x, y)
                    print("Answer:", x, "+", y, "=", Answ1)
                    tDel.goto(-200,125)
                    tDel.write("=", font=('Courier', 13, 'bold'))
                    tDel.goto(-200,100)
                    tDel.write(Answ1, font=('Courier', 13, 'bold'))
                    Answ_List.append(Answ1)
                    hlp()

                elif operation == '-':
                    Answ2 = subtract(x, y)
                    print("Answer:", x, "-", y, "=", Answ2)
                    tDel.goto(-200,125)
                    tDel.write("=", font=('Courier', 13, 'bold'))
                    tDel.goto(-200,100)
                    tDel.write(Answ2, font=('Courier', 13, 'bold'))
                    Answ_List.append(Answ2)
                    hlp()

                elif operation == '*':
                    Answ3 = multiply(x, y)
                    print("Answer:", x, "*", y, "=", Answ3)
                    tDel.goto(-200,125)
                    tDel.write("=", font=('Courier', 13, 'bold'))
                    tDel.goto(-200,100)
                    tDel.write(Answ3, font=('Courier', 13, 'bold'))
                    Answ_List.append(Answ3)
                    hlp()

                elif operation == '/':
                    Answ4 = divide(x, y)
                    print("Answer:", x, "/", y, "=", Answ4)
                    tDel.goto(-200,125)
                    tDel.write("=", font=('Courier', 13, 'bold'))
                    tDel.goto(-200,100)
                    tDel.write(Answ4, font=('Courier', 13, 'bold'))
                    Answ_List.append(Answ4)
                    hlp()

                elif operation == '^':
                    Answ5 = power(x, y)
                    print("Answer:", x, "^", y, "=", Answ5)
                    tDel.goto(-200,125)
                    tDel.write("=", font=('Courier', 13, 'bold'))
                    tDel.goto(-200,100)
                    tDel.write(Answ5, font=('Courier', 13, 'bold'))
                    Answ_List.append(Answ5)
                    hlp()

            else:
                print("ERROR 'Invalid Operation'")
                calculate()
        except ZeroDivisionError:
            print("ERROR 'Can Not Divide By Zero'")
            calculate()
        except OverflowError:
            print("ERROR 'The Number Is Too Big For The Computer To Handle'")
            calculate()
        else:
            rerun()


#Asking If The User Wants To Continue Or Stop Using The Calculator.    
def rerun():

    run_again = input("\nWould you like to calculate again?\nPlease Type Y for Yes or N for No: ")
      
    if run_again.upper() == "Y":
        calculate()

    elif run_again.upper() == "N":
        print("Good Luck!")
        quit()

    else:
        rerun()

#History List Print.
def hlp():
    for i in range(len(Answ_List)):
        ##print(Answ_List[i])
        t.write(Answ_List[i], font=('Courier', 20, 'bold'))
        Answ_List.clear()
        t.backward(25)
    
calculate()
t.mainloop()