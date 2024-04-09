
import matplotlib.pyplot as plt
import math


class Analiza_częstości:
    
    alfabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"

    def licz_litery(self, tekst):
        tekst = tekst.upper()
        znaki = {}

        for symbol in tekst:
            if symbol in self.alfabet:
                if symbol in znaki.keys():
                    znaki[symbol] = znaki[symbol] + 1
                else:
                    znaki[symbol] = 1

        for symbol in self.alfabet:
            if not symbol in znaki.keys():
                znaki[symbol] = 0

        return znaki

    def licz_znaki(self, tekst):
        tekst = tekst.upper()
        znaki = {}

        for symbol in tekst:
            if symbol in znaki.keys():
                znaki[symbol] = znaki[symbol] + 1
            else:
                znaki[symbol] = 1

        for symbol in self.alfabet:
            if not symbol in znaki.keys():
                znaki[symbol] = 0

        return znaki

    def oblicz_procent(self, znaki):
        suma = sum(znaki.values())
        procent = znaki.copy()
        for klucz in znaki:
            procent[klucz] = float(f"{(procent[klucz]/suma)*100:.2f}")
        return procent

    def sortuj_znaki(self, znaki):
        znaki_posortowane = dict(sorted(znaki.items()))
        return znaki_posortowane

    def sortuj_wartości(self, znaki):
        znaki_posortowane = dict(sorted(znaki.items(), key=lambda x: x[1], reverse=True))
        return znaki_posortowane

    def histogram(self, tekst):
        znaki = self.licz_litery(tekst)
        procent = self.oblicz_procent(znaki)
        procent = self.sortuj_wartości(procent)
        symbole = procent.keys()
        wartości = procent.values()
        ymax = math.ceil(max(wartości) + 3)
        fig, ax = plt.subplots()
        bar_container = ax.bar(symbole, wartości)
        ax.set(ylabel="%", title="Wykres częstości liter w tekście", ylim=(0, ymax))
        ax.bar_label(bar_container)  # fmt=lambda x : f'{x} %')
        plt.show()

    def analiza_ilość(self, tekst):
        znaki = self.licz_litery(tekst)
        znaki_posortowane = self.sortuj_znaki(znaki)

        return znaki_posortowane

    def analiza_procent(self, tekst):
        znaki = self.licz_litery(tekst)
        znaki = self.sortuj_znaki(znaki)
        procent = self.oblicz_procent(znaki)
        return procent
