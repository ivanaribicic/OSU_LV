import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import load_model
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

#1.1
#skup za učenje sadrži 60000 primjera, a skup za testiranje sadriži 10000 primjera
#ulazna veličina je matrica 28*28, izlazna veličina je jedan broj

#1.2
# TODO: prikazi nekoliko slika iz train skupa
for i in range(3):
    plt.imshow(x_train[i])
    plt.title(y_train[i])
    plt.show()
    print(y_train[i])

# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)

x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

#1.3
# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu
model = keras.Sequential()
model.add(layers.Input(shape=(784, )))
model.add(layers.Dense(100, activation ='relu'))
model.add(layers.Dense(50, activation ='relu'))
model.add(layers.Dense(10, activation ='softmax'))
model.summary()

#1.4
# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(loss ='categorical_crossentropy',
optimizer ='adam',
metrics = ['accuracy',])

#1.5
# TODO: provedi ucenje mreze
batch_size = 32
epochs = 20

history = model.fit(x_train_s,
y_train_s,
batch_size = batch_size,
epochs = epochs,
validation_split = 0.1)

#1.6
score = model.evaluate(x_test_s, y_test_s, verbose=0)
print('Score')
print(score)

#1.7
# TODO: Prikazi test accuracy i matricu zabune
predictions = model.predict(x_test_s)
predict_class = np.argmax(predictions, axis=1)

print('Tocnost: ', accuracy_score(y_test, predict_class))
cm = confusion_matrix(y_test, predict_class)
disp = ConfusionMatrixDisplay(confusion_matrix(y_test, predict_class))
disp.plot()
plt.show()

#1.8
# TODO: spremi model
KERAS_MODEL_NAME = "Model/keras.hdf5"
keras.models.save_model(model, KERAS_MODEL_NAME)
del model
