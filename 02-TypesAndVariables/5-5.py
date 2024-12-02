cena = float(input('Podaj cene produktu: '))
znizka = float(input('Podaj wartosc znizki w %: '))
cena_po_znizce = cena - cena*(znizka/100)
roznica_cen = cena - cena_po_znizce
print(f'cena : {cena}')
print(f'znizka : {znizka}')
print(f'cena po znizce : {round(cena_po_znizce, 2)}')
print(f'roznica cen : {round(roznica_cen, 2)}')