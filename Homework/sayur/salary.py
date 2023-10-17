#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5, 23, 21, 14, 23, 12, 4, 12, 22, 22, 34, 12]
base_salary = 10000
bonus_per_5_phones = 5000
bonus_per_phone_after_5 = 1100
additional_bonus = 5000
previousMonthSalary = 0
cumulative_bonus = 0 

for month, phoneCount in enumerate(monthlySalesList):
    if phoneCount >= 5:
        bonus = bonus_per_5_phones + (phoneCount - 5) * bonus_per_phone_after_5
    else:
        bonus = 0
    currentMonthSalary = base_salary + bonus
    if previousMonthSalary > 20000 and phoneCount >= 20:
        currentMonthSalary += additional_bonus
    cumulative_bonus += bonus
    cumulative_bonus += currentMonthSalary - base_salary
    if cumulative_bonus >= 100000:
        base_salary *= 1.05  
        cumulative_bonus = 0 
    print(f"This {month+1}month's salary: {currentMonthSalary}")
    previousMonthSalary = currentMonthSalary