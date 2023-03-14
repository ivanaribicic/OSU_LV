import numpy as np
import matplotlib.pyplot as plt

img = plt.imread ("road.jpg")
img = img[ :,:,0].copy()
print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img, cmap ="gray")
plt.title('Original')
plt.show()

#a)
plt.figure()
plt.imshow(img, cmap = "gray", alpha = 0.5)
plt.title('Posvijetljeno')
plt.show()

#b)
a = img.shape[1]
img4 = img[:, int(a/4): int(a/2)]

plt.figure()
plt.imshow(img4, cmap="gray")
plt.title("Druga četvrtina")
plt.show()

#c)
plt.figure()
rotate_img = np.rot90(img)
rotate_img = np.rot90(rotate_img)
rotate_img = np.rot90(rotate_img)
plt.imshow(rotate_img, cmap = "gray")
plt.title('Rotirano')
plt.show()

#d)
plt.figure()
flipped_img = np.fliplr(img)
plt.imshow(flipped_img, cmap = "gray")
plt.title('Zrcaljeno')
plt.show()
