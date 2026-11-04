# Zadanie 1: podstawy
# Utwórz słownik z danymi osoby (imie, wiek, miasto). Wypisz każde pole, zmień wiek, dodaj nowy klucz zawod, usuń miasto. 
# Potem pobierz klucz, którego nie ma, dwoma sposobami: slownik['x'] (zobacz błąd) i slownik.get('x', 'brak').
# Podpowiedź: wypisz wszystkie pary pętlą po .items().

# def wypisz(slownik):
#     for klucz, wartosc in slownik.items():
#         print(f'{klucz}: {wartosc}')

# osoba = {'imie': 'Kacper', 'wiek': '25', 'miasto': 'Radom'}
# wypisz(osoba)

# print('-----------')
# osoba['wiek'] = 26
# wypisz(osoba)

# print('-----------')
# osoba['zawod'] = 'bezrobotny'
# wypisz(osoba)

# print('-----------')
# del osoba['miasto']
# wypisz(osoba)
# # print(osoba['nazwisko']) 
# print(osoba.get('nazwisko', 'brak'))

# Zadanie 2: zliczanie
# Funkcja licz_elementy(lista) zwraca słownik z liczbą wystąpień każdego elementu. Dla ['a', 'b', 'a', 'c', 'a', 'b'] wynik to {'a': 3, 'b': 2, 'c': 1}.
# Podpowiedź: pusty słownik, pętla po liście, a licznik zwiększasz przez .get(x, 0) + 1.

# def licz_elementy(lista):
#     licznik = {}
#     for x in lista:
#         licznik[x] = licznik.get(x, 0) + 1
#     return licznik
# lista = ['a', 'b', 'a', 'c', 'a', 'b']
# wynik = licz_elementy(lista)
# print(wynik)

# Zadanie 3: książka telefoniczna
# Słownik nazwisko: numer. Program w pętli pyta: dodać kontakt, wyszukać, usunąć czy zakończyć. Wyszukiwanie ma obsłużyć brak 
# kontaktu (bez błędu).
# Podpowiedź: trzy if / elif po wyborze użytkownika i .get() przy wyszukiwaniu.

# kontakty = {}

# while True:
#     print('Dodać kontakt? -- 1')
#     print('Wyszukać kontakt? -- 2')
#     print('Usunąć kontakt? -- 3')
#     print('Zakończ -- 4')
#     decyzja = int(input('> '))

#     if decyzja == 1:
#         nazwisko = str(input('Podaj nazwisko: '))
#         numer = input('Podaj numer: ')
#         kontakty[nazwisko] = numer
#     elif decyzja == 2:
#         szukane = input('Podaj nazwisko:')
#         wynik = kontakty.get(szukane, 'Brak kontaktu w bazie')
#         print(f'Numer: {wynik}')
#     elif decyzja == 3:
#         usun = input('Podaj nazwisko:')
#         kontakty.pop(usun, None)
#     elif decyzja == 4:
#         break
#     for i in kontakty.items():
#         print(i)

# Zadanie 4: oceny uczniów
# Słownik uczen: lista ocen, np. {'Anna': [5, 4, 3], 'Jan': [3, 3, 4], 'Ewa': [5, 5, 4]}. Wypisz średnią każdego ucznia 
# (użyj swojej srednia_listy) oraz nazwę ucznia z najwyższą średnią.
# Podpowiedź: maksimum szukasz jak w znajdz_max, tylko porównujesz średnie i zapamiętujesz imię.

# def srednia_listy(lista):
#     if len(lista) == 0:
#         return None
#     return sum(lista) / len(lista)

# dziennik = {'Anna': [5, 4, 3], 'Jan': [3, 3, 4], 'Ewa': [5, 5, 4], 'Ola': []}

# najlepszy_uczen = None
# najwyzsza_srednia = None

# for uczen, oceny in dziennik.items():
#     srednia = srednia_listy(oceny)
#     if srednia is None:
#         print(f'{uczen}: brak ocen')
#         continue
#     print(f'{uczen}: {srednia:.2f}')
#     if najwyzsza_srednia is None or srednia > najwyzsza_srednia:
#         najwyzsza_srednia = srednia
#         najlepszy_uczen = uczen

# print(f'Najwyższa średnia: {najlepszy_uczen} ({najwyzsza_srednia:.2f})')
     

# Zadanie 5: lista słowników
# Lista produktów: [{'nazwa': 'mleko', 'cena': 4.5, 'ilosc': 10}, ...] (min. 4 produkty). Oblicz łączną wartość magazynu (cena × ilość), 
# wypisz nazwy produktów droższych niż 5 zł i produkt o największej wartości.
# Podpowiedź: for p in produkty: i dostęp p['cena'].

# produkty = [{'nazwa': 'mleko', 'cena': 4.5, 'ilosc': 10}, 
#             {'nazwa': 'jajka', 'cena': 10, 'ilosc': 20}, 
#             {'nazwa': 'gąbka', 'cena': 1.5, 'ilosc': 140},
#             {'nazwa': 'paluszki', 'cena': 6.5, 'ilosc': 44}]

# laczna_wartosc = 0
# najdrozszy = None
# najwyzsza_wartosc = None

# for p in produkty:
#     wartosc = p['cena'] * p['ilosc']
#     laczna_wartosc = laczna_wartosc + wartosc
#     if p['cena'] > 5:
#         print(f'{p['nazwa']}: {p['cena']} zł')
#     if najwyzsza_wartosc is None or wartosc > najwyzsza_wartosc:
#         najwyzsza_wartosc = wartosc
#         najdrozszy = p['nazwa']

# print(f'Łączna wartość magazynu: {laczna_wartosc:.2f} zł.')
# print(f'Najdroższy produkt to {najdrozszy} ({najwyzsza_wartosc} zł).')

# Zadanie 6 (bonus): grupowanie
# Dana jest lista par [('Łódź', 10), ('Warszawa', 12), ('Łódź', 8), ('Kraków', 9), ('Warszawa', 14)]. 
# Zbuduj słownik miasto: lista temperatur, a potem wypisz średnią temperaturę każdego miasta.
# Podpowiedź: .setdefault(miasto, []) albo sprawdzenie in. To jest dokładnie operacja groupby, którą zobaczysz w Pandas.

# dane = [('Łódź', 10), ('Warszawa', 12), ('Łódź', 8), ('Kraków', 9), ('Warszawa', 14)]

# dane_grupowane = {}

# for miasto, temperatura in dane:
#     dane_grupowane.setdefault(miasto, []).append(temperatura)

# def srednia_listy(lista):
#     if len(lista) == 0:
#         return None
#     return sum(lista) / len(lista)

# for miasto, temperatura in dane_grupowane.items():
#     srednia = srednia_listy(temperatura)
#     print(f'Średnia temperatura roczna w mieście {miasto} wynosi: {srednia:.2f} stopni celsjusza.')
