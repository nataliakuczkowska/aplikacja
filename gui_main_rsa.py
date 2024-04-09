import tkinter as tk
from gui_wzór import Gui_wzór
from gui_klucz_rsa import Gui_klucz_rsa
from gui_szyfrowanie_rsa import Gui_szyfrowanie_rsa
from gui_deszyfrowanie_rsa import Gui_deszyfrowanie_rsa

class Gui_RSA_menu(Gui_wzór):

    def __init__(self, parent, root):
        super().__init__(parent, root)

    def etykietki(self, root):
        rsa = tk.Label(
            root,
            text="RSA",
            width=65,
            bg="black",
            fg="#DEBA2F",
            font=("Courier New", 20, "bold"),
        )
        rsa.grid(row=0, column=0, ipady=15, ipadx=5, columnspan=3)
        return rsa
    
    def przyciski_rsa(self, root):
        szyfrowanie = tk.Button(
            self.root,
            text="SZYFROWANIE",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        szyfrowanie.configure(
            command=self.szyfrowanie()
        )
        szyfrowanie.grid(row=2, column=1, ipady=10, ipadx=10, pady=10)

        deszyfrowanie = tk.Button(
            self.root,
            text="DESZYFROWANIE",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        deszyfrowanie.configure(
            command=self.deszyfrowanie()
        )
        deszyfrowanie.grid(row=3, column=1, ipady=10, ipadx=10, pady=10)

        nowy_klucz = tk.Button(
            self.root,
            text="GENEROWANIE KLUCZY",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        nowy_klucz.configure(
            command=self.nowy_klucz()
        )
        nowy_klucz.grid(row=1, column=1, ipady=10, ipadx=10, pady=10)
        powrót = tk.Button(
            root,
            text="POWRÓT DO MENU",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        powrót.grid(row=12, column=1, ipady=10, ipadx=10, pady=20)
        powrót.configure(command=self.funkcja_przycisku_powrót())
    def szyfrowanie(self):
        def f():
            self.wyczyść_okno(self.root)
            Gui_szyfrowanie_rsa(parent=self, root=self.root).gui()
        return f
    
    def deszyfrowanie(self):
        def f():
            self.wyczyść_okno(self.root)
            Gui_deszyfrowanie_rsa(parent=self, root=self.root).gui()
        return f
    
    def nowy_klucz(self):
        def f():
            self.wyczyść_okno(self.root)
            Gui_klucz_rsa(parent=self, root=self.root).gui()
        return f

    def gui(self):
        self.wyczyść_okno(self.root)
        przyciski = self.przyciski_rsa(self.root)
        napisy = self.etykietki(self.root)