# Klucz publiczny
n=847470401 
e=814989661
#klucz prywatny
d=528300841
#tekst jawny
m=171800
#szyfrowanie
c=pow(m, e, n)
print(c)
#deszyfrowanie
m=pow(c, d, n)
print(m)