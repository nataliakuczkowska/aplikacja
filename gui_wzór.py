import tkinter as tk
import pyperclip
from plik import Plik

class Gui_wzór:
    def __init__(self, parent, root):
        self.parent = parent
        self.root = root
        self.tekst_wyświetlany = ""
        self.plik = Plik()
        self.czas = 0

    def inicjalizacjaEkranu(self, root):
        ekran = tk.Label(root, bg="black", width=46, fg="#DEBA2F", font=("Courier New", 15, "bold"))
        ekran.grid(row=10, column=0, ipady=15, ipadx=0, columnspan=3)
        ekran2 = tk.Text(
            root,
            wrap="word",
            bg="#C0CBCB",
            width=50,
            height=10,
            font=("Courier New", 12, "bold"),
        )
        ekran2.grid(row=11, column=0, ipady=5, ipadx=0,padx=10, columnspan=3)
        return ekran, ekran2

    def etykietki(self, root):
        szyfr = tk.Label(
            root,
            text=self.nazwa_szyfru,
            width=65,
            bg="black",
            fg="#DEBA2F",
            font=("Courier New", 20, "bold"),
        )
        szyfr.grid(row=0, column=0, ipady=15, ipadx=5, columnspan=3)
        wspisz_tekst = tk.Label(
            root,
            text="Wpisz tekst",
            width=65,
            bg="black",
            fg="white",
            font=("Courier New", 15, "bold"),
        )
        wspisz_tekst.grid(row=1, column=0, ipady=15, ipadx=5, columnspan=3)
        klucz = None
        if self.tekst_klucz != "":
            klucz = tk.Label(
                root,
                text=self.tekst_klucz,
                width=65,
                bg="black",
                fg="white",
                font=("Courier New", 15, "bold"),
            )
            klucz.grid(row=3, column=0, ipady=15, ipadx=5, columnspan=3)
        return wspisz_tekst, klucz, szyfr

    def inicjalizacjaPól(self, root):
        pole_na_dane = tk.Entry(root, width=75)
        pole_na_dane.grid(row=2, column=0, ipady=15, ipadx=1, columnspan=3)
        pole_na_n = None
        if self.tekst_klucz != "":
            pole_na_n = tk.Entry(root, width=75)
            pole_na_n.grid(row=4, column=0, ipady=15, ipadx=1, columnspan=3)
        pole_na_b = None
        if self.tekst_b != "":
            pole_na_b = tk.Entry(root, width=75)
            pole_na_b.grid(row=6, column=0, ipady=15, ipadx=1, columnspan=3)

        return pole_na_dane, pole_na_n, pole_na_b

    def inicjalizacjaPrzycisków(self, root, pole_na_dane, ekran, pole_na_n, ekran2, pole_na_b=None, rsa=False):
        zaszyfruj = tk.Button(
            root,
            text="ZASZYFRUJ",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        odszyfruj = tk.Button(
            root,
            text="ODSZYFRUJ",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        kopiuj = tk.Button(
            root,
            text="KOPIUJ",
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
        wczytaj_plik = tk.Button(
            root,
            text="WCZYTAJ Z PLIKU",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        usuń_plik = tk.Button(
            root,
            text="USUŃ PLIK",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        zapisz_do_pliku = tk.Button(
            root,
            text="ZAPISZ DO PLIKU",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        czas = tk.Button(
            root,
            text="CZAS",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )

        zaszyfruj.grid(row=7, column=1, ipady=10, ipadx=10, sticky="E", pady=20)
        odszyfruj.grid(row=7, column=1, ipady=10, ipadx=10, sticky="W", pady=20)
        kopiuj.grid(row=12, column=1, ipady=10, ipadx=10, sticky="E", pady=20)
        powrót.grid(row=12, column=1, ipady=10, ipadx=10, sticky="W", pady=20)
        wczytaj_plik.grid(row=8, column=1, ipady=10, ipadx=2, pady=0, padx=0, sticky="W")
        usuń_plik.grid(row=8, column=1, ipady=10, ipadx=5, pady=0)
        zapisz_do_pliku.grid(
            row=8, column=1, ipady=10, ipadx=2, pady=0, padx=0, sticky="E"
        )
        czas.grid(row=7, column=1, ipady=10, ipadx=30, pady=20, padx=20)

        zaszyfruj.configure(
            command=self.zaszyfruj_tekst(pole_na_dane, pole_na_n, pole_na_b, ekran, ekran2)
        )
        odszyfruj.configure(
            command=self.odszyfruj_tekst(pole_na_dane, pole_na_n, pole_na_b, ekran, ekran2)
        )
        kopiuj.configure(command=self.funkcja_kopiuj())
        powrót.configure(command=self.funkcja_przycisku_powrót())
        wczytaj_plik.configure(command=self.funkcja_przycisku_wczytaj_plik())
        usuń_plik.configure(command=self.funkcja_przycisku_usuń(ekran, ekran2))
        zapisz_do_pliku.configure(command=self.funkcja_przycisku_zapisz())
        czas.configure(command=self.funkcja_przycisku_czas(ekran, ekran2))

        return zaszyfruj, odszyfruj, kopiuj, powrót, wczytaj_plik, usuń_plik, zapisz_do_pliku

    def funkcja_kopiuj(self):
        def f():
            pyperclip.copy(self.tekst_wyświetlany)

        return f

    def funkcja_przycisku_powrót(self):
        def f():
            self.parent.gui()

        return f

    def waliduj(self, przesuniecie, b, tekst, ekran):
        if tekst == "":
            ekran["text"] = "Wpisz tekst"
            return False, None, None

        try:
            n = int(przesuniecie)
            b_int = int(b)
        except ValueError:
            ekran["text"] = "Wpisz liczbę"
            return False, None, None

        return True, n, b_int

    def wyczyść_ekrany(self, ekran, ekran2):
        ekran["text"] = ""
        ekran2.delete('1.0', tk.END)
        self.tekst_wyświetlany = ""

    def funkcja_przycisku_wczytaj_plik(self):
        def f():
            self.plik.wczytaj_plik()

        return f

    def funkcja_przycisku_usuń(self, ekran, ekran2):
        def f():
            self.plik.usuń_plik()
            self.wyczyść_ekrany(ekran, ekran2)

        return f

    def funkcja_przycisku_zapisz(self):
        def f():
                self.plik.zapisz_do_pliku(self.tekst_wyświetlany)

        return f
    
    def funkcja_przycisku_czas(self, ekran, ekran2):
        def f():
            self.wyczyść_ekrany(ekran, ekran2)
            ekran["text"] = "Czas szyfrowania"
            ekran2.insert(tk.END, f'{self.czas} s')
        return f
    
    def pobieranie_danych(self, ekran, ekran2, pole_na_dane, pole_na_n, pole_na_b):
        self.wyczyść_ekrany(ekran, ekran2)

        if pole_na_n != None:
            przesuniecie = pole_na_n.get()
        else:
            przesuniecie = 0

        if pole_na_b != None:
            b = pole_na_b.get()
        else:
            b = 0

        if self.plik.czy_jest_plik == False:
                tekst = pole_na_dane.get()
        else:
                tekst = self.plik.tekst_z_pliku
                
        return  przesuniecie, b, tekst
    
    def wyczyść_okno(self, root):
        for element in root.winfo_children():
            element.destroy()