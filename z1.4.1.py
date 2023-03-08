print("Unesite broj radnih sati: ")
work_hours = int(input())
print("Unesite koliko ste plaćeni po satu: ")
pay = float(input())
income = work_hours*pay

print(income)

def total_euro(work_hours, pay):
    income = work_hours*pay
    print("Ukupni iznos: " + str(income) + "eura")

total_euro(work_hours, pay)

