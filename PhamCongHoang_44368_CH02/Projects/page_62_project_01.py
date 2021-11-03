"""
Author: Pham Cong Hoang
Date: 04/09/2021
Problem:

Solution:

    ....
"""
# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 8000.0
DEPENDENT_DEDUCTION = 2000.0
# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))
# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
 DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE
# Display the income tax
print("The income tax is $" + str(incomeTax))