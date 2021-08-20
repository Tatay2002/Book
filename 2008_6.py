TAX_RATE = 7/100
STANDARD_DEDUCTION = 500
DEPENDENT_DEDUCTION = 300

GrossIncome= float(input("Enter the gross income : "))
NumDependents = int(input("Enter the number of dependents : "))

taxableIncome = GrossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * NumDependents
incomeTax = taxableIncome * TAX_RATE

print("The income tax is $" + str(round(incomeTax, 2)))