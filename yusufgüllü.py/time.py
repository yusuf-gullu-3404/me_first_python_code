import time 

zaman = time.ctime()
print(zaman)


import time

zaman2 = time.strftime("%Y,%B,%A,%d")
print(zaman2)

zaman3 = time.asctime()
print(zaman3)

import time

while True:
    saat = time.strftime("%H:%M:%S")
    print(saat)
    time.sleep(1)  # 1 saniye bekle
