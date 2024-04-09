from gui_wzór_rsa import Gui_wzór_rsa
import time
import tkinter as tk
from rsa import RSA
class Gui_szyfrowanie_rsa(Gui_wzór_rsa):

    def __init__(self, parent, root):
        super().__init__(parent, root)
        self.tekst='SZYFROWANIE'
        self.tekst2='PUBLICZNY'
        
    
    def funkcja_przycisku_szyfrowanie(self, ekran, ekran2, pole_dlugosc_tekstu):
        def f():
            tekst = self.plik.tekst_z_pliku
            x,y=0,0
            poprawne, x, y = self.waliduj(x, y, tekst, ekran)
            
            if poprawne == True:

                start=time.time()
                rsa=RSA(klucz_publiczny=self.klucz)
                tekst_zaszyfowany = rsa.szyfrowanie_rsa(tekst)
                stop=time.time()
                self.czas=stop-start
                self.symbole = rsa.get_symbole()
                self.dlugosc_tekstu = rsa.get_dlugosc_tekstu()

                ekran["text"] = "Zaszyfrowany tekst"
                ekran2.insert(tk.END, tekst_zaszyfowany)
                self.tekst_wyświetlany=tekst_zaszyfowany
        return f
    
    def funkcja_przycisku_zapisz_do_pliku(self):
        def f(): 
            self.plik.dodaj_i()
            self.plik.zapisz_do_pliku(self.symbole, 'symbole')
            self.plik.zapisz_bloki_do_pliku(self.tekst_wyświetlany, 'tekst_zaszyfrowany')
            self.plik.zapisz_do_pliku(self.dlugosc_tekstu, 'dlugosc_tekstu')

        return f

    def gui(self):
        self.wyczyść_okno(self.root)
        ekran, ekran2 = self.inicjalizacjaEkranu(self.root)
        przyciski = self.inicjalizacjaPrzycisków(self.root, ekran, ekran2)
        napisy = self.etykietki()