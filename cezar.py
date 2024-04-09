
class Cezar():
    def __init__(self):
        self.symbole = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def szyfrowanie(self, text_in, key):
        return self.cezar(text_in, key)

    def deszyfrowanie(self, text_in, key):
        return self.cezar(text_in, -key)

    def cezar(self, text_in, key):
        text_out = ""
        text_in=text_in.upper()
        for i in text_in:
            if i in self.symbole:
                index = self.symbole.find(i)
                index = (index + key) % len(self.symbole)
                text_out = text_out + self.symbole[index]
            else:
                text_out = text_out + i
        return text_out
