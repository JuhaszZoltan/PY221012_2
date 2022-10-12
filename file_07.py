from math import pi

r:int = int(input('a kör sugarának hossza (cm): '))

print(f'kör kerülete: {round(2 * r * pi, 4)} cm')
print(f'kör területe: {round(r ** 2 * pi, 4)} cm^2')