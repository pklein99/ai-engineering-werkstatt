import json

with open("kunden.json", "r", encoding="utf-8") as datei:
    kunden = json.load(datei)

print(f"Anzahl Kunden: {len(kunden)}")
print(kunden[0])
kunden_essen = []
for kunde in kunden:
    if kunde["stadt"] == "Essen":
        kunden_essen.append(kunde)

print(f"Kunden aus Essen: {len(kunden_essen)}")

with open("kunden_essen.json", "w", encoding="utf-8") as datei:
    json.dump(kunden_essen, datei, ensure_ascii=False, indent=2)