import numpy as np
import matplotlib.pyplot as plt
import statistics

data = np.loadtxt('data.csv', skiprows=1, delimiter=',')
print(data)

#a)
print('Mjerenja su izvrsena na ' + str(len(data)) + ' osoba')

#b)
plt.scatter(data[:,1], data[:,2])
plt.xlabel('visina [cm]')
plt.ylabel('masa [kg]')
plt.title('Odnos mase i visine')
plt.show()

#c)
height = data[:,1]
weight = data[:,2]
plt.scatter(weight[::50], height[::50])
plt.xlabel('visina [cm]')
plt.ylabel('masa [kg]')
plt.title('Odnos mase i visine za svaku pedesetu osobu')
plt.show()

#d)
print('Minimalna vrijednost visine ' + str(np.min(data[:,1])))
print('Maksimalna vrijednost visine ' + str(height.max()))
print('Srednja vrijednost visine ' + str(np.mean(data[:,1])))

#e) muškarci
males = []
for person in data:
    if person[0] == 1:
        males.append(person[1])

print('Minimalna vrijednost visine muskaraca ' + str(min(males)))
print('Maksimalna vrijednost visine muskaraca ' + str(max(males)))
print('Srednja vrijednost visine muskaraca ' + str(statistics.mean(males)))

#e) žene
females = []
for person in data:
    if person[0] == 0:
        females.append(person[1])

print('Minimalna vrijednost visine zena ' + str(min(females)))
print('Maksimalna vrijednost visine zena ' + str(max(females)))
print('Srednja vrijednost visine zena ' + str(statistics.mean(females)))

