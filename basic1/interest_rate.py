#interest rate checker using if-elif-else
balance =input("what is your bank balance?")
if int(balance) <=0:
    print("Would you like to make a deposit ?")
elif int(balance) <= 50 :
    print("you do not qualify for interset ")
elif int(balance) < 100:
    print("your interest rate is 1%")
else:
    print("your interest rate is 2%")
