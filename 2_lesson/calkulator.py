a = int(input("Enter a: "))
b = int(input("Enter b: "))
operation =input("/ * - +: ")
rezult = None
if (b==0 and operation== '/'):
    print("b= 0 and op=/ -----not good")
else:
    if (operation == '/'):
        rezult = a / b
        print(rezult)
    elif (operation == '*'):
        rezult = a * b
        print(rezult)
    elif (operation == '-'):
        rezult = a - b
        print(rezult)
    elif (operation == '+'):
        rezult = a + b
        print(rezult)
    else:
        print("operation not good")

