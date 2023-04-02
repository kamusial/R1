#1. Odczyt pliku

with open('my_file.txt', 'r') as plik1:
    content = plik1.read()   #tu plik jest otwarty
print(type(content))         #tu plik jest zamknięty
content = content.split()
print(content)

print('Liczba slow to:    ',len(content))

# liczba unikalnych słów
content = set(content) #zamieniłem liste na zbior
print('Liczba unikalnych slow ',len(content))

# napis = 'mama tata kot'
# napis2 = napis.split()
# print(napis2)
#
# cos = 'mama.tata.pies.kot'
# cos = cos.split('.')
# print(cos)