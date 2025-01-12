import time #uzywamy modulu time. Pomaga mierzyc uply czas

def slow_function(): #definicja funkcji
 print("Rozpo dzial slow_function...") 
time.sleep(3) #uśpienie programu na x sek
print("Zak dzial slow_function.")

print("Zacz pom czas")
start_time = time.time() #pobieranie aktualn czasu w sek 

slow_function() #wywołanie funkcji

end_time = time.time() #to samo co linijka 9

elapsed_time = end_time - start_time #odejmujemy 2 czasy zeby dowiedziec sie ile czasu minelo od wywolania do zakonczenia
print(f"Funkcja wyk sie w czasie {elapsed_time} sekund") #f string 