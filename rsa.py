from pierwsze import Generowanie_liczb_pierwszych
import random


class RSA():
    def __init__(self, klucz_publiczny=None, klucz_prywatny=None, symbols=None, dlugosc_tekstu=None, długość_klucza=1024, wielkość_bloku=169):

        if klucz_publiczny is None and klucz_prywatny is None:
            self.generowanie_kluczy(długość_klucza)
        elif klucz_publiczny:
            self.n=klucz_publiczny[0]
            self.e=klucz_publiczny[1]
        elif klucz_prywatny:
            self.n=klucz_prywatny[0]
            self.d=klucz_prywatny[1]

        if symbols is None:
            self.symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,"
        else:
            self.symbols=symbols

        self.wielkość_bloku=wielkość_bloku
        self.dlugosc_tekstu=dlugosc_tekstu

    def generowanie_kluczy(self, długość_klucza):
        self.generator=Generowanie_liczb_pierwszych()
        p=self.generator.generowanie_liczb_pierwszych(długość_klucza)
        q=self.generator.generowanie_liczb_pierwszych(długość_klucza)
        self.n=p*q
        phi=self.phi(p,q)
        self.e=self.losuj_e(phi)
        self.d=self.oblicz_klucz_prywatny(self.e, phi)

    def phi(self, p, q):
        phi=(p - 1) * (q - 1)
        return phi
    
    def losuj_e(self, phi):
        while True:
            e=random.randint(2,phi-1)
            nwd=self.NWD(e, phi)
            if nwd == 1:
                return e
        
    def NWD(self,a,b):
        nwd=1
        if a > b:
            r=[b, a%b]
        else:
            r=[a, b%a]

        if r[1] == 0:
            nwd = r[0]
            return nwd
        
        i=1
        while True:
            r.append(r[i-1]%r[i])
            if r[i+1] == 0:
                nwd = r[i]
                return nwd
            else:
                i+=1


    def zamiana_tekstu_na_liczbe(self, tekst):
        for znak in tekst:
            if znak not in self.symbols:
                self.symbols+=znak

        bloki = []
        for blok in range(0, len(tekst), self.wielkość_bloku):
            liczba = 0
            for i in range(blok, min(blok+self.wielkość_bloku,len(tekst))):
                liczba +=(self.symbols.index(tekst[i])*(len(self.symbols))**(i%self.wielkość_bloku))
            bloki.append(liczba)

        return bloki
    
    def zamiana_liczby_na_tekst(self, bloki, dlugosc_tekstu):
        tekst = []
        dlugosc_blokow = []
        while dlugosc_tekstu > self.wielkość_bloku:
            dlugosc_blokow.append(self.wielkość_bloku)
            dlugosc_tekstu=dlugosc_tekstu-self.wielkość_bloku

        dlugosc_blokow.append(dlugosc_tekstu)

        j=0
        for blok in bloki:
            blok_tekstu = []
            dlugosc_bloku=dlugosc_blokow[j]
            j+=1
            for i in range(dlugosc_bloku-1,-1,-1):
                        indeks = blok // (len(self.symbols)**i)
                        blok = blok % (len(self.symbols)**i)
                        blok_tekstu.insert(0, self.symbols[indeks])
                            
            tekst.extend(blok_tekstu)

        return ''.join(tekst)
    
    def klucz_publiczny(self):
        return self.n , self.e 
    
    def oblicz_klucz_prywatny(self, e, phi):
        d = self.odwrotność_modulo(e, phi)
        return d
    
    def klucz_prywatny(self):
        return self.n, self.d
    
    def klucz_prywatny_d(self):
        return self.d
    
    
    def odwrotność_modulo(self, a, m):

        if self.NWD(a,m)!=1:
            return None
        
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 =0, 1, m

        while v3!=0:
            q=u3 // v3
            v1, v2,v3, u1, u2, u3 = (u1-q*v1), (u2-q*v2), (u3-q*v3), v1, v2, v3
        return u1%m
    
    def get_dlugosc_tekstu(self):
        return self.dlugosc_tekstu
    
    def get_symbole(self):
        return self.symbols
    
    def szyfrowanie_rsa(self, tekst):
        self.dlugosc_tekstu = len(tekst)
        n, e = self.klucz_publiczny()
        bloki = self.zamiana_tekstu_na_liczbe(tekst)
        tekst_zaszyfrowany = []
        for m in bloki:
            c=pow(m, e, n)
            tekst_zaszyfrowany.append(c)

        return tekst_zaszyfrowany
    
    def deszyfrowanie_rsa(self, tekst_zaszyfrowany):
        długość_tekstu=self.dlugosc_tekstu
        tekst_odszyfrowany = []
        n, d = self.klucz_prywatny()
        for c in tekst_zaszyfrowany:

            m=pow(c, d, n)
            tekst_odszyfrowany.append(m)
        
        return self.zamiana_liczby_na_tekst(tekst_odszyfrowany, długość_tekstu)
