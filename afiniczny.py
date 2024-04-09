class Afiniczny:
    def __init__(self):
        self.symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,"
        self.N=len(self.symbols)

    def get_N(self):
        return self.N
    
    def szyfrowanie(self, a, b, tekst):
        
        tekst_zaszyfrowany=''
        for znak in tekst:
            if znak in self.symbols:
                indeks=self.symbols.find(znak)
                tekst_zaszyfrowany+=self.symbols[(indeks*a + b)%self.N]
            else:
                tekst_zaszyfrowany+=znak

        return tekst_zaszyfrowany

    def deszyfrowanie(self, a, b, tekst_zaszyfrowany):
        tekst_odszyfrowany=''
        odw_a=self.odwrotność_modulo(a,self.N)

        for znak in tekst_zaszyfrowany:
            if znak in self.symbols:
                indeks=self.symbols.find(znak)
                tekst_odszyfrowany+=self.symbols[(indeks - b)*odw_a%self.N]
            else:
                tekst_odszyfrowany+=znak
        return tekst_odszyfrowany

    def odwrotność_modulo(self, a, N):

        if self.NWD(a,N)!=1:
            return None
        
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 =0, 1, N

        while v3!=0:
            q=u3 // v3
            v1, v2,v3, u1, u2, u3 = (u1-q*v1), (u2-q*v2), (u3-q*v3), v1, v2, v3

        return u1%N

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
