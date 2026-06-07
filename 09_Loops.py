#Lesson_9_Loops 
#learning For loops and While loops
#learning to use break
#Combining Both for loops and while loops

#for loop 1. alternate uppercase for a word challenge.
person1 = 'joshua'
output = ''
count = 0
for letter in person1:
    if count % 2 == 0:
        letter = letter.upper()
        output += letter
        count += 1
    else:
        output += letter
        count+= 1
print(output)

#for loop 2.using for loop with number range and playing with asterisk pattern.
times = ''
asterisk = '*'
count = 0
for x in range(0,11):
    print(times)
    times += asterisk
    count += 1

#While Loop 1. true / false
password = 'Hehe'

while True:
    userInput = input('Password: ')
    if userInput == password:
        print("Access Granted!")
        break
    else:
        print("Password Incorrect! \nTry again.")

#While loop 2. with condition
userPass = 'koko'
passInput = ''
while userPass != passInput:
    passInput = input("Enter Password: ")
    if passInput != userPass:
        print("Incorrect!")
    else:
        print('Access Granted!')

#end
new = ''
length = len(times)
num = length
for x in range(length):
    new = '*' * num
    print(new)
    num -= 1

    







        
    