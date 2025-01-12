#test obciążeniowy
import time
import requests

url = "https://www.facebook.com/"

def send_requests():
    response = requests.get(url)
    return response.status_code
print("Rozpo test, wysylamy ile zapytan wysylac do api")

start_time = time.time()
for i in range(10):
    status = send_requests()
    print(f"Zapytanie numer {i + 1}: status: {status}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"suma czasu dla 10 zapytań {elapsed_time} sekund")