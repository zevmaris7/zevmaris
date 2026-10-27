from math import pi
import calendar
from datetime import *
from calendar import *
tana=date.today()
print(f"Tere! \nTäna on {tana}")

# 27/12/2022
tana1 = tana.strftime("%d/%m/%Y")
print(f"Täna on {tana1}")

# December 27, 2022
tana2 = tana.strftime("%B %d, %Y")
print(f"Täna on {tana2}")

# 12/27/22
tana3 = tana.strftime("%m/%d/%y")
print(f"Täna on {tana3}")

# Dec-27-2022
tana4 = tana.strftime("%b-%d-%Y")
print(f"Täna on {tana4}")

# Ülesanne 1
# Omadused day, month, year kasutatakse päeva, kuu ja aasta parameetri leidmiseks date klassist.
# Arvuta mitu päeva on jäänud kuu lõpuni, aasta lõpuni.
# Arvuta oma vanus aastates, kuudes ja päevades.
print("Täna on", tana.day)
print("päev, kuu number on", tana.month)
print ("ja aasta on", tana.year)

kuulöpuni-monthrange(tana.year, tana.month)[1] - tana.day
# oktoobris on 31 päeva, 31-27=4 päeva jäänud
print("Kuu lõpuni on jäänud", kuulõpuni, "päeva.")
aastalöpuni=(date(tana.year, 12, 31) - tana). days
#date() -> 31.12.2026
#tana -> 27.10.2026
#days -> 65 päeva jäänud
print("Aasta lõpuni on jäänud", aastalõpuni, "päeva.")
sünnipäev=date(2010, 1, 7)
vanus=aastalõpuni//365
print("Oled", vanus, "aastat, "), 
print((aastalõpuni%365)//30, "kuud ja")
print((aaslõpuni%365)%30, "päeva vana.")

# Ülesanne 2
# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt ning lisa 
# ka selgitavad tekstid, et väljund oleks arusaadav.

print("3 + 8 / (4 - 2) * 4 = ", 3 + 8 / (4 - 2) * 4)
print("3 + 8 / 4 - 2 * 4 = ", 3 + 8 / 4 - 2 * 4)
print("(3 + 8) / 4 - 2 * 4 = ", (3 + 8) / 4 - 2 * 4)

# Ülesanne 3
# Ruudu sees asub ring. Ringi raadius on R.
# Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.

#Küsi kasutajalt sisendit raadisu kohta ja kasuta try-except plokki, et vältida vigu, kui kasutaja sisestab mitte-nimbri.

try:
    R= float(input("Sisesta ringi raadius: "))
    print("Ruudu pindala:", R**2)
    print("Ruudu ümbermõõt:", 4*R)
    print("Ringi pindala:"), pi*R**2)
    print("Ringi ümbermõõt:"), 2*pi*R)
except :
    print("Valeda andmed")

# Ülesanne 4
# Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu: 
# kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km.

# Algandmed (Maa raadius, mündi läbimõõt jne) omista programmi alguses sisukate nimedega muutujatele. Kuna ümbermõõdu 
# arvutamiseks tuleb kasutada  PI-d (3,14...), siis võid selle (umbkaudse) väärtuse otse programmi kirjutada.  
# Püüdke välja mõelda viise, kuidas juhuslikest vigadest valemis hoiduda (teisendamised, ümardamise täpsus jne). 
# Võimalusel võrrelge tulemusi teistega. Kui on erinevusi, leidke ühiselt põhjused.
# Kas programm on piisavalt hästi kirjutatud, et algandmete muutumise korral (näiteks juhul, 
# kui on vaja arvutada Marsi ümbermõõtu 1-eurostes müntides) on parandusi selge ja lihtne teha?


# Ülesanne 5
# Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
# kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll kill-koll
# kill-koll

# Saab kasutada muutujaid. Kuva iga sõna suure tähega.
a="Kill-koll"
b="Killadi-koll"
print(a.upper() * 3 + b.upper() + a. upper() * 3 + b.upper() + a. upper() * 3)

# Ülesanne 6
# Koosta programm, mis väljastaks järgmised laulusõnad suurte tähtedega:

print ("Rong see sõitis tsuhh tsuhh tsuhh,".upper())
print ("""piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.""".upper())



# ....Sisend, väljund, tingimus....

# Ülesanne 7
# Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.


