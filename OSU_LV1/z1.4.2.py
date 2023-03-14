print("Unesite broj između 0.0 i 1.0: ")

try:
    number = float(input())
except : 
    print("Uneseni podatak nije broj")

if number < 0.0 or number > 1.0:
    print("Broj se ne nalazi u zadanom intervalu.")
elif number >= 0.9:
    print("A")
elif number >= 0.8:
    print("B")
elif number >= 0.7:
    print("C")
elif number >= 0.6:
    print("D")
else:
    print("F")
