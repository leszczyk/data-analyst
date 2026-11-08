#! python3
# myclip.py - program schwka dla wielu ciągów tekstowych

TEXT = {'zgoda': 'Tak, zgadzam się. To brzmi rozsądnie.',
        'zajęty': ' Przepraszam, ale jestem zajęty. Czy mogę się tym zająć w przyszłym tygodniu?',
        'pytanie': 'Czy rozważassz dokonywanie comiesięcznych wpłat?'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Użycie: python myclip.py [skrót] - skopiowanie wskazanej wiadomości')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Wiadomość dla skrótu ' + keyphrase + ' została skopiowana do schowka.')
else:
    print('Nie istnieje wiadomość dla skrótu ' + keyphrase + '.')