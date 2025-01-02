import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def keyValidation(key):
    a = key[0][0]
    b = key[0][1]
    c = key[1][0]
    d = key[1][1]
    return (a*d) - (b*c) ==1

def encrypt(image,key):
    if not keyValidation(key):
        print('Matriks Salah')
        return None
    a = key[0][0]
    b = key[0][1]
    c = key[1][0]
    d = key[1][1]
    result = np.zeros_like(image)
    for i in range(0,image.shape[0]-1,2):
        for j in range(0,image.shape[1]):
            r1 = ((image[i,j,0] * a) + (image[i+1,j,0] * c)) % 256
            r2 = ((image[i,j,0] * b) + (image[i+1,j,0] * d)) % 256
            
            g1 = ((image[i,j,1] * a) + (image[i+1,j,1] * c)) % 256
            g2 = ((image[i,j,1] * b) + (image[i+1,j,1] * d)) % 256
            
            b1 = ((image[i,j,2] * a) + (image[i+1,j,2] * c)) % 256
            b2 = ((image[i,j,2] * b) + (image[i+1,j,2] * d)) % 256
            
            result[i,j,0] = r1
            result[i+1,j,0] = r2
            
            result[i,j,1] = g1
            result[i+1,j,1] = g2
            
            result[i,j,2] = b1
            result[i+1,j,2] = b2
    return result

def decrypt(image,key):
    if not keyValidation(key):
        print('Matriks Salah')
        return None
    d = key[0][0]
    b = 256- key[0][1]
    c = 256- key[1][0]
    a = key[1][1]
    result = np.zeros_like(image)
    for i in range(0,image.shape[0]-1,2):
        for j in range(0,image.shape[1]):
            r1 = ((image[i,j,0] * a) + (image[i+1,j,0] * c)) % 256
            r2 = ((image[i,j,0] * b) + (image[i+1,j,0] * d)) % 256
            
            g1 = ((image[i,j,1] * a) + (image[i+1,j,1] * c)) % 256
            g2 = ((image[i,j,1] * b) + (image[i+1,j,1] * d)) % 256
            
            b1 = ((image[i,j,2] * a) + (image[i+1,j,2] * c)) % 256
            b2 = ((image[i,j,2] * b) + (image[i+1,j,2] * d)) % 256
            
            result[i,j,0] = r1
            result[i+1,j,0] = r2
            
            result[i,j,1] = g1
            result[i+1,j,1] = g2
            
            result[i,j,2] = b1
            result[i+1,j,2] = b2
    return result

image = img.imread('image.jpg')
key = np.array([
    [5,3],
    [8,5]
])

enc = encrypt(image,key)
dec = decrypt(enc,key)

plt.figure(figsize=(15,15))
plt.subplot(1,3,1)
plt.imshow(image)
plt.subplot(1,3,2)
plt.imshow(enc)
plt.subplot(1,3,3)
plt.imshow(dec)

plt.show()

img.imsave('enc.jpg',enc)

img.imsave('dec.jpg',dec)





