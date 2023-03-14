import statistics
numbers = []
user_input = ""
print("Unesite broj: ")

while True:
    user_input = input()
    if user_input == "Done":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except:
        print("Unešena vrijednost nije broj.")

average = statistics.mean(numbers)

print("Korisnik je unio: " + str(len(numbers)) + " brojeva")
print("Srednja vrijednost brojeva: " + str(average))
print("Minimalna vrijednost: " + str(min(numbers)))
print("Maksimalna vrijednost: " + str(max(numbers)))

numbers.sort()
print(numbers)
    
