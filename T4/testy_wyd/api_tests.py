import requests #import biblioteki 

url = "https://www.facebook.com/" #podajemy str

print("Wysyl zapytanie GET do:", url)

response = requests.get(url) #zapytanie pobrania danych

print("Otrzym odp o statusie:", response.status_code)

if response.status_code == 200: #sprawdz status code
    #jesli status to 200 widzimi zwrot
    data = response.json()
    print("Zaw strony to:", data)
else:
    print("Nie udalo sie pobrac danych API")