# Zadanie 1: czyszczenie imienia
# Funkcja popraw_imie(tekst) zamienia ' jAN kowalSKI ' na 'Jan Kowalski'.
# Podpowiedź: .strip(), .lower(), .split() (bez argumentu usuwa też podwójne spacje) i .join(), albo .title() na końcu.

# def popraw_imie(tekst):
#     slowa = tekst.lower().split()
#     wynik = []
#     for slowo in slowa:
#         wynik.append(slowo[0].upper() + slowo[1:])
#     return " ".join(wynik)

# tekst = input('Podaj imię: ')
# print(popraw_imie(tekst))

# Zadanie 2: palindrom
# Funkcja czy_palindrom(tekst) zwraca True, jeśli tekst czyta się tak samo od przodu i od tyłu, ignorując wielkość liter i spacje. 
# Przetestuj 'Kajak' i 'Kobyła ma mały bok'.
# Podpowiedź: wycinek [::-1] odwraca napis. Najpierw wyczyść tekst (małe litery, bez spacji), potem porównaj z jego odwróceniem.

# def czy_palindrom(tekst):
#     slowo = tekst.lower().replace(' ','')
#     return slowo == slowo[::-1]
        
# print(czy_palindrom('Kobyła ma mały bok'))

# Zadanie 3: zdanie w liczbach
# Dla wpisanego zdania wypisz liczbę słów, liczbę liter (bez spacji) i liczbę samogłosek.
# Podpowiedź: .split() i len dla słów. Samogłoski: pętla po znakach i sprawdzenie in 'aeiouyąę' (na małych literach).

# zdanie = input('Wpisz zdanie: ')

# il_wyrazow = len(zdanie.split())
# il_liter = 0
# il_samoglosek = 0

# for znak in zdanie.lower():
#     if znak.isalpha():
#         il_liter += 1
#         if znak in 'aeiouyąę':
#             il_samoglosek += 1

# print(f'Ilość wyrazów: {il_wyrazow}')
# print(f'Ilość liter: {il_liter}')
# print(f'Ilość samogłosek: {il_samoglosek}')


# Zadanie 4: linia pliku na słownik
# Linia 'Anna;25;Łódź' ma pola oddzielone średnikiem. 
# Funkcja linia_do_slownika(linia) zwraca {'imie': 'Anna', 'wiek': 25, 'miasto': 'Łódź'} (wiek jako liczba). 
# Potem zrób to dla listy kilku linii i zbierz wynik w liście słowników.
# Podpowiedź: .split(';') i int() na wieku. Wynik składasz ze słownika z trzema kluczami.

# def linia_do_slownika(linia):
#     imie, wiek, miasto = linia.split(';')
#     wiek = int(wiek)
#     slownik = {'imie': imie, 'wiek': wiek, 'miasto': miasto}
#     return slownik
# linie = ['Anna;25;Łódź', 'Piotr;31;Gdańsk', 'Ewa;19;Kraków']
# wyniki = []
# for linia in linie:
#     wyniki.append(linia_do_slownika(linia))
# print(wyniki)

# Zadanie 5: dane z PSE
# To są prawdziwe formaty z Twojego eksportu.
# a) tekst_na_liczbe('14266,64') zwraca 14266.64 jako float. Podpowiedź: .replace(',', '.') i float().
# b) okres_na_czasy('00:00 - 00:15') zwraca początek i koniec okresu jako dwa napisy. Podpowiedź: .split(' - ').
# c) Połącz oba w jedną funkcję, która dla trzech wartości ('2024-07-01', '00:00 - 00:15', '14266,64') 
# zwraca słownik {'doba': '2024-07-01', 'od': '00:00', 'do': '00:15', 'rzeczywiste': 14266.64}.

# def tekst_na_liczbe(tekst):
#     return float(tekst.replace(',','.'))

# def okres_na_czasy(okres):
#     od, do = okres.split(' - ')
#     return od, do

# def wiersz_do_slownika(doba, okres, rzeczywiste):
#     od, do = okres_na_czasy(okres)
#     liczba = tekst_na_liczbe(rzeczywiste)
#     slownik = {'doba': doba, 'od': od, 'do': do, 'rzeczywiste': liczba}
#     return slownik

# print(tekst_na_liczbe('14266,64'))
# print(okres_na_czasy('00:00 - 00:15'))
# print(wiersz_do_slownika('2024-07-01', '00:00 - 00:15', '14266,64'))

# Zadanie 6 (bonus): kilka wyjątków
# Funkcja bezpieczne_dzielenie(a, b) dzieli dwa napisy wpisane przez użytkownika. Osobne komunikaty dla ValueError 
# (to nie liczby) i ZeroDivisionError (dzielnik 0), a poprawny wynik zwraca przez else.

# def bezpieczne_dzielenie(a, b):
#     try:
#         liczba_a = float(a)
#         liczba_b = float(b)
#         wynik = liczba_a / liczba_b
#     except ValueError:
#         print(f'To nie są liczby!')
#         return None
#     except ZeroDivisionError:
#         print(f'Nie można dzielić przez 0!')
#         return None
#     else:
#         return wynik

# print(bezpieczne_dzielenie('10', '4'))     
# print(bezpieczne_dzielenie('10', '0'))     
# print(bezpieczne_dzielenie('abc', '2')) 