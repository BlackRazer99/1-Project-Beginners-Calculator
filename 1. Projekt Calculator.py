#Calculator

num1 = float(input("Input the first Number " ))

num2 = float(input("Input the second Number " ))

typeofCalc = input("Which type of Calculation do you want? Add + | - | * | / " )


if typeofCalc == "+" :
    result = float(num1) + float(num2)
    print(result)
elif typeofCalc == "-" :
    result = float(num1) - float(num2)
    print(result)
elif typeofCalc == "*":
    result = float(num1) * float(num2)
    print(result)
elif typeofCalc == "/" :
    result = float(num1) / float(num2)
    print(result)
else: print("Your type of Calculation doesn't Exist")

Continue = input("Press y if you want to continue " )

if Continue == "y" :
    typeofCalc = input("Which type of Calculation do you want? Add + | - | * | / " )
    numx = float(input("Input the Number you want " ))
    if typeofCalc == "+" :
        result = float(result) + float(numx)
        print(result)
    elif typeofCalc == "-" :
        result = float(result) - float(numx)
        print(result)
    elif typeofCalc == "*":
        result = float(result) * float(numx)
        print(result)
    elif typeofCalc == "/" :
        result = float(result) / float(numx)
        print(result)
    else: print("Your type of Calculation doesn't Exist")
else: print("Your result is", result)

input("prompt: ") 
