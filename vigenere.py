
class Vigenere():
    
    def konwertuj_klucz(self, key: str):
        klucz = []
        key = key.lower()

        for i in key:
            n = ord(i) - 97
            klucz.append(int(n))

        return klucz
    
    def szyfrowanie(self, tekst: str, key) -> str:
        tekst_zaszyfrowany = []
        j = 0
        klucz = self.konwertuj_klucz(key)

        for i in tekst:
            n = klucz[j]
            x = ord(i)
            # małe litery
            if x > 96 and x < 123:
                while x + n > 122:
                    x -= 26
                x += n
                j += 1
            # wielkie litery
            if x > 64 and x < 91:
                while x + n > 90:
                    x -= 26
                x += n
                j += 1
            # cyfry
            if x > 47 and x < 58:
                while x + n > 57:
                    x -= 10
                x += n
                j += 1

            tekst_zaszyfrowany.append(chr(x))
            if j >= len(key):
                j = 0

        return "".join(tekst_zaszyfrowany)

    def deszyfrowanie(self, tekst: str, key) -> str:
        tekst_odszyfrowany = []
        j = 0
        klucz = self.konwertuj_klucz(key)
        for i in tekst:
            n = klucz[j]
            x = ord(i)

            if x > 96 and x < 123:
                while x - n < 97:
                    x += 26
                x -= n
                j += 1
            if x > 64 and x < 91:
                while x - n < 65:
                    x += 26
                x -= n
                j += 1
            if x > 47 and x < 58:
                if x - n < 47:
                    x += 10
                x -= n
                j += 1

            tekst_odszyfrowany.append(chr(x))
            if j >= len(key):
                j = 0
        return "".join(tekst_odszyfrowany)
