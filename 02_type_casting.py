# Lesson 2: Type Casting in Python 

#I will create a Code using my wallet balance right now
#Lets try

wallet = "1000"
expense = "0"
balance = "0"
print("My wallet balance is: " + wallet)
expense = "40"
expense = int(expense)
print("and i have spend " + str(expense))
balance = int(wallet) - expense
print("so my balance is: " + str(balance))

#note that in the future i will be writing updated refactors of this code, so stay tuned for that!

