import tkinter as tk
from gui_wzór import Gui_wzór
from analiza_częstości import Analiza_częstości

class Analiza_gui(Gui_wzór):
    def __init__(self, parent, root):
        super().__init__(parent, root)
        self.nazwa_szyfru = "Analiza częstotliwościowa"
        self.tekst_klucz = ""
        self.tekst_b = ""

    def inicjalizacjaPrzycisków(self, root, pole_na_dane, ekran, ekran2):
        ilość = tk.Button(
            root,
            text="ILOŚĆ ZNAKÓW",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        ilość.grid(row=7, column=1, ipady=10, ipadx=15, pady=20, sticky="W")
        ilość.configure(command=self.analiza_ilość(pole_na_dane, ekran, ekran2, root))

        procent = tk.Button(
            root,
            text="OBLICZ PROCENT",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        procent.grid(row=7, column=1, ipady=10, ipadx=25, pady=20, padx=40)
        procent.configure(
            command=self.analiza_procent(pole_na_dane, ekran, ekran2, root)
        )

        histogram = tk.Button(
            root,
            text="HISTOGRAM",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        histogram.grid(row=7, column=1, ipady=10, ipadx=30, pady=20, sticky="E")
        histogram.configure(command=self.pokaż_histogram(pole_na_dane, ekran))

        powrót = tk.Button(
            root,
            text="POWRÓT DO MENU",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        powrót.grid(row=13, column=1, ipady=10, ipadx=10, pady=20)
        powrót.configure(command=self.funkcja_przycisku_powrót())

        wczytaj_plik = tk.Button(
            root,
            text="WCZYTAJ Z PLIKU",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        wczytaj_plik.grid(row=8, column=1, ipady=10, ipadx=10, pady=20, padx=10, sticky="W")
        wczytaj_plik.configure(command=self.funkcja_przycisku_wczytaj_plik())

        usuń_plik = tk.Button(
            root,
            text="USUŃ PLIK",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        usuń_plik.grid(row=8, column=1, ipady=10, ipadx=20, pady=20)
        usuń_plik.configure(command=self.funkcja_przycisku_usuń(ekran, ekran2))

        zapisz_do_pliku = tk.Button(
            root,
            text="ZAPISZ DO PLIKU",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        zapisz_do_pliku.grid(
            row=8, column=1, ipady=10, ipadx=15, pady=20, padx=1, sticky="E"
        )
        zapisz_do_pliku.configure(command=self.funkcja_przycisku_zapisz())
        return ilość, procent, histogram, powrót, wczytaj_plik, usuń_plik, zapisz_do_pliku

    def analiza_ilość(self, pole_na_dane, ekran, ekran2, root):
        def f():
            self.wyczyść_ekrany(ekran, ekran2)
            if self.plik.czy_jest_plik == False:
                tekst = pole_na_dane.get()
                poprawne = self.waliduj(tekst, ekran)
            else:
                tekst = self.plik.tekst_z_pliku
                poprawne = True

            if poprawne == True:
                znaki_posortowane = Analiza_częstości().analiza_ilość(tekst)
                ekran["text"] = "Wynik"
                ekran2.insert(tk.END, znaki_posortowane)
                self.tekst_wyświetlany = znaki_posortowane

        return f

    def analiza_procent(self, pole_na_dane, ekran, ekran2, root):
        def f():
            self.wyczyść_ekrany(ekran, ekran2)
            if self.plik.czy_jest_plik == False:
                tekst = pole_na_dane.get()
                poprawne = self.waliduj(tekst, ekran)
            else:
                tekst = self.plik.tekst_z_pliku
                poprawne = True

            if poprawne == True:
                procent = Analiza_częstości().analiza_procent(tekst)
                ekran["text"] = "Wynik"
                ekran2.insert(tk.END, procent)
                self.tekst_wyświetlany = procent

        return f

    def pokaż_histogram(self, pole_na_dane, ekran):
        def f():
            if self.plik.czy_jest_plik == False:
                tekst = pole_na_dane.get()
                poprawne = self.waliduj(tekst, ekran)
            else:
                tekst = self.plik.tekst_z_pliku
                poprawne = True

            if poprawne == True:
                Analiza_częstości().histogram(tekst)

        return f

    def waliduj(self, tekst, ekran):
        if tekst == "":
            ekran["text"] = "Wpisz tekst"
            return False

        return True

    def gui(self):
        root = self.root
        ekran, ekran2 = self.inicjalizacjaEkranu(root)
        pole_na_tekst, _ , b= self.inicjalizacjaPól(root)
        self.inicjalizacjaPrzycisków(root, pole_na_tekst, ekran, ekran2)
        self.etykietki(root)
