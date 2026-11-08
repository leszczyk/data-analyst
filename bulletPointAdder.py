#! python3
# bulletPointAdder.py - na początku każdego wiersza tekstu znajdującego się
# w schowku dodaje gwiazedki tworzące listę wypunktowaną w artykule Wikipedii

import pyperclip
text = pyperclip.paste()

#rozdzielenie wierszy i dodanie gwiazdek
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)