import math
import random
import time
class Generowanie_liczb_pierwszych():
    def __init__(self):
        self.liczby_pierwsze=self.sito_Eratostenesa(1000)

    def generowanie_liczb_pierwszych(self,długość_klucza):
        
        while True:
            liczba=random.randint(2**(długość_klucza-1),2**(długość_klucza))
            if self.czy_to_liczba_pierwsza(liczba)== True:
                return liczba

    def czy_to_liczba_pierwsza(self,liczba):
        if liczba<2:
            return False
        
        for i in self.liczby_pierwsze:
            if liczba == i:
                return True
            if liczba % i == 0:
                return False
        
        wynik=self.test_Rabina_Millera(liczba)
        if wynik == False:
            return False
        
        return True


    def sito_Eratostenesa(self,n):
        liczby_pierwsze = []
        czy_pierwsze=[True for x in range(n+1)]
        m=math.ceil(math.sqrt(n))+1
        for i in range(2,m):
            if czy_pierwsze[i]==True:
                for j in range(i*i,n+1,i):
                    czy_pierwsze[j]=False

        for i in range(2,n):
            if czy_pierwsze[i]==True:
                liczby_pierwsze.append(i)

        return liczby_pierwsze
    

    def test_Rabina_Millera(self,liczba):

        n=liczba-1
        s=0
        t=n
        while t == 0:
            if n%2 == 0:
                s+=1
                n=n/2
            else:       
                t=int(n)
        
        wynik=self.testRM(s,t, liczba)
        
        if wynik==False:
            return False
        
        return True

    def testRM(self,s,t, liczba):
        for i in range(5):
            bc=random.randint(2,liczba-2)
            a=pow(bc,t,liczba)
            if a == 1 or a == liczba-1:
                return True

            for r in range(2,s-1):

                a=a**2&liczba
                if a == 1:
                    return False
                if a == -1 or a == liczba-1:  
                    return True
            
        return False
    