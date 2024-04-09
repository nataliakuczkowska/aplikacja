from gui_wzór_rsa import Gui_wzór_rsa
import time
import tkinter as tk
from rsa import RSA

class Gui_deszyfrowanie_rsa(Gui_wzór_rsa):

    def __init__(self, parent, root):
        super().__init__(parent, root)
        self.tekst='DESZYFROWANIE'
        self.tekst2='PRYWATNY'
    
    def funkcja_przycisku_szyfrowanie(self, ekran, ekran2, pole_dlugosc_tekstu):
        def f():
            niepoprawny_tekst = self.plik.tekst_z_pliku
            tekst = niepoprawny_tekst.replace('\n',',').split(",")
            x, y =0, 0
            tekst.pop()
            tekst_int = [int(element) for element in tekst]
            poprawne, x, y = self.parent.waliduj(x, y, tekst_int, ekran)

            
            dlugosc_tekstu=pole_dlugosc_tekstu.get()
            poprawne, self.dlugosc_tekstu = self.waliduj(dlugosc_tekstu, ekran)

            if poprawne == True:
                start=time.time()
                rsa=RSA(klucz_prywatny=self.klucz, symbols=self.symbole, dlugosc_tekstu=self.dlugosc_tekstu)
                tekst_odszyfowany = rsa.deszyfrowanie_rsa(tekst_int)
                stop=time.time()
                self.czas=stop-start
                ekran["text"] = "Odszyfrowany tekst"
                ekran2.insert(tk.END, tekst_odszyfowany)
                self.tekst_wyświetlany=tekst_odszyfowany

        return f
    def waliduj(self, dlugosc_tekstu, ekran):
        if dlugosc_tekstu == "":
            ekran["text"] = "Wpisz długość tekstu"
            return False, None

        try:
            d = int(dlugosc_tekstu)
        except ValueError:
            ekran["text"] = "Wpisz liczbę"
            return False, None

        return True, d

    def funkcja_przycisku_zapisz_do_pliku(self):
        def f():
            self.plik.dodaj_i()
            self.plik.zapisz_do_pliku(self.tekst_wyświetlany, 'tekst_odszyfrowany')
        return f
    
    def funkcja_przycisku_wczytaj_symbole(self):
        def f ():
            self.symbole=self.plik.wczytaj_symbole()
        return f
    
    def prziciski(self):
        wczytaj_symbole = tk.Button(
            self.root,
            text="WCZYTAJ SYMBOLE",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        wczytaj_symbole.configure(
            command=self.funkcja_przycisku_wczytaj_symbole()
        )
        wczytaj_symbole.grid(row=2, column=1, ipady=10, ipadx=10, pady=10)
        return
    
    def inicjalizacjaPól(self):
        pole_dlugosc_tekstu = tk.Entry(self.root, width=75)
        pole_dlugosc_tekstu.grid(row=4, column=0, ipady=15, ipadx=1, columnspan=3)
        return pole_dlugosc_tekstu
    
    def napis(self):
        tekst = tk.Label(
            self.root,
            text='Podaj długość tekstu',
            width=65,
            bg="black",
            fg="#DEBA2F",
            font=("Courier New", 20, "bold"),
        )
        tekst.grid(row=3, column=0, ipady=15, ipadx=5, columnspan=3)
        return tekst
    
    def gui(self):
        self.wyczyść_okno(self.root)
        ekran, ekran2 = self.inicjalizacjaEkranu(self.root)
        pole_dlugosc_tesktu = self.inicjalizacjaPól()
        przyciski = self.inicjalizacjaPrzycisków(self.root, ekran, ekran2, pole_dlugosc_tesktu)
        dodatkowe_przyciski = self.prziciski()
        napisy = self.etykietki()
        dodatkowy_napis=self.napis()