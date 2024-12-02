###
# Write a program that calculates and displays
# the income of a family per person. To display the results
# in a readable form, use f-strings.
#
father_income = 5450
mother_income = 4920
son_income = 0
family_members = 3
total_income = father_income + mother_income + son_income
income_per_person = round(total_income/family_members)
print(f'Total family income is {total_income}, and income per person is {income_per_person}')