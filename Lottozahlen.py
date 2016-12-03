from __future__ import print_function
import numpy as np

def zahlen_einlesen(filename):
    zahlen = []
    beliebtheiten = []
    with open(filename) as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                entries = line.split()
                if len(entries)%2:
                    raise ValueError("Problem when parsing line {}".format(line))
                for i, entry in enumerate(entries):
                    entry = entry.replace(",", ".")
                    if i%2 == 0:
                        zahlen.append(int(entry))
                    else:
                        beliebtheiten.append(float(entry))

    return zahlen, beliebtheiten

#(Normale) Zahlen einlesen
zahlen, beliebtheiten = zahlen_einlesen("Zahlen_Beliebtheiten.txt")

#Gewichte erzeugen
gewichte = 1 / (np.asarray(beliebtheiten)**2)
wahrscheinlichkeiten = gewichte/np.sum(gewichte)

#Zahlen ziehen
lotto_zahlen = np.sort(np.random.choice(zahlen, size=6, replace=False, p=wahrscheinlichkeiten))



#Das Ganze nun noch fuer die Superzahl
superzahlen, superbeliebtheiten = zahlen_einlesen("Superzahlen_Beliebtheiten.txt")

#Gewichte erzeugen
supergewichte = 1 / (np.asarray(superbeliebtheiten)**2)
superwahrscheinlichkeiten = supergewichte/np.sum(supergewichte)

#Superzahl ziehen, bis man eine hat, die nicht auch als "normale" Zahl gezogen wurde
superzahl = lotto_zahlen[0]
while superzahl in lotto_zahlen:
    superzahl = np.random.choice(superzahlen, p=superwahrscheinlichkeiten)


print("Lottozahlen: {}".format(", ".join(map(str,lotto_zahlen))))
print("Superzahl: {}".format(superzahl))
