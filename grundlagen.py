# Variable
name = "Paul"
alter = 12

# Liste
fahrzeuge = ["Auto", "Zug", "Fahrrad", "Flugzeug", "Boot"]

# Schleife: geht jedes Element der Liste einzeln durch
for fahrzeug in fahrzeuge:
    print(f"{fahrzeug} hat {len(fahrzeug)} Buchstaben.")

# Bedingung (if/else)
if alter >= 18:
    print("volljährig")
else:
    print("minderjährig")

# Funktion: wiederverwendbarer Codeblock mit Eingabe und Rückgabewert
def verdopple(zahl):
    return zahl * 2

ergebnis = verdopple(21)
print(f"21 verdoppelt ist {ergebnis}")
def ist_lang(wort):
    return len(wort) > 4

print(ist_lang("Auto"))
print(ist_lang("Fahrrad"))

for fahrzeug in fahrzeuge:
    if ist_lang(fahrzeug):
        print(fahrzeug)