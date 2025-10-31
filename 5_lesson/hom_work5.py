import calcelator
a = int(input("Enter firsr num: "))
operation = input("Enter operation: ")
b = int(input("Entrr second number"))
if (b==0 and operation== '/'):
    print("b= 0 and op=/ -----not good")
else:
    if (operation == '/'):
        calcelator.division(a,b,operation)
    elif (operation == '*'):
        calcelator.multiplication(a,b,operation )

    elif (operation == '-'):
        calcelator.subtraction(a,b,operation )

    elif (operation == '+'):
        calcelator.adding(a,b,operation )

    else:
        print("operation not good")



