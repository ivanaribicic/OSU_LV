import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import load_model
from matplotlib import pyplot as plt
from sklearn.preprocessing import OneHotEncoder

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

KERAS_MODEL_NAME = "Model/keras.hdf5"
model = keras.models.load_model(KERAS_MODEL_NAME)

x_test_reshaped = np.reshape(x_test, (len(x_test), x_test.shape[1]*x_test.shape[2]))
y_test = OneHotEncoder().fit_transform(np.reshape(y_test, (-1, 1))).toarray()

y_pred = model.predict(x_test_reshaped)
y_pred = np.argmax(y_pred, axis=1)

y_test = np.argmax(y_test, axis=1)

print(y_test.shape, y_pred.shape)
y_bool = y_test == y_pred
print(y_bool, y_bool.shape)

indexes = np.where(y_bool==False)

for i in range(1, 8):
    plt.imshow(x_test[indexes[0][i]])
    title = f"Stvarna klasa: {y_test[indexes[0][i]]}, Predikcija: {y_pred[indexes[0][i]]}" 
    plt.title(title)
    plt.show()

