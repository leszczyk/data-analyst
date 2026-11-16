import csv
import json

def tekst_na_liczbe(tekst):
    return float(tekst.replace(',','.'))

def okres_na_czasy(okres):
    od, do = okres.split(' - ')
    return od, do

def srednia_listy(lista):
    if len(lista) == 0:
        return None
    else:
        return sum(lista) / len(lista)

def znajdz_max_wiersz(wiersze):
        if len(wiersze) == 0:
            return None
        maks_wiersz = wiersze[0]
        for wiersz in wiersze[1:]:
            if wiersz['rzeczywiste'] > maks_wiersz['rzeczywiste']:
                maks_wiersz = wiersz
        return maks_wiersz

def znajdz_min_wiersz(wiersze):
        if len(wiersze) == 0:
            return None
        min_wiersz = wiersze[0]
        for wiersz in wiersze[1:]:
            if wiersz['rzeczywiste'] < min_wiersz['rzeczywiste']:
                min_wiersz = wiersz
        return min_wiersz

KOL_DOBA = 'Doba'
KOL_OKRES = 'OREB[Jednostka czasu od - do]'
KOL_PROGNOZA = 'Prognozowane zapotrzebowanie KSE[MW]'
KOL_RZECZ = 'Rzeczywiste zapotrzebowanie KSE[MW]' 

dane = []
pominete = 0

with open('../dane/pse.csv', 'r', encoding='utf-8-sig', newline='') as f:
    pseFile = csv.DictReader(f, delimiter=';')
    for nr, wiersz in enumerate(pseFile, start=2):
        try:
            od, do = okres_na_czasy(wiersz[KOL_OKRES])
            prognoza = tekst_na_liczbe(wiersz[KOL_PROGNOZA])
            rzeczywiste = tekst_na_liczbe(wiersz[KOL_RZECZ])
        except ValueError:
            print(f'Wiersz {nr}: problem z komórką: {wiersz}')
            pominete += 1
            continue
        dane.append({
            'doba': wiersz[KOL_DOBA],
            'od': od,
            'do': do,
            'prognoza': prognoza,
            'rzeczywiste': rzeczywiste,
        })

print(f'Liczba wierszy: {len(dane)}')
print(f'Pominięte: {pominete}')

lista_rzecz = []
for wiersz in dane:
    lista_rzecz.append(wiersz['rzeczywiste'])

maks_wiersz = znajdz_max_wiersz(dane)
min_wiersz = znajdz_min_wiersz(dane)
print('------------------------------------')
print(f'Średnia rzeczywista: {srednia_listy(lista_rzecz):.2f} MW')
print('------------------------------------')
print(f'Maksimum: {maks_wiersz["rzeczywiste"]} MW')
print(f'Wystąpiło od: {maks_wiersz["od"]} do: {maks_wiersz["do"]}, dnia: {maks_wiersz["doba"]}')
print('------------------------------------')
print(f'Minimum: {min_wiersz["rzeczywiste"]} MW')
print(f'Wystąpiło od: {min_wiersz["od"]} do: {min_wiersz["do"]}, dnia: {min_wiersz["doba"]}')
print('------------------------------------')


lista_blad = []
for wiersz in dane:
    lista_blad.append(wiersz['rzeczywiste'] - wiersz['prognoza'])

print(f'Średni błąd: {srednia_listy(lista_blad):.2f} MW')
if srednia_listy(lista_blad) > 0:
    print('Prognoza zaniżona')
elif srednia_listy(lista_blad) < 0:
    print('Prognoza zawyżona')
else: 
    print('Prognoza zgodna')

lista_mae = []
for wiersz in dane:
    lista_mae.append(abs(wiersz['rzeczywiste'] - wiersz['prognoza'])) 
print(f'MAE: {srednia_listy(lista_mae):.2f} MW')

wartosc_doba = {}

for wiersz in dane:
    wartosc_doba.setdefault(wiersz['doba'], []).append(wiersz['rzeczywiste'])

print('Liczba dób:', len(wartosc_doba))
for dzien, lista in wartosc_doba.items():
    print(dzien, len(lista))

with open('../dane/srednie_dobowe.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['doba','srednie_zapotrzebowanie'])
    for dzien, lista in wartosc_doba.items():
        writer.writerow([dzien, f'{srednia_listy(lista):.2f}'])

statystyki = {
    'srednia_rzeczywiste_MW': srednia_listy(lista_rzecz),
    'maksimum': {
        'wartosc_MW': maks_wiersz['rzeczywiste'],
        'doba': maks_wiersz['doba'],
        'od': maks_wiersz['od'],
        'do': maks_wiersz['do'],
    },
    'minimum': {
        'wartosc_MW': min_wiersz['rzeczywiste'],
        'doba': min_wiersz['doba'],
        'od': min_wiersz['od'],
        'do': min_wiersz['do'],
    },
    'sredni_blad_MW': srednia_listy(lista_blad),
    'mae_MW': srednia_listy(lista_mae),
    'liczba_wierszy': len(dane),
    }

with open('../dane/statystyki.json', 'w', encoding='utf-8') as f:
    json.dump(statystyki, f, indent=2, ensure_ascii=False)

with open('../dane/statystyki.json', 'r', encoding='utf-8') as f:
    wczytane = json.load(f)

print(wczytane)

print(wczytane == statystyki)