# numerikus egész (integer) "egész számok"
a:int = 1994
# numerikus lebegőpontos (floating point number) ""valós szám""
b:float = 3.1415

print(10 + 3)
print(10 - 3)
print(10 * 3)

print(10 / 3)         # 3.33333...  'sima osztás'
print(10 // 3) # DIV  # 3           'egész osztás'
print(10 % 3)  # MOD  # 1           'maradékképzés'

print(2 ** 10)  # POW  # 1024        'hatványozás'
print(16 ** .5) # sqrt(x) = x^(1/2) => OP: 4

# int és float 'típuskompatibilis'
print(10 // 1.5)
print(3 * 3.1415)

# karakteres (string) "karakterlánc"
c:str = 'string'

print('kutya' + "ház") # konkatenáció 'összefűzés' => 'kutyaház'
print(3 * 'cica ') # 'cica cica cica '

# logikai értékek (Boolean) 
d:bool = True # vagy False

print(True and False)  # => F
print(True or False)   # => T
print(not False)       # => T

# compare 'összehasonlító' operátorok:
# numerikus alkalmazás:
print(10 < 3)   # F
print(10 <= 3)  # F
print(10 > 3)   # T
print(10 >= 3)  # T

# általános alkalmazás:
print('kutya' == 'macska')  # F
print(10 == 10)             # T
print(True == False)        # F

print('kutya' != 'macska')  # T
print(10 != 10)             # F
print(True != False)        # T

print(10 < 3 or 'kutya' != 'macska') # T

# "tartalmazza-e?" <érték> in <kollekció> -> <logikai>
print(10 in [3, 5, 6, 89, 2, 32]) # F
print('kutya' in [5, 42, True, True, 'macska', 17, 'kutya', False]) # T