print('Kamil')

list1 = [24, 65.5, 'piesek', 'ala ma kota']

print(           'cala lista to:'        ,list1)
print('pierwszy element to:', list1[0])
print('trzeci element listy to:', list1[2])
print('ostatni element listy to:', list1[-1])  #można liczyć od tyłu
print('przedostatni element listy to:', list1[-2])

print(type(list1))
print(type(list1[1]))
print(type(list1[2]))
list1[2] = 'zmiana nazwy'
print('3ci element listy to teraz:',list1[2])
suma = list1[0] + list1[1]
print('suma dwoch pierwszych elementow to:',suma)