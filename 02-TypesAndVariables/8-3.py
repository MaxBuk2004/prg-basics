###
# A program that displays your height both in cm and in feet and inches.
#
# calculate the number of feet
cm = 170
inches = round((cm * 0.3937),3)
feet1 = cm // 30.48
feet2 = (cm%30.48)/30.48
feet1_2 = round((feet1 + feet2),3)
print(f'Moj wzrost w cm to {cm}, w calach to {inches}, a w stopach to {feet1_2}.')