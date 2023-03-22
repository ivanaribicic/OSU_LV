import pandas as pd
data = pd.read_csv('data_C02_emission.csv')

print('----------------a)----------------')
#a)
print('Broj mjerenja: '  + str(len(data)))
print('Tip velicina: ' + str(data.info()))

print(data.isnull().sum())
data.dropna(axis=0)
data.dropna(axis=1)
data.drop_duplicates()
data = data.reset_index(drop=True)

cols = ['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']
data[cols] = data[cols].astype('category')
print(data.info())

print('---------------b)-----------------')
#b)
sorted_data = data.sort_values(by = ['Fuel Consumption City (L/100km)'], ascending= False)
print(sorted_data[['Make', 'Model', 'Fuel Consumption City (L/100km)']].head(3))
print(sorted_data[['Make', 'Model', 'Fuel Consumption City (L/100km)']].tail(3))

print('-----------------c)---------------')
#c)
cars = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5 )]
print('Broj vozila: ', len(cars))
print('Prosjecna emisija CO2: ', cars['CO2 Emissions (g/km)'].mean())

print('----------------d)----------------')
#d)
audi = (data[data.Make == 'Audi'])
print('Broj mjerenja za vozila proizvodjaca Audi: ' + str(len(audi)))
audi4 = audi[(audi['Cylinders'] == 4)] 
print('Prosjecna emisija CO2 za Audi s 4 cilindra: ', audi4['CO2 Emissions (g/km)'].mean())

print('----------------e)----------------')
#e)
even_cylinders = data[(data['Cylinders'] % 2 == 0)]
print('Broj autobomila s parnim brojem cilindara: ', len(even_cylinders))
cylinders4 = even_cylinders[(even_cylinders['Cylinders'] == 4)]
print('Prosjecna emisija CO2 za automobile s 4 cilindra: ', cylinders4['CO2 Emissions (g/km)'].mean())
cylinders6 = even_cylinders[(even_cylinders['Cylinders'] == 6)]
print('Prosjecna emisija CO2 za automobile sa 6 cilindara: ', cylinders6['CO2 Emissions (g/km)'].mean())
cylinders8 = even_cylinders[(even_cylinders['Cylinders'] == 8)]
print('Prosjecna emisija CO2 za automobile s 8 cilindara: ', cylinders8['CO2 Emissions (g/km)'].mean())
cylinders10 = even_cylinders[(even_cylinders['Cylinders'] == 10)]
print('Prosjecna emisija CO2 za automobile s 10 cilindara: ', cylinders10['CO2 Emissions (g/km)'].mean())
cylinders12 = even_cylinders[(even_cylinders['Cylinders'] == 12)]
print('Prosjecna emisija CO2 za automobile s 12 cilindara: ', cylinders12['CO2 Emissions (g/km)'].mean())
cylinders16 = even_cylinders[(even_cylinders['Cylinders'] == 16)]
print('Prosjecna emisija CO2 za automobile s 16 cilindara: ', cylinders16['CO2 Emissions (g/km)'].mean())

print('----------------f)----------------')
#f)
diesel = data[data['Fuel Type'] == 'D']
print('Prosjecna gradska potrosnja vozila koja koriste dizel: ', diesel['Fuel Consumption City (L/100km)'].mean())
print('Medijalna vrijednost za vozila koja koriste dizel', diesel['Fuel Consumption City (L/100km)'].median())
gasoline = data[data['Fuel Type'] == 'X']
print('Prosjecna gradska potrosnja vozila koja koriste regularni benzin: ', gasoline['Fuel Consumption City (L/100km)'].mean())
print('Medijalna vrijednost za vozila koja koriste regularni benzin', gasoline['Fuel Consumption City (L/100km)'].median())

print('--------------g)------------------')
#g)
diesel4 = diesel[(diesel['Cylinders'] == 4)] 
sorted_diesel4 = diesel4.sort_values(by = ['Fuel Consumption City (L/100km)'], ascending= False)
print('Vozilo s 4 cilindra koje koristi dizel s najvecom gradskom potrosnjom: ', diesel4.head(1))

print('----------------h)----------------')
#h)
manual = data[(data['Transmission'].str.contains('M'))]
print('Broj vozila s rucnim tipom mjenjaca: ', len(manual))

print('----------------i)----------------')
#i)
print('Korelacija: ', data.corr(numeric_only=True))