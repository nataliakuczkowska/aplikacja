import tkinter as tk
from vigenere import Vigenere
from gui_wzór import Gui_wzór
import time

class Vigenere_gui(Gui_wzór):

    def __init__(self, parent, root):
        super().__init__(parent, root)
        self.nazwa_szyfru = "Szyfr Vigenère’a"
        self.tekst_klucz = "Podaj klucz"
        self.tekst_b = ""

    def zaszyfruj_tekst(self, pole_na_dane, pole_na_n,_, ekran, ekran2):
        def f():
            klucz,_, tekst = self.pobieranie_danych(ekran, ekran2, pole_na_dane, pole_na_n, None)
            poprawne = self.waliduj(klucz, tekst, ekran)

            if poprawne == True:
                start=time.time()
                tekst_zaszyfowany = Vigenere().szyfrowanie(tekst, klucz)
                stop=time.time()
                self.czas=stop-start
                ekran["text"] = "Zaszyfrowany tekst"
                ekran2.insert(tk.END, tekst_zaszyfowany)
                self.tekst_wyświetlany=tekst_zaszyfowany
        return f

    def odszyfruj_tekst(self, pole_na_dane, pole_na_n,_, ekran, ekran2):
        def f():
            klucz,_, tekst = self.pobieranie_danych(ekran, ekran2, pole_na_dane, pole_na_n, None)
            poprawne= self.waliduj(klucz, tekst, ekran)

            if poprawne == True:
                start=time.time()
                tekst_odszyfowany = Vigenere().deszyfrowanie(tekst, klucz)
                stop=time.time()
                self.czas=stop-start
                ekran["text"] = "Odszyfrowany tekst"
                ekran2.insert(tk.END, tekst_odszyfowany)
                self.tekst_wyświetlany=tekst_odszyfowany
        return f

    def waliduj(self, przesuniecie, tekst, ekran):
        if tekst == "":
            ekran["text"] = "Wpisz tekst"
            return False

        if przesuniecie == "":
            ekran["text"] = "Wpisz klucz"
            return False

        return True

    def gui(self):
        root = self.root
        ekran, ekran2 = self.inicjalizacjaEkranu(root)
        pole_na_tekst, pole_na_n,_ = self.inicjalizacjaPól(root)
        self.inicjalizacjaPrzycisków(root, pole_na_tekst, ekran, pole_na_n, ekran2)
        self.etykietki(root)
