p=float(input("Enter a principle amount in a saving account: "))
t=float(input("Enter a duration of investment in years: "))
r=float(input("Enter rate of interest for SB account: "))
simpleInt=(p*t*r)/100
print("Total Invested amount is: ",p,"\nTotal Interest accumulated: ",simpleInt,"\nTotal Balance: ",p+simpleInt)
print("--------------END OF THE PROGRAM----------------")
