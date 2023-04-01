for i in range (10):
    print('Leci petla ',i)
    print('wykonuje operacje')
print('koniec petli')

#wypisz wszystkie liczby parzyste z przedzialu 0-10

#for i in range (od, do, krok):
for i in range (2, 11, 2):
    print(i)
print('\nkoniec petli2')   #\n - enter
for i in range (100, 20, -13):
    print(i)

lista1 = ['marchewka', 'seler', 'wolowina', 'mleko']
print(lista1)
print(lista1[0])
print(lista1[2])
print(len(lista1))
print(len(lista1[2]))

for i in range(len(lista1)):
    if len(lista1[i]) >= 6:
        print(lista1[i],'ma ',len(lista1[i]),'znakow')



