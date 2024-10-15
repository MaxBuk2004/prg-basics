name = str(input('Podaj imie: '))
name_lenght = (len(name))-1
last_letter = name[name_lenght]
if last_letter == 'a':
    print(f'{name} is a female name')