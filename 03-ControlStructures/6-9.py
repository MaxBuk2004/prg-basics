age = int(input('Podaj wiek psa w latach: '))
age_count = 1
dog_to_human_age = 0
for age_count in range(1, age + 1):
    if age_count == 1 or age_count == 2:
        dog_to_human_age += 10.5
    else:
        dog_to_human_age += 4
print(f'Pies w wieku {age} lat ma {dog_to_human_age} ludzkich lat')

#Enter the dog's age in human years: 15
#The dog's age in dog's years is 73 years.