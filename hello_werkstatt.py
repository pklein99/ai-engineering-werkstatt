import random
from datetime import date

heute = date.today()
print(f"Heute ist der {heute}.")

with open("LOGBUCH.md", "r", encoding="utf-8") as datei:
    zeilen = datei.readlines()

zeilen = [z.strip() for z in zeilen if z.strip()]
zufallszeile = random.choice(zeilen)
print(f"Zufällige Zeile aus deinem Logbuch: {zufallszeile}")