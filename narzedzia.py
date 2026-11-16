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