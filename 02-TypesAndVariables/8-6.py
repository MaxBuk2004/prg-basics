dziesietna = int(input('Podaj liczbe dziesietna: '))
dwojkowo = bin(dziesietna) 
szesnastowo = hex(dziesietna)
print(f'Liczba dziesietna {dziesietna} to {dwojkowo} w systemie dwojkowym i {szesnastowo} w systemie szesnastkowym')