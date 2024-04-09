import tkinter as tk
from gui_wzór import Gui_wzór
from rsa import RSA
import time

class RSA_gui(Gui_wzór):

    def __init__(self, parent, root):
        super().__init__(parent, root)
        self.nazwa_szyfru = "RSA"
        self.tekst_klucz = ""
        self.rsa=RSA()
        self.dlugosc_tekstu=0

    def przyciski_rsa(self, ekran, ekran2):
        nowy_klucz = tk.Button(
            self.root,
            text="WYGENERUJ NOWY KLUCZ",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        nowy_klucz.configure(
            command=self.funkcja_przycisku_nowy_klucz(ekran, ekran2)
        )
        nowy_klucz.grid(row=9, column=1, ipady=10, ipadx=10, pady=20, sticky="E")

        zapisz_klucz = tk.Button(
            self.root,
            text="ZAPISZ KLUCZ",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        zapisz_klucz.configure(
            command=self.funkcja_przycisku_zapisz_klucz()
        )
        zapisz_klucz.grid(row=9, column=1, ipady=10, ipadx=10, pady=20, sticky="W")

        wczytaj_klucz_publiczny = tk.Button(
            self.root,
            text="WCZYTAJ KLUCZ PUBLICZNY",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        wczytaj_klucz_publiczny.configure(
            command=self.funkcja_przycisku_zapisz_klucz()
        )
        wczytaj_klucz_publiczny.grid(row=10, column=1, ipady=10, ipadx=10, pady=20, sticky="E")

        wczytaj_klucz_prywatny = tk.Button(
            self.root,
            text="WCZYTAJ KLUCZ PRYWATNY",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        wczytaj_klucz_prywatny.configure(
            command=self.funkcja_przycisku_zapisz_klucz()
        )
        wczytaj_klucz_prywatny.grid(row=10, column=1, ipady=10, ipadx=10, pady=20, sticky="W")

        return nowy_klucz, zapisz_klucz, wczytaj_klucz_prywatny, wczytaj_klucz_publiczny
    
    def funkcja_przycisku_nowy_klucz(self, ekran, ekran2):
        def f():
            self.rsa=RSA()
            self.wyczyść_ekrany(ekran, ekran2)
            self.wyświetl_klucz(ekran, ekran2)
        return f
    
    def funkcja_przycisku_zapisz_klucz(self):
        def f():
            self.plik.zapisz_bloki_do_pliku(self.rsa.klucz_publiczny(), 'klucz_publiczny')
            self.plik.zapisz_bloki_do_pliku(self.rsa.klucz_prywatny(), 'klucz_prywatny')
        return f
    
    def wyświetl_klucz(self, ekran, ekran2):
        n, e = self.rsa.klucz_publiczny()
        d =  self.rsa.klucz_prywatny()
        ekran["text"] = "Wygenerowane klucze"
        tekst= f"Klucz publiczny \nn = {n} \ne = {e}\nKlucz prywatny \nd = {d}"
        ekran2.insert(tk.END,tekst)
        self.tekst_wyświetlany=tekst
        
    def zaszyfruj_tekst(self, pole_na_dane, pole_na_n, ekran, ekran2):
        def f():
            n, tekst = self.pobieranie_danych(ekran, ekran2, pole_na_dane, pole_na_n)
            poprawne, n = self.waliduj(n, tekst, ekran)

            if poprawne == True:
                start=time.time()
                
                tekst_zaszyfowany = self.rsa.szyfrowanie_rsa(tekst)
                stop=time.time()
                self.czas=stop-start
                n, e = self.rsa.klucz_publiczny()
                
                ekran["text"] = "Zaszyfrowany tekst"
                ekran2.insert(tk.END, tekst_zaszyfowany)
                self.tekst_wyświetlany=tekst_zaszyfowany

        return f

    def odszyfruj_tekst(self, pole_na_dane, pole_na_n, ekran, ekran2):
        def f():
            n, niepoprawny_tekst = self.pobieranie_danych(ekran, ekran2, pole_na_dane, pole_na_n)
            poprawny_tekst = niepoprawny_tekst.replace('[','').replace(']','').replace(' ','').split(",")
            tekst_int = [int(element) for element in poprawny_tekst]
            poprawne, n = self.waliduj(n, niepoprawny_tekst, ekran)

            if poprawne == True:
                start=time.time()
                tekst_odszyfowany = self.rsa.deszyfrowanie_rsa(tekst_int)
                stop=time.time()
                self.czas=stop-start
                ekran["text"] = "Odszyfrowany tekst"
                ekran2.insert(tk.END, tekst_odszyfowany)
                self.tekst_wyświetlany=tekst_odszyfowany

        return f


    def gui(self):
        root = self.root
        ekran, ekran2 = self.inicjalizacjaEkranu(root)
        pole_na_tekst, pole_na_n = self.inicjalizacjaPól(root)
        self.inicjalizacjaPrzycisków(root, pole_na_tekst, ekran, pole_na_n, ekran2, rsa=True)
        self.przyciski_rsa(ekran, ekran2)
        self.etykietki(root)
