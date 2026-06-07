#Groups in Python 

#List [], ordered, Allows duplicates, Mutable
fruits = ['orange','apple', 'apple', 'grapes', 'peach']
print(fruits)
fruits.remove('orange')
print(fruits)
fruits[0] = 'watermelon'
print(fruits)
fruits[1] = 'rambutan'
print(fruits)
fruits.clear()
print(fruits)

#Set {}, unordered, NO duplicates, Mutable
person = {'Joshua','Mariel','Mariel','Mark'}
print(person)
person.add('Bon')
print(person)
person.discard('Mark')
print(person)

#Tuples (), ordered, Allows Duplicates, immutable
cities = ('Sagay','Bacolod','Cadiz')
print(cities)

#Dictionary {}, ordered,  Key:Value Pairs
user = {
    'username':'Joshua',
    'career': 'Developer',
    'age':23
    }

print(user)
print(user['username'])
print(f"{user['career']}\n{user['age']}")

