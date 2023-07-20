# Get details of loan
money_owed = float(input("How much money do you owe, in dollars?\n")) #ex 5000
apr = float(input('What is the annual percentalge rate?\n')) #5%
payment = float(input('How much will you pay monthly?\n')) #500
months = int(input('How many months do you want the results for?\n')) # 10

monthly_rate = apr/100/12 #to get decimal/to get month

for i in range(months):
    # calc interest
    interest_paid = money_owed*monthly_rate
    #add in interest
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print('The last paymenet is', money_owed)
        print('You paid out the loan in', i + 1, 'months')
        break
    #make paymenet
    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest', end = ' ')
    print('Now I owe', money_owed)
