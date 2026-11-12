# Zadanie 1: Zapis i odczyt. Zapisz 5 słów do lista.txt, każde w osobnej linii. 
# Wczytaj plik i wypisz zawartość z numerami linii (1: słowo).
# Podpowiedź: 'w', \n na końcu każdej linii, pętla for linia in f, a .strip() usuwa znak nowej linii.

# with open('lista.txt', 'w', encoding='utf-8') as f:
#     f.write('Niemcy\n')
#     f.write('Czechy\n')
#     f.write('Słowacja\n')
#     f.write('Ukraina\n')
#     f.write('Białoruś\n')
#     f.write('Litwa\n')
#     f.write('Rosja\n')

# with open('lista.txt', 'r', encoding='utf-8') as f:
#     for numer, linia in enumerate(f, start = 1):
#         print(f'{numer}: {linia.strip()}')

# Zadanie 2: Dziennik. Program pyta o wpis i dopisuje go do dziennik.txt z datą i godziną. Uruchom kilka razy i sprawdź, 
# że stare wpisy zostają. Podpowiedź: tryb 'a', from datetime import datetime, datetime.now().

# from datetime import datetime

# content = input('Wprowadź dane do dziennika: ')
# znak_czasu = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# with open('dziennik.txt', 'a', encoding='utf-8') as f:
#     f.write(f'[{znak_czasu}] {content}\n')

# with open('dziennik.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

# Zadanie 3: Statystyki pliku. Funkcja statystyki(nazwa_pliku) zwraca słownik z liczbą linii, słów i znaków.
# Podpowiedź: .read(), .split() i len. Linie możesz policzyć przez .splitlines().

# def statystyki(nazwa_pliku):
#     with open(nazwa_pliku, 'r', encoding='utf-8') as f:
#         content = f.read()

#         l_linii = len(content.splitlines())
#         l_slow = len(content.split())
#         l_znakow = len(content)
#         stats = {'Liczba linii': f'{l_linii}',
#                      'Liczba słów': f'{l_slow}',
#                      'Liczba znaków': f'{l_znakow}'}
#         return stats

# print(statystyki('lista.txt'))

# Zadanie 4: Bezpieczny input. wczytaj_liczbe(pytanie) pyta w pętli, aż użytkownik poda poprawną liczbę.
# Podpowiedź: while True, try: ... except ValueError:, return po udanej konwersji.

# def wczytaj_liczbe(pytanie):
#     while True: 
#         tekst = input(pytanie)
#         try:
#             liczba = float(tekst.replace(',', '.'))
#         except ValueError:
#             print('Zła liczba')
#         else:
#             return liczba

# wynik = wczytaj_liczbe('Podaj liczbę: ')
# print(f'Podano: {wynik}')

# Zadanie 5: Brakujący plik. Funkcja wczytuje plik i zwraca jego treść, a gdy pliku nie ma, wypisuje komunikat i zwraca pusty napis.
# Podpowiedź: except FileNotFoundError, konkretny wyjątek, a nie gołe except:.

# def odczyt_pliku(plik):
#     try:
#         with open(plik, 'r', encoding='utf-8') as f:
#             content = f.read()
#     except FileNotFoundError:
#         print('Nie ma takiego pliku')
#         return ''
#     else:
#         return content

# nazwa = input('Podaj nazwę pliku: ')
# print(odczyt_pliku(nazwa))

# Bonus: bezpieczne_dzielenie(a, b), czyli try / except / else z osobnymi komunikatami dla ValueError i ZeroDivisionError. 
# Szkielet i testy masz z wcześniejszej wiadomości.

# def bezpieczne_dzielenie(a, b):
#     try:
#         liczba_a = float(str(a).replace(',','.'))
#         liczba_b = float(str(b).replace(',','.'))
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