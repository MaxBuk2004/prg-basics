###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
#Pobieramy wartosc w stopniach celcjusza
celsius = float(input("Podaj temperature w stopniach celcjusza: "))
#Zamieniamy calcjusze na kelviny
kelvin = celsius + 273.15
#Zamieniamy celcjusze na farenheity
fahrenheit = (celsius * 9/5) + 32
#Wyswietlamy obliczone wyniki
print(f"Ta temperatura w kelvinach to: {kelvin}K")
print(f"Ta temperatura w farenheitach to: {fahrenheit}°F")