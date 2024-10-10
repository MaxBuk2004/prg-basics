###
# Calculation of circle area and circumference 
# determine radius and PI values
# calculate area 
# calculate circumference 
# display results
r = float(input('Podaj wartość r:'))
pi = 3.14
area = pi * r**2
circumference = 2 * pi * r
print(f'Dla r={r} pole wynosi: {area}, a obwod: {circumference}')