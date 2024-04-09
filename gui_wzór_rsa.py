from gui_wzór import Gui_wzór
import tkinter as tk
from rsa import RSA
from plik import Plik

class Gui_wzór_rsa(Gui_wzór):
    def __init__(self, parent, root):
        super().__init__(parent, root)
        # self.rsa=RSA(długość_klucza=5)
        self.klucz=[]
        self.symbole = ''
        self.dlugosc_tekstu = 0

    def etykietki(self):
        tekst = tk.Label(
            self.root,
            text=f'RSA {self.tekst}',
            width=65,
            bg="black",
            fg="#DEBA2F",
            font=("Courier New", 20, "bold"),
        )
        tekst.grid(row=0, column=0, ipady=15, ipadx=5, columnspan=3)
        return tekst
    
    def inicjalizacjaPrzycisków(self, root, ekran, ekran2, pole=None):
        wczytaj_plik = tk.Button(
            self.root,
            text="WCZYTAJ TEKST Z PLIKU",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        zapisz_do_pliku = tk.Button(
            self.root,
            text="ZAPISZ DO PLIKU",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        czas = tk.Button(
            self.root,
            text="CZAS",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        wczytaj_klucz = tk.Button(
            self.root,
            text=f"WCZYTAJ KLUCZ {self.tekst2}",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        szyfrowanie = tk.Button(
            self.root,
            text=self.tekst,
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        powrót = tk.Button(
            root,
            text="POWRÓT DO MENU",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        wczytaj_plik.configure(
            command=self.funkcja_przycisku_wczytaj_plik()
        )
        zapisz_do_pliku.configure(
            command=self.funkcja_przycisku_zapisz_do_pliku()
        )
        czas.configure(
            command=self.funkcja_przycisku_czas(ekran, ekran2)
        )
        wczytaj_klucz.configure(
            command=self.funkcja_przycisku_wczytaj_klucz()
        )
        szyfrowanie.configure(
            command=self.funkcja_przycisku_szyfrowanie(ekran, ekran2, pole_dlugosc_tekstu=pole)
        )
        powrót.configure(command=self.funkcja_przycisku_powrót()) 
        wczytaj_plik.grid(row=1, column=1, ipady=10, ipadx=15, pady=10, sticky='E')
        wczytaj_klucz.grid(row=1, column=1, ipady=10, ipadx=15, pady=10, sticky='W')
        szyfrowanie.grid(row=5, column=1, ipady=10, ipadx=10, pady=10, sticky='W')
        zapisz_do_pliku.grid(row=5, column=1, ipady=10, ipadx=10, pady=10)
        czas.grid(row=5, column=1, ipady=10, ipadx=15, pady=10, sticky='E')
        powrót.grid(row=12, column=1, ipady=10, ipadx=10, pady=20)

        return wczytaj_plik, wczytaj_klucz, szyfrowanie, zapisz_do_pliku, czas

    def funkcja_przycisku_wczytaj_klucz(self):
        def f():
            self.klucz = self.plik.wczytaj_klucz()
        return f
    

    




        
    


    
