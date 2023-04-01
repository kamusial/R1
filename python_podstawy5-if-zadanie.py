#program pyta o zarobki:
#Jeśli zarabiamy więcej, niż 8000zł - podatek 60%
#Jeśli zarabiasz więcej niż 4000zł, ale do 8000zl - 15%
#w przeciwnym wypadku brak podatku

zarobki = int(input('Ile zarabiasz '))

#wersja 1
if (zarobki > 4000 and zarobki < 8000):
    print('Zarobisz',zarobki*0.85)
elif (zarobki > 8000):
    print('Zarobisz',zarobki*0.4)
else:
    print('Zarobisz',zarobki,'bo nie ma podatku')

#wersja 2
if (zarobki > 8000):
    print('Zarobisz',zarobki*0.4)
elif (zarobki > 4000):
    print('Zarobisz',zarobki*0.85)
else:
    print('Zarobisz',zarobki,'bo nie ma podatku')
