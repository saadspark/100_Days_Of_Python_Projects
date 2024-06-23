print('welcome to tip calculator')

total_bill = float(input('what was the total bill? $'))
tip = int(input('how much tip would you like to give? 10, 12, or 15? '))
people = int(input('how many people to split the bill? '))


total_bill_of_each = total_bill+tip/people; 

print(f'each person should pay: ${total_bill_of_each}')