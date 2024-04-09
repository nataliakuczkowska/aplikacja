from gui_wzór_rsa import Gui_wzór_rsa
import time
import tkinter as tk
from rsa import RSA

class Gui_klucz_rsa(Gui_wzór_rsa):

    def __init__(self, parent, root):
        super().__init__(parent, root)
        self.tekst='GENEROWANIE KLUCZA'
        self.tekst2=''
        self.n = 0
        self.e = 0
        self.d = 0


    def inicjalizacjaPrzycisków(self, root, ekran, ekran2, dlugosc_klucza):
        zapisz_do_pliku = tk.Button(
            self.root,
            text="ZAPISZ DO PLIKU",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        zapisz_do_pliku.configure(
            command=self.funkcja_przycisku_zapisz_klucz()
        )
        zapisz_do_pliku.grid(row=4, column=1, ipady=10, ipadx=15, pady=10)
        wygeneruj_klucz = tk.Button(
            self.root,
            text="WYGENERUJ KLUCZ",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        wygeneruj_klucz.configure(
            command=self.funkcja_przycisku_nowy_klucz(ekran, ekran2, dlugosc_klucza)
        )
        wygeneruj_klucz.grid(row=3, column=1, ipady=10, ipadx=15, pady=10)
        powrót = tk.Button(
            root,
            text="POWRÓT DO MENU",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        powrót.grid(row=12, column=1, ipady=10, ipadx=10, pady=20)
        powrót.configure(command=self.funkcja_przycisku_powrót())

    def waliduj(self, klucz, ekran):
        if klucz == "":
            ekran["text"] = "Wpisz długość klucza"
            return False, None

        try:
            n = int(klucz)
        except ValueError:
            ekran["text"] = "Wpisz liczbę"
            return False, None

        return True, n
    
    def funkcja_przycisku_nowy_klucz(self, ekran, ekran2, dlugosc_klucza):
        def f():
            klucz=dlugosc_klucza.get()
            poprawne, klucz_int = self.waliduj(klucz, ekran)

            if poprawne == True:
                rsa=RSA(długość_klucza=klucz_int)
                self.wyczyść_ekrany(ekran, ekran2)
                self.n, self.e = rsa.klucz_publiczny()
                self.d =  rsa.klucz_prywatny_d()
                ekran["text"] = "Wygenerowane klucze"
                tekst= f"Klucz publiczny \nn = {self.n} \ne = {self.e}\nKlucz prywatny \nd = {self.d}"
                ekran2.insert(tk.END,tekst)

        return f
    
    def funkcja_przycisku_zapisz_klucz(self):
        def f():
            self.plik.zapisz_bloki_do_pliku([self.n, self.e], 'klucz_publiczny')
            self.plik.zapisz_bloki_do_pliku([self.n, self.d], 'klucz_prywatny')
        return f
    
    def wpisz_teskt(self):
        wpisz_tekst = tk.Label(
            self.root,
            text='Podaj długość klucza',
            width=65,
            bg="black",
            fg="#DEBA2F",
            font=("Courier New", 20, "bold"),
        )
        wpisz_tekst.grid(row=1, column=0, ipady=15, ipadx=5, columnspan=3)
        return wpisz_tekst
    
    def inicjalizacjaPól(self):
        dlugosc_klucza = tk.Entry(self.root, width=75)
        dlugosc_klucza.grid(row=2, column=0, ipady=15, ipadx=1, columnspan=3)
        return dlugosc_klucza
    
    def inicjalizacjaEkranu(self, root):
        ekran = tk.Label(root, bg="black", width=46, fg="#DEBA2F", font=("Courier New", 15, "bold"))
        ekran.grid(row=10, column=0, ipady=15, ipadx=0, columnspan=3)
        ekran2 = tk.Text(
            root,
            wrap="word",
            bg="#C0CBCB",
            width=70,
            height=20,
            font=("Courier New", 12, "bold"),
        )
        ekran2.grid(row=11, column=0, ipady=5, ipadx=0,padx=10, columnspan=3)
        return ekran, ekran2
    
    def gui(self):
        self.wyczyść_okno(self.root)
        ekran, ekran2 = self.inicjalizacjaEkranu(self.root)
        dlugosc_klucza = self.inicjalizacjaPól()
        przyciski = self.inicjalizacjaPrzycisków(self.root, ekran, ekran2, dlugosc_klucza)
        napisy = self.etykietki()
        podaj_dlugosc_klucza = self.wpisz_teskt()
