from cezar import Cezar
import time
teskt_zaszyfrowany="CPYLPOCXTYHOT YTHI CXTLXSDROCT SAP DROJ"
start=time.time()

for i in range(26):
    teskt_odszyfrowany = Cezar().deszyfrowanie(teskt_zaszyfrowany, i)
    print(f'{i} {teskt_odszyfrowany}')

stop=time.time()
czas=stop-start
print(f'Czas: {czas} s')