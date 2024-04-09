import tkinter as tk
from cezar import Cezar
from gui_wzór import Gui_wzór
import time


class Cezar_gui(Gui_wzór):
    def __init__(self, parent, root):
        super().__init__(parent, root)
        self.nazwa_szyfru = "Szyfr Cezara"
        self.tekst_klucz = "Podaj przesunięcie"
        self.tekst_b = ""

    def zaszyfruj_tekst(self, pole_na_dane, pole_na_n, pole_na_b, ekran, ekran2):
        def f():
            
            przesuniecie,_ , tekst = self.pobieranie_danych(ekran, ekran2, pole_na_dane, pole_na_n, pole_na_b)
            poprawne, n,_  = self.waliduj(przesuniecie,_, tekst, ekran)
            if poprawne == True:
                start=time.time()
                tekst_zaszyfowany = Cezar().szyfrowanie(tekst, n)
                stop=time.time()
                self.czas=stop-start
                ekran["text"] = "Zaszyfrowany tekst"
                ekran2.insert(tk.END, tekst_zaszyfowany)
                self.tekst_wyświetlany=tekst_zaszyfowany
            
        return f

    def odszyfruj_tekst(self, pole_na_dane, pole_na_n, pole_na_b, ekran, ekran2):
        def f():
            przesuniecie,_ , tekst = self.pobieranie_danych(ekran, ekran2, pole_na_dane, pole_na_n, pole_na_b)
            poprawne, n, _ = self.waliduj(przesuniecie,_, tekst, ekran)
            
            if poprawne == True:
                start=time.time()
                tekst_odszyfowany = Cezar().deszyfrowanie(tekst, n)
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
        self.inicjalizacjaPrzycisków(root, pole_na_tekst, ekran, pole_na_n, ekran2)
        self.etykietki(root)
