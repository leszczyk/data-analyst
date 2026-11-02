# Zadanie 1: podstawy
# Utwórz listę [4, 8, 15, 16, 23, 42]. Wypisz: pierwszy i ostatni element, trzy pierwsze elementy, trzy ostatnie, 
# długość listy oraz sumę, minimum i maksimum (wbudowane sum, min, max).

# lista = [4, 8, 15, 16, 23, 42]

# print(lista[0])
# print(f'{lista[len(lista)-1]}')
# print(lista[:3])
# print(lista[-3:])
# print(f'Długość listy: {str(len(lista))}')

# suma = sum(lista)
# print(f'Suma = {suma}')
# minimum = min(lista)
# print(f'Min = {minimum}')
# maksimum = max(lista)
# print(f'Max = {maksimum}')

# Zadanie 2: średnia z listy
# Funkcja srednia_listy(lista) zwraca średnią elementów. Co zrobi dla pustej listy? 
# Obsłuż ten przypadek (np. zwróć None). To poprawka do zadania 3 z sesji 3, które dzieliło zawsze przez 3.

# def srednia_listy(lista):
#     if len(lista) == 0:
#         return None
#     else:
#         return sum(lista) / len(lista)
# lista = []
# while True:
#     print(f'Podaj cyfrę (kliknij Enter, aby zakończyć): ')
#     liczba = input()
#     if liczba == '':
#         break
#     lista.append(float(liczba))
# print(f'To twoja lista {lista}')
# print(f'Średnia z listy = {srednia_listy(lista)}')

# Zadanie 3: maksimum bez max()
# Funkcja znajdz_max(lista) znajduje największy element pętlą. Przetestuj na liście z liczbami ujemnymi, np. [-5, -2, -9].
# Podpowiedź: zacznij od pierwszego elementu listy, a nie od 0. Pamiętasz z zadania 5 w sesji 2, dlaczego.

# def znajdz_max(lista):
#         if len(lista) == 0:
#             return None
#         temp = lista[0]
#         for n in range(1,len(lista)):
#             if lista[n] > temp:
#                 temp = lista[n]
#         return temp
# lista = []
# while True:
#     print(f'Podaj cyfrę (kliknij Enter, aby zakończyć): ')
#     liczba = input()
#     if liczba == '':
#         break
#     lista.append(float(liczba))
# print(f'To twoja lista {lista}')
# print(f'Max z listy = {znajdz_max(lista)}')

# Zadanie 4: filtrowanie
# a) Funkcja parzyste(lista) zwraca nową listę z samymi parzystymi liczbami.
# b) Użyj czy_pierwsza z sesji 3, żeby zbudować listę liczb pierwszych od 1 do 50 (zamiast ich wypisywania) i wypisać ją razem z 
# liczbą elementów.
# Podpowiedź: pusta lista na początku i append w pętli.

# def parzyste(lista):
#     lista_parzysta = []
#     for n in range(len(lista)):
#         if lista[n] % 2 == 0:
#             lista_parzysta.append(lista[n])
#     return lista_parzysta

# print(f'Lista liczb parzystych = {parzyste([1,2,3,4,5,6])}')

# def czy_pierwsza(n):
#     if n < 2:
#         return False
#     for dzielnik in range(2, n):
#         if n % dzielnik == 0:
#             return False
#     return True

# print('Program sprawdzający czy liczba jest liczbą pierwszą:')
# pierwsze = []
# for n in range(1,51):
#     if czy_pierwsza(n):
#         pierwsze.append(n)
# print(pierwsze)
# print(len(pierwsze))


# Zadanie 5: lista zakupów
# Program wczytuje produkty w pętli, aż użytkownik wpisze koniec, i zapisuje je do listy. Potem:
# wypisuje listę posortowaną alfabetycznie i liczbę produktów,
# pyta o nazwę produktu do usunięcia i go usuwa (remove). Co się stanie, jeśli produktu nie ma na liście? Sprawdź warunkiem in, zanim go usuniesz.
# produkty = []
# while True:
#     produkt = input('Wpisz produkt lub "koniec", jeżeli chcesz zakończyć: ').strip()
#     if produkt == 'koniec':
#         break
#     produkty.append(produkt)
# produkty.sort(key=str.lower)
# print(f'To twoja lista posortowana alfabetyzcnie o długości {len(produkty)}: {produkty}')
# usun = input('Jaki produkt usunąć: ')
# if usun not in produkty: 
#     print('Nie ma takiego produktu')
# else:
#     produkty.remove(usun)
# print(f'To twoja lista: {produkty}')


# Zadanie 6 (bonus): usuwanie duplikatów
# Funkcja bez_duplikatow(lista) zwraca nową listę bez powtórzeń, zachowując kolejność pierwszych wystąpień. 
# Przetestuj na [3, 1, 3, 2, 1, 5] (oczekiwany wynik [3, 1, 2, 5]).

# def bez_duplikatow(lista):
#     lista_bez = []
#     for x in lista:
#         if x not in lista_bez:
#             lista_bez.append(x)
#     return lista_bez

# print(bez_duplikatow([3, 1, 3, 2, 1, 5]))