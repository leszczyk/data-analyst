# Zadanie 1: kwadrat(x): zwraca kwadrat liczby. Wywołaj ją dla kilku liczb.

# def kwadrat(x):   
#     return x ** 2
# liczba = float(input('Podaj liczbę: '))
# print(kwadrat(liczba))
# print(kwadrat(3))
# print(kwadrat(2.5))

# Zadanie 2: czy_parzysta(n): zwraca True lub False. Przetestuj dla 0, 7, 10.

# def czy_parzysta(n):
#         return n%2 == 0    
# liczba = int(input('Podaj liczbę: '))
# print(czy_parzysta(liczba))
# print(czy_parzysta(0))
# print(czy_parzysta(7))
# print(czy_parzysta(10))

# Zadanie 3: srednia(a, b, c): zwraca średnią trzech liczb. Potem zmień tak, żeby parametr c miał wartość domyślną 0.

# def srednia(a, b, c=0):
#     return (a + b + c)/3
# liczba1 = float(input('Podaj liczbę: '))
# liczba2 = float(input('Podaj liczbę: '))
# liczba3 = float(input('Podaj liczbę: '))
# print(srednia(liczba1, liczba2, liczba3))
# print(srednia(7,4,8))
# print(srednia(7,4))

# Zadanie 4: kategoria_wiekowa(wiek): Twoje zadanie 1 zamienione na funkcję, która zwraca napis (zamiast go wypisywać). Wynik wypisz poza funkcją.

# def kategoria_wiekowa(wiek):
#     if wiek <= 12:
#         return 'dziecko'
#     elif wiek <= 17:
#         return 'nastolatek'
#     elif wiek <= 64:
#         return 'dorosły'
#     else:
#         return 'senior'

# liczba = int(input('Ile masz lat? '))
# print(f'Jesteś {kategoria_wiekowa(liczba)}.')

# Zadanie 5: czy_pierwsza(n). Przenieś swoje rozwiązanie z zadania 6 z sesji 2 do funkcji. Funkcja ma zwracać True lub False (bez print w środku). Potem w pętli for wypisz wszystkie liczby pierwsze od 1 do 50, wywołując ją dla każdej liczby.

# def czy_pierwsza(n):
#     if n < 2:
#         return False
#     for dzielnik in range(2, n):
#         if n % dzielnik == 0:
#             return False
#     return True

# print('Program sprawdzający czy liczba jest liczbą pierwszą:')
# for x in range(1,51):
#     print(f'{x} {czy_pierwsza(x)}')


# Zadanie 6 (bonus): fizzbuzz(n). Funkcja ma zwracać 'Fizz', 'Buzz', 'FizzBuzz' albo samą liczbę, a pętla poza nią wypisuje wyniki dla 1–50. Masz już gotowe rozwiązanie z sesji 2, więc to głównie przeniesienie print na return.

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 5 == 0:
        return 'Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    else:
        return n
for x in range(1, 51):
    print(fizzbuzz(x))