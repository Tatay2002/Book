First_number = float(input("Enter the first number : "))
MathematicsSign = input("Enter the mathematics sign : ")
Second_number = float(input("Enter the second number : "))
if(MathematicsSign == '+'):
    print("The answer is ", First_number + Second_number)
elif(MathematicsSign == '-'):
    print("The answer is ", First_number - Second_number)
elif (MathematicsSign == '*'):
    print("The answer is ", First_number * Second_number)
elif (MathematicsSign == '/'):
    print("The answer is ", First_number / Second_number)
elif(MathematicsSign == '%'):
    print("The answer is ", First_number % Second_number)