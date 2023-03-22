import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data_C02_emission.csv')

#a)
plt.hist(data["CO2 Emissions (g/km)"], bins=50, histtype='stepfilled', color='steelblue', edgecolor='black')
plt.xlabel("CO2 emisija")
plt.ylabel("Broj automobila")
plt.show()

#b)
colors = { 'X': 'blue', 'Z': 'green', 'D': 'red', 'E': 'orange', 'N': 'black' }
data.plot.scatter(x='Fuel Consumption City (L/100km)',
                    y='CO2 Emissions (g/km)',
                    c=data['Fuel Type'].apply(lambda x: colors[x]), cmap ="hot", s=10)
plt.xlabel('Gradska potrošnja goriva')
plt.ylabel('CO2 emisija')
plt.show()

#c)
grouped_fuel_type = data.groupby('Fuel Type')

grouped_fuel_type.boxplot(column=['Fuel Consumption Hwy (L/100km)'])
plt.show()

#d)
grouped_fuel_type['Make'].count().plot(kind="bar")
plt.xlabel('Tip goriva')
plt.ylabel("Broj vozila")
plt.show()

#e)
grouped_cylinders = data.groupby("Cylinders").mean()
grouped_cylinders["CO2 Emissions (g/km)"].plot(kind="bar")
plt.xlabel('Broj cilindara')
plt.ylabel("CO2 emisija")
plt.show()
