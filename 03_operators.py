# Lesson 3: Operators in Python 

#1. Arithmetic Operators

budget = 1000
notebook_price = 150
pen_price = 20


#Addition
total_cost = notebook_price + pen_price
print("Total Cost:", total_cost)

#Subtraction
left_budget = budget - total_cost
print("Left Budget:", left_budget)

#Multiplication
required_notebooks = 3
required_pens = 2
total_notebook_cost = notebook_price * required_notebooks
total_pen_cost = pen_price * required_pens
print("Total Notebook Cost:", total_notebook_cost)
print("Total Pen Cost:", total_pen_cost)

#Division
split_budget = budget / 2
print("Split Budget:", split_budget)

#2. Assignment Operators (Shortcut to change a value of the variable)
budget += 1500
print("Updated Budget:", budget)

#3. Comparison Operators (Testing True or False)
overAll_cost = total_notebook_cost + total_pen_cost
is_within_budget = overAll_cost <= budget
print("Is the overall cost within the budget? ", is_within_budget)





