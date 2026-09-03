import requests

antwort = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true")
print(antwort.status_code)
print(antwort.text)
daten = antwort.json()
temperatur = daten["current_weather"]["temperature"]
wind = daten["current_weather"]["windspeed"]

print(f"Aktuelle Temperatur in Berlin: {temperatur}°C")
print(f"Windgeschwindigkeit: {wind} km/h")