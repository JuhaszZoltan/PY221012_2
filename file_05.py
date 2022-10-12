arfolyam:float = float(input('€ árfolyama: '))
ft:int = int(input('Mennyi HUF-od van? '))

print(f'ez összesen {round(ft / arfolyam, 2)}€-t ér')