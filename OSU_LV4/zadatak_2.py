import sklearn.linear_model as lm
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error
from sklearn import metrics
import matplotlib.pyplot as plt

data = pd.read_csv('data_C02_emission.csv')

data = data.drop(['Make', 'Model'], axis=1)

ohe = OneHotEncoder()
X_encoded = ohe.fit_transform(data[['Fuel Type']]).toarray()

input_variables = ['Fuel Consumption City (L/100km)',
                   'Fuel Consumption Hwy (L/100km)',
                   'Fuel Consumption Comb (L/100km)',
                   'Fuel Consumption Comb (mpg)',
                   'Engine Size (L)',
                   'Cylinders',
                   'Fuel Type']

output_variable = ['CO2 Emissions (g/km)']
data['Fuel Type'] = X_encoded

X = data[input_variables].to_numpy()
y = data[output_variable].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)

linearModel = lm.LinearRegression()
linearModel.fit(X_train, y_train)

y_test_p = linearModel.predict(X_test)

print('Apsolutna pogreska: ', mean_absolute_error(y_test, y_test_p))
print('Apsolutna postotna pogreska: ',
      metrics.mean_absolute_percentage_error(y_test, y_test_p))
print('Apsolutna kvadratna pogreška: ', metrics.mean_squared_error(y_test, y_test_p))
print('Koeficijent determinacije: ', metrics.r2_score(y_test, y_test_p))

MAX_ERROR = metrics.max_error(y_test, y_test_p)

data["difference"] = abs(data['CO2 Emissions (g/km)'] - MAX_ERROR)
car = data[data["difference"] == data["difference"].max()]

print("Najveće odstupanje iznosi:", round(data["difference"].max(), 2), "g/km")
print("Najveće odstupanje je za automobil:")
print(car)

