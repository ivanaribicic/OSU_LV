import numpy as np
import matplotlib.pyplot as plt

white = np.zeros((50, 50))
black = np.ones((50, 50))


first_row = np.hstack((black, white))
second_row = np.hstack((white, black))

img = np.vstack((first_row, second_row))
print(img)

plt.figure()
plt.imshow(img, cmap="gray")
plt.show()