import math

class Kolumnowy():

    def szyfrowanie(self, klucz, tekst):
        tekst_zaszyfrowany = [""] * klucz
        for kolumna in range(klucz):
            indeks = kolumna

            while indeks < len(tekst):
                tekst_zaszyfrowany[kolumna] += tekst[indeks]

                indeks += klucz
        return "".join(tekst_zaszyfrowany)
    
    def deszyfrowanie(self, klucz, tekst_zaszyfrowany):
        liczba_kolumn=math.ceil(len(tekst_zaszyfrowany)/klucz)
        liczba_wierszy=klucz
        wykreslone_kratki=(liczba_kolumn*liczba_wierszy)-len(tekst_zaszyfrowany)
        tekst_odszyfrowany = [""]*liczba_kolumn
        kolumna=0
        wiersz=0

        for znak in tekst_zaszyfrowany:
            tekst_odszyfrowany[kolumna]+=znak
            kolumna+=1

            if (kolumna==liczba_kolumn) or (kolumna==liczba_kolumn-1 and wiersz>= liczba_wierszy-wykreslone_kratki):
                kolumna=0
                wiersz+=1

        return "".join(tekst_odszyfrowany)
