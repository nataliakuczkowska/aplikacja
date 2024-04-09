import tkinter as tk
from kolumnowy import Kolumnowy
from gui_wzór import Gui_wzór
import time

class Kolumnowy_gui(Gui_wzór):
    def __init__(self, parent, root):
        super().__init__(parent, root)
        self.nazwa_szyfru = "Szyfr Kolumnowy"
        self.tekst_klucz = "Podaj klucz"
        self.tekst_b = ""

    # def waliduj(self, tekst, ekran):
    #     if tekst == "":
    #         ekran["text"] = "Wpisz tekst"
    #         return False

    #     return True

    def zaszyfruj_tekst(self, pole_na_dane, pole_na_n,_, ekran, ekran2):
        def f():
            n,_, tekst = self.pobieranie_danych(ekran, ekran2, pole_na_dane, pole_na_n, None)
            poprawne, klucz,_  = self.waliduj(n,_, tekst, ekran)

            if poprawne == True:
                start=time.time()
                tekst_zaszyfowany = Kolumnowy().szyfrowanie(klucz, tekst)
                stop=time.time()
                self.czas=stop-start
                ekran["text"] = "Zaszyfrowany tekst"
                ekran2.insert(tk.END, tekst_zaszyfowany)
                self.tekst_wyświetlany=tekst_zaszyfowany

        return f

    def odszyfruj_tekst(self, pole_na_dane, pole_na_n,_, ekran, ekran2):
        def f():
            n,_, tekst = self.pobieranie_danych(ekran, ekran2, pole_na_dane, pole_na_n, None)
            poprawne, klucz,_  = self.waliduj(n,_, tekst, ekran)

            if poprawne == True:
                start=time.time()
                tekst_odszyfowany = Kolumnowy().deszyfrowanie(klucz,tekst)
                stop=time.time()
                self.czas=stop-start
                ekran["text"] = "Odszyfrowany tekst"
                ekran2.insert(tk.END, tekst_odszyfowany)
                self.tekst_wyświetlany=tekst_odszyfowany

        return f
    


    def gui(self):
        root = self.root
        ekran, ekran2 = self.inicjalizacjaEkranu(root)
        pole_na_tekst, pole_na_n,_ = self.inicjalizacjaPól(root)
        przyciski = self.inicjalizacjaPrzycisków(
            root, pole_na_tekst, ekran, pole_na_n, ekran2
        )
        napisy = self.etykietki(root)
