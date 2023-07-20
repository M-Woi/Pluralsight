
expenses = [10.50, 8, 5, 15, 20, 5, 3]
"""
sum = 0
for Xexpense in expenses:
    sum = sum + Xexpense
#can be skipped sum"""

total = sum(expenses)

print('you spent $', total, sep = '') #no space before $

#expenses.append(float(input("Enter an expense:/n"))) #x7?

for i in range(7):
    print(i)

total2 = 0
expenses2 = []

num_expenses = int(input("Enter # of expenses:"))
for i2 in range(num_expenses):
    expenses2.append(float(input("Enter an expense:")))
total2 = sum(expenses2)
print("You spent $", total2, sep='')

