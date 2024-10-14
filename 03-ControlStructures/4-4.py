###
# Displays the name of university where you are studying
# with an extra space between characters (add a space between
# each character)
#
university = 'Krakow University of Economics'
university_expanded = ''
x = -1

for char in university:
    x += 1
    university_expanded += ' '
    university_expanded += university[x]
    
print(university_expanded)