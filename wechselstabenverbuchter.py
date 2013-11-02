# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import random

# <codecell>

def verbuchte(string):
    string = string.split()
    for i in range(len(string)):
        if len(string[i]) > 2:
            pre = string[i][:2]
            post = string[i][-1:]
            mid = ''.join(random.sample(string[i][2:-1],len(string[i][2:-1])))
            if len(mid)>1:
                while mid == string[i][2:-1]:
                    mid = ''.join(random.sample(string[i][2:-1],len(string[i][2:-1])))
            string[i]=pre+mid+post
    return ' '.join(string)

# <codecell>

text = u'Wie man an diesem Beispiel zweifelsfrei sieht, \
    ist das Gehirn relativ gut in der Lage diese Wörter zu erkennen, \
    selbst wenn die Buchstaben in zufälliger Reihenfolge sind. \
    Wichtig ist nur, dass Anfangs- und Endbuchstabe an der \
    richtigen Stelle stehen und die korrekten Buchstaben verwendet wurden. \
    Die Jungs bei der NSA müssen jetzt aber alles mit deutschen \
    Dolmetschern checken lassen oder alle Nachrichten zufällig \
    zurück durch sortieren. :)'


print verbuchte(text)

# <codecell>


# <codecell>


