#!/usr/bin/env python
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
                        zahlen.append(entry)
                    else:
                        beliebtheiten.append(float(entry))

    return zahlen, beliebtheiten


def zahlen_ziehen(zahlen, zahlen_wkten, superzahlen, superzahlen_wkten, lotterie="6aus49"):
    #Normale Zahlen ziehen
    if lotterie == "6aus49":
        n = 6
    elif lotterie == "eurojackpot":
        n = 5

    lotto_zahlen = np.sort(np.random.choice(zahlen, size=n, replace=False, p=zahlen_wkten))

    if lotterie == "6aus49":
        #Superzahl ziehen, bis man eine hat, die nicht auch als "normale" Zahl gezogen wurde
        superzahl = lotto_zahlen[0]
        while superzahl in lotto_zahlen:
            superzahl = np.random.choice(superzahlen, p=superzahlen_wkten)
    elif lotterie == "eurojackpot":
        #Eurozahlen ziehen bis man welche hat, die nicht auch als "normale" Zahlen gezogen wurden
        eurozahlen = (lotto_zahlen[0], lotto_zahlen[1])
        while eurozahlen[0] in lotto_zahlen or eurozahlen[1] in lotto_zahlen:
            eurozahlen = np.random.choice(superzahlen, p=superzahlen_wkten).split("-")
            eurozahlen = [int(eurozahlen[0]), int(eurozahlen[1])]

        superzahl = "{}, {}".format(eurozahlen[0], eurozahlen[1])

    return lotto_zahlen, superzahl


def print_usage():
    print("BENUTZUNG: python {} <6aus49/eurojackpot> <#Reihen>".format(sys.argv[0]))
    sys.exit(1)


if __name__ == "__main__":
    #Wieviele Reihen sollen gespielt werden?
    if len(sys.argv) == 1:
        lotterie = "6aus49"
        n_reihen = 1
    elif len(sys.argv) == 2:
        lotterie = sys.argv[1]
        n_reihen = 1
    elif len(sys.argv) == 3:
        lotterie = sys.argv[1]
        n_reihen = int(sys.argv[2])
    else:
        print_usage()

    if lotterie != "6aus49" and lotterie != "eurojackpot":
        print_usage()

    #(Normale) Zahlen einlesen
    zahlen, beliebtheiten = zahlen_einlesen(f"data/{lotterie}/Zahlen_Beliebtheiten.txt")
    zahlen = [int(zahl) for zahl in zahlen]

    #Gewichte anhand der Beliebtheiten erzeugen
    gewichte = 1 / (np.asarray(beliebtheiten)**2)
    wahrscheinlichkeiten = gewichte/np.sum(gewichte)

    #Das Ganze nun noch fuer die Superzahl/Eurozahlen
    superzahlen, superbeliebtheiten = zahlen_einlesen(f"data/{lotterie}/Superzahlen_Beliebtheiten.txt")

    #Gewichte erzeugen
    supergewichte = 1 / (np.asarray(superbeliebtheiten)**2)
    superwahrscheinlichkeiten = supergewichte/np.sum(supergewichte)

    #Reihen ziehen und ausgeben
    if lotterie == "6aus49":
        print("{0:>10} | {1:>23} | {2:>9}".format("Reihe", "Zahlen", "Superzahl"))
    elif lotterie == "eurojackpot":
        print("{0:>10} | {1:>23} | {2:>9}".format("Reihe", "Zahlen", "Eurozahlen"))

    for i in range(n_reihen):
        lotto_zahlen, superzahl = zahlen_ziehen(zahlen, wahrscheinlichkeiten, superzahlen,
                                                superwahrscheinlichkeiten, lotterie)
        print("{0:>10} | {1:>23} | {2:>9}".format(i+1, ", ".join(map(str, lotto_zahlen)), superzahl))


#input()  #Noetig um die Ausgabe in Windows geoeffnet zu lassen
