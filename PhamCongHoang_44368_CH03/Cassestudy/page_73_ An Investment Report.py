"""
Author: Pham Cong Hoang
Date: 19/09/2021
Problem:It has been said that compound interest is the eighth wonder of the world. Our next
case study, which computes an investment report, shows why.

Solution:Compute an investment report.
1. The inputs are
 starting investment amount
 number of years
 interest rate (an integer percent)
2. The report is displayed in tabular form with a header.
3. Computations and outputs:
 for each year
 compute the interest and add it to the investment
 print a formatted row of results for that year
4. The ending investment and interest earned are also
 displayed.


    ....
"""
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))
rate = rate / 100
totalInterest = 0.0
print("%4s%18s%10s%16s" % \
 ("Year", "Starting balance",
 "Interest", "Ending balance"))
for year in range(1, years + 1):
 interest = startBalance * rate
 endBalance = startBalance + interest
 print("%4d%18.2f%10.2f%16.2f" % \
 (year, startBalance, interest, endBalance))
 startBalance = endBalance
 totalInterest += interest
 print("Ending balance: $%0.2f" % endBalance)
 print("Total interest earned: $%0.2f" % totalInterest)