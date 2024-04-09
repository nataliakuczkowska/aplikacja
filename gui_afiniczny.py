import tkinter as tk
from afiniczny import Afiniczny
from gui_wzór import Gui_wzór
import time

class Afiniczny_gui(Gui_wzór):
    def __init__(self, parent, root):
        super().__init__(parent, root)
        self.nazwa_szyfru = "Szyfr Afiniczny"
        self.tekst_klucz = "Podaj a"
        self.tekst_b = "Podaj b"


    def zaszyfruj_tekst(self, pole_na_dane, pole_na_n ,pole_na_b, ekran, ekran2):
        def f():
            
            a_n, b_n, tekst = self.pobieranie_danych(ekran, ekran2, pole_na_dane, pole_na_n, pole_na_b)
            poprawne, a, b = self.waliduj(a_n, b_n, tekst, ekran)
            N=Afiniczny().get_N()

            if poprawne:
                if Afiniczny().NWD(a,N)!=1:
                    poprawne = False
                    ekran["text"] = "Niepoprawne dane"
                    ekran2.insert(tk.END, f"Klucz 'a' musi być względnie pierwszy z {N}")


            if poprawne == True:
                start=time.time()
                tekst_zaszyfowany = Afiniczny().szyfrowanie(a, b, tekst)
                stop=time.time()
                self.czas=stop-start
                ekran["text"] = "Zaszyfrowany tekst"
                ekran2.insert(tk.END, tekst_zaszyfowany)
                self.tekst_wyświetlany=tekst_zaszyfowany
            
        return f
    
    def odszyfruj_tekst(self, pole_na_dane, pole_na_n ,pole_na_b, ekran, ekran2):
        def f():
            
            a, b, tekst = self.pobieranie_danych(ekran, ekran2, pole_na_dane, pole_na_n, pole_na_b)
            poprawne, a, b = self.waliduj(a, b, tekst, ekran)
            N=Afiniczny().get_N()
            
            if poprawne:
                if Afiniczny().NWD(a,N)!=1:
                    poprawne = False
                    ekran["text"] = "Niepoprawne dane"
                    ekran2.insert(tk.END, f"Klucz 'a' musi być względnie pierwszy z {N}")

            if poprawne == True:
                start=time.time()
                tekst_odszyfowany = Afiniczny().deszyfrowanie(a, b, tekst)
                stop=time.time()
                self.czas=stop-start
                ekran["text"] = "Odszyfrowany tekst"
                ekran2.insert(tk.END, tekst_odszyfowany)
                self.tekst_wyświetlany=tekst_odszyfowany
            
        return f
    def etykieta_b(self, root):
        wspisz_b = tk.Label(
            root,
            text=self.tekst_b,
            width=65,
            bg="black",
            fg="white",
            font=("Courier New", 15, "bold"),
        )
        wspisz_b.grid(row=5, column=0, ipady=15, ipadx=5, columnspan=3)
        return wspisz_b
    
    def gui(self):
        root = self.root
        ekran, ekran2 = self.inicjalizacjaEkranu(root)
        pole_na_tekst, pole_na_n, pole_na_b= self.inicjalizacjaPól(root)
        self.inicjalizacjaPrzycisków(root, pole_na_tekst, ekran, pole_na_n, ekran2, pole_na_b)
        self.etykietki(root)
        self.etykieta_b(root)
