from tkinter import filedialog as fd
import os


class Plik:
    def __init__(self):
        self.czy_jest_plik = False
        self.tekst_z_pliku = ""
        self.nazwa_pliku = ""
        self.i = 0

    def wczytaj_klucz(self):
        filetypes = (("Text Files", "*.txt"),)
        ścieżka = fd.askopenfilename(
            title="Open a file", initialdir="/", filetypes=filetypes
        )
        try:
            with open(ścieżka, "r", encoding="utf-8") as plik:
                linie = plik.readlines()
        except FileNotFoundError:
            pass
        klucz=[]
        for linia in linie:
            klucz.append(int(linia.replace('\n','')))
        return klucz
    
    def dodaj_i(self):
        self.i += 1

    def wczytaj_symbole(self):
        filetypes = (("Text Files", "*.txt"),)
        ścieżka = fd.askopenfilename(
            title="Open a file", initialdir="/", filetypes=filetypes
        )
        symbole=''
        try:
            with open(ścieżka, "r", encoding="utf-8") as plik:
                symbole = "".join(plik.readlines())
        except FileNotFoundError:
            pass
        return symbole
    
    def wczytaj_plik(self):
        filetypes = (("Text Files", "*.txt"),)
        ścieżka = fd.askopenfilename(
            title="Open a file", initialdir="/", filetypes=filetypes
        )
        try:
            with open(ścieżka, "r", encoding="utf-8") as plik:
                self.tekst_z_pliku = "".join(plik.readlines())
                self.czy_jest_plik = True
                self.nazwa_pliku = os.path.basename(plik.name)
        except FileNotFoundError:
            pass

    def zapisz_do_pliku(self, tekst_wyświetlany, nazwa=None):
        self.i += 1
        wynik = str(tekst_wyświetlany)
        if not nazwa:
            nazwa=self.nazwa_pliku
        
        f = open(f"{self.i}_{nazwa}.txt", mode="w", encoding="utf-8")
        f.write(wynik)
        f.close()

    def zapisz_bloki_do_pliku(self, bloki, tekst):
        self.i += 1
        with open(f"{self.i}_{tekst}.txt", 'w',  encoding="utf-8") as file:
            for item in bloki:
                file.write("%s\n" % item)

    def usuń_plik(self):
        self.czy_jest_plik = False
        self.tekst_z_pliku = ""
        self.i = 0
        self.nazwa_pliku = ""
