from __future__ import print_function
import numpy as np
import sys

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


def zahlen_ziehen(zahlen, zahlen_wkten, superzahlen, superzahlen_wkten):
    #Zahlen ziehen
    lotto_zahlen = np.sort(np.random.choice(zahlen, size=6, replace=False, p=zahlen_wkten))

    #Superzahl ziehen, bis man eine hat, die nicht auch als "normale" Zahl gezogen wurde
    superzahl = lotto_zahlen[0]
    while superzahl in lotto_zahlen:
        superzahl = np.random.choice(superzahlen, p=superzahlen_wkten)

    return lotto_zahlen, superzahl


if __name__ == "__main__":
    #Wieviele Reihen sollen gespielt werden?
    if len(sys.argv) == 2:
        n_reihen = int(sys.argv[1])
    elif len(sys.argv) == 1:
        n_reihen = 1
    else:
        print("BENUTZUNG: python {} <Anzahl_Reihen>".format(sys.argv[0]))

    #(Normale) Zahlen einlesen
    zahlen, beliebtheiten = zahlen_einlesen("Zahlen_Beliebtheiten.txt")

    #Gewichte erzeugen
    gewichte = 1 / (np.asarray(beliebtheiten)**2)
    wahrscheinlichkeiten = gewichte/np.sum(gewichte)

    #Das Ganze nun noch fuer die Superzahl
    superzahlen, superbeliebtheiten = zahlen_einlesen("Superzahlen_Beliebtheiten.txt")

    #Gewichte erzeugen
    supergewichte = 1 / (np.asarray(superbeliebtheiten)**2)
    superwahrscheinlichkeiten = supergewichte/np.sum(supergewichte)

    #Reihen ziehen und ausgeben
    print("{0:>10} | {1:>23} | {2:>9}".format("Reihe", "Lottozahlen", "Superzahl"))
    for i in range(n_reihen):
        lotto_zahlen, superzahl = zahlen_ziehen(zahlen, wahrscheinlichkeiten, superzahlen,
                                                superwahrscheinlichkeiten)
        print("{0:>10} | {1:>23} | {2:>9}".format(i+1, ", ".join(map(str,lotto_zahlen)),superzahl))


raw_input()  #Noetig um die Ausgabe in Windows geoeffnet zu lassen
