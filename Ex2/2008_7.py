First_number = float(input("Enter the first number : "))
MathematicsSign = input("Enter the mathematics sign : ")
Second_number = float(input("Enter the second number : "))
if(MathematicsSign == '+'):
    print("The answer is ", round((First_number + Second_number), 2))
elif(MathematicsSign == '-'):
    print("The answer is ", round((First_number - Second_number),2))
elif (MathematicsSign == '*'):
    print("The answer is ", round((First_number * Second_number),2))
elif (MathematicsSign == '/'):
    print("The answer is ", round((First_number / Second_number),2))
elif(MathematicsSign == '%'):
    print("The answer is ", round((First_number % Second_number),2))

