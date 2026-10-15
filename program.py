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