import sklearn.linear_model as lm
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error
from sklearn import metrics

data = pd.read_csv('data_C02_emission.csv')

# a)
data = data.drop(['Make', 'Model'], axis=1)

input_variables = ['Fuel Consumption City (L/100km)',
                   'Fuel Consumption Hwy (L/100km)',
                   'Fuel Consumption Comb (L/100km)',
                   'Fuel Consumption Comb (mpg)',
                   'Engine Size (L)',
                   'Cylinders']

output_variable = ['CO2 Emissions (g/km)']
X = data[input_variables].to_numpy()
y = data[output_variable].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)

# b)
fuel_consumption_train = X_train[:,1]
fuel_consumption_test = X_test[:,1]

plt.scatter(fuel_consumption_train, y_train, c='blue', s=2)
plt.scatter(fuel_consumption_test, y_test, c='red', s=2)
plt.legend(['Training data', 'Test data'])
plt.show()

# c)
sc = StandardScaler()
X_train_n = pd.DataFrame(sc.fit_transform(X_train))
X_test_n = pd.DataFrame(sc.transform(X_test))

plt.hist(X_train[:,1], bins=15, color="blue")
plt.title('Prije skaliranja')
plt.show()

plt.hist(X_train_n[0], bins=15, color="red")
plt.title('Poslije skaliranja')
plt.show()

# d)
linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)
print('Parametri modela: ')
for i in range(len(linearModel.singular_)):
    print("theta", i, ":", round(linearModel.singular_[i], 5))

# e)
y_test_p = linearModel.predict(X_test_n)
plt.scatter(y_test, y_test_p, c='blue', s=2)
plt.xlabel("Stvarna vrijednost")
plt.ylabel("Izracunata vrijednost")
plt.show()

# f)
print('Apsolutna pogreska: ', mean_absolute_error(y_test, y_test_p))
print('Apsolutna postotna pogreska: ',
      metrics.mean_absolute_percentage_error(y_test, y_test_p))
print('Apsolutna kvadratna pogreška: ', metrics.mean_squared_error(y_test, y_test_p))
print('Koeficijent determinacije: ', metrics.r2_score(y_test, y_test_p))


