# ZADANIE 1: Program pyta o imię i rok urodzenia, a wypisuje: “Cześć Anna, w tym roku skończysz X lat”.
# print("Jak masz na imię?")
# imie = input('>')
# print("W którym roku się urodziłeś?")
# rok_urodzenia = int(input('>'))
# print("Cześć " + imie +", w tym roku skończysz " + str(2026 - rok_urodzenia) + " lat.")

# ZADANIE 2: Kalkulator: pyta o dwie liczby i wypisuje wynik dodawania, odejmowania, mnożenia, dzielenia i dzielenia całkowitego
# print("Podaj dwie liczby:")
# liczba_1 = int(input('Liczba 1: '))
# liczba_2 = int(input('Liczba 2: '))
# print('Dodawanie: ' + str(liczba_1 + liczba_2))
# print('Odejmowanie: ' + str(liczba_1 - liczba_2))
# print('Mnożenie: ' + str(liczba_1 * liczba_2))
# print('Dzielenie: ' + str(liczba_1 // liczba_2))

# ZADANIE 3: Konwerter: kilometry na mile (1 km ≈ 0,621371 mili), wynik zaokrąglony do 2 miejsc (round()).
# print("Podaj odległość w kilometrach:")
# km = float(input('>'))
# print("Odległość " + str(km) + " to " + str(round((km * 0.621371),2)) + " mil.")

# ZADANIE 4: Program liczy BMI na podstawie wagi i wzrostu i wypisuje wynik.
# print("Kalkulator BMI")
# print("Podaj swoją wagę: ")
# waga = float(input('>'))
# print("Podaj swój wzrost w centymetrach: ")
# wzrost = float(input('>'))
# bmi = round((waga / ((wzrost/100)**2)),1)
# print("Twoje BMI to: " + str(bmi) + ".")

# ZADANIE 5: Program pyta o cenę netto i stawkę VAT w procentach i wypisuje cenę brutto oraz kwotę VAT.
# print("Jaka była cena netto?")
# netto = float(input('>'))
# print("Jaka była stawka VAT (w %)?")
# vat = int(input('>'))
# brutto = netto * ((100 + vat) / 100)
# kwota_vat = brutto - netto
# print("Cena brutto " + str(brutto) + " złotych.")
# print("Kwota VAT " + str(kwota_vat) + " złotych.")

# ZADANIE 6: Program pyta o wiek i wypisuje: “dziecko” (do 12), “nastolatek” (13–17), “dorosły” (18–64), “senior” (65+).
# print('Ile masz lat?')
# wiek = int(input('>'))
# if wiek <= 12:
#   print('dziecko')
# elif wiek >= 13 and wiek <= 17:
#   print('nastolatek')
# elif wiek >= 18 and wiek <= 64:
#   print('dorosły')
# else:
#   print('senior') 

# ZADANIE 7:
# Dla liczb od 1 do 50 wypisz:
# “Fizz” dla wielokrotności 3,
# “Buzz” dla wielokrotności 5,
# “FizzBuzz” dla wielokrotności obu,
# w pozostałych przypadkach samą liczbę.

# for liczba in range(1, 51):
#   if liczba % 3 == 0 and liczba % 5 == 0:
#     print('FizzBuzz')
#   elif liczba % 5 == 0:
#     print('Buzz')
#   elif liczba % 3 == 0:
#     print('Fizz')
#   else:
#     print(liczba)

# ZADANIE 8: Program pyta o liczbę i wypisuje jej tabliczkę mnożenia od 1 do 10, np. 7 x 3 = 21.
# liczba = int(input('Podaj liczbę: '))
# for i in range(1,11):
#   wynik = liczba * i
#   print(f'{liczba} x {i} = {wynik}')

# ZADANIE 9: Program losuje liczbę od 1 do 100, a użytkownik zgaduje. Po każdej próbie program podpowiada “za mało” lub “za dużo”. Po trafieniu wypisuje liczbę prób.
# import random
# liczba_los = random.randint(1,100)
# print('Wylosowano liczbę z zakresu 1 - 100, spróbuj ją odgadnąć')
# licznik = 1
# while True:
#   print(f'Próba #{licznik}')
#   liczba = int(input("Zgadnij liczbę: "))
#   if liczba > liczba_los:
#     print('Za wysoko')
#   elif liczba < liczba_los:
#     print('Za nisko')
#   else:
#     break
#   licznik = licznik + 1
#   print(f'Gratulacje, trafiłeś w {licznik} próbie!')

# ZADANIE 10: Program wczytuje liczby w pętli, aż użytkownik wpisze słowo “koniec”. Potem wypisuje sumę, średnią i największą liczbę.
# suma = 0
# licznik = 0
# maks = None
# while True:
#   wejscie = input('Podaj liczbę lub zakończ programi wpisując koniec: ')
#   if wejscie == 'koniec':
#     break
#   liczba = float(wejscie)
#   suma += liczba
#   licznik += 1  
#   if maks is None or liczba > maks:
#     maks = liczba
# if licznik == 0:
#   print('Nie podano żadniej liczby')
# else:
#   avg = suma / licznik
#   print(f'Suma = {suma}, Średnia = {avg}, Maksimum = {maks}')

  # ZADANIE 11: Program ma sprawdzić, czy podana liczba jest pierwsza, czyli ma dokładnie dwa dzielniki: 1 i samą siebie.
# print('Program sprawdzający czy liczba jest liczbą pierwszą')
# liczba = int(input('Podaj liczbę: '))
# if liczba < 2:
#   print(f'Liczba {liczba} nie jest liczbą pierwszą')
# else:
#   pierwsza = True
#   for dzielnik in range(2, liczba):
#     if liczba % dzielnik == 0:
#       pierwsza = False
#       break
#   if pierwsza:
#     print(f'Liczba {liczba} jest liczbą pierwszą')
#   else:
#     print(f'Liczba {liczba} nie jest liczbą pierwszą')


