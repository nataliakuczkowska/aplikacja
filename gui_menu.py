import tkinter as tk
from gui_cezar import Cezar_gui
from gui_vigenere import Vigenere_gui
from gui_kolumnowy import Kolumnowy_gui
from gui_afiniczny import Afiniczny_gui
from gui_main_rsa import Gui_RSA_menu
from gui_analiza import Analiza_gui



class Main_menu_gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="black")
        self.root.geometry("1000x1000")
        
    def okienko(self):
        return self.root

    def inicjalizacjaPrzycisków(self, root):
        cezar = tk.Button(
            root,
            text="Szyfr Cezara",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        vigenere = tk.Button(
            root,
            text="Szyfr Vigenère’a",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        kolumnowy = tk.Button(
            root,
            text="Szyfr Kolumnowy",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        afiniczny = tk.Button(
            root,
            text="Szyfr Afiniczny",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )
        rsa = tk.Button(
            root, text="RSA", bg="#DEBA2F", fg="black", font=("Courier New", 13, "bold")
        )
        analiza = tk.Button(
            root,
            text="Analiza częstotliwościowa",
            bg="#DEBA2F",
            fg="black",
            font=("Courier New", 13, "bold"),
        )

        cezar.grid(row=1, column=1, ipady=10, ipadx=15, pady=10)
        vigenere.grid(row=2, column=1, ipady=10, ipadx=10, pady=10)
        afiniczny.grid(row=3, column=1, ipady=10, ipadx=10, pady=10)
        kolumnowy.grid(row=4, column=1, ipady=10, ipadx=10, pady=10)
        rsa.grid(row=5, column=1, ipady=10, ipadx=30, pady=10)
        analiza.grid(row=6, column=1, ipady=10, ipadx=30, pady=10)

        cezar.configure(command=self.funkcja_przycisku_cezar(root))
        vigenere.configure(command=self.funkcja_przycisku_vigenere(root))
        kolumnowy.configure(command=self.funkcja_przycisku_odwrotny(root))
        afiniczny.configure(command=self.funkcja_przycisku_afiniczny(root))
        rsa.configure(command=self.funkcja_przycisku_rsa(root))
        analiza.configure(command=self.funkcja_przycisku_analiza(root))

        return cezar, vigenere, kolumnowy, rsa

    def funkcja_przycisku_cezar(self, root):
        def f():
            self.wyczyść_okno(root)
            Cezar_gui(parent=self, root=root).gui()

        return f

    def funkcja_przycisku_vigenere(self, root):
        def f():
            self.wyczyść_okno(root)
            Vigenere_gui(parent=self, root=root).gui()

        return f

    def funkcja_przycisku_odwrotny(self, root):
        def f():
            self.wyczyść_okno(root)
            Kolumnowy_gui(parent=self, root=root).gui()

        return f
    
    def funkcja_przycisku_afiniczny(self, root):
        def f():
            self.wyczyść_okno(root)
            Afiniczny_gui(parent=self, root=root).gui()

        return f
    
    def funkcja_przycisku_rsa(self, root):
        def f():
            self.wyczyść_okno(root)
            Gui_RSA_menu(parent=self, root=root).gui()

        return f

    def funkcja_przycisku_analiza(self, root):
        def f():
            self.wyczyść_okno(root)
            Analiza_gui(parent=self, root=root).gui()

        return f

    def wyczyść_okno(self, root):
        for element in root.winfo_children():
            element.destroy()

    def etykietki(self, root):
        wybierz = tk.Label(
            root,
            text="Wybierz szyfr",
            width=65,
            bg="black",
            fg="#DEBA2F",
            font=("Courier New", 20, "bold"),
        )
        wybierz.grid(row=0, column=0, ipady=15, ipadx=5, columnspan=3)

    def gui(self):
        self.wyczyść_okno(self.root)
        przyciski = self.inicjalizacjaPrzycisków(self.root)
        napisy = self.etykietki(self.root)
