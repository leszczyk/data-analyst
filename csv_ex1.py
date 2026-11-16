import csv
with open('../dane/pse.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    naglowek = next(reader)
    wiersze = list(reader)

print(f'Nagłówek: {naglowek}')
for i in wiersze[:5]:
    print(i)
print(f'Liczba wierszy: {len(wiersze)}')
print(all(len(w) == 4 for w in wiersze))
print(len(wiersze) / 96)