import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
from skimage import io, color

img = io.imread("609db0b0a906d09f9f805d5e9f98622a.jpg")
img_gray = color.rgb2gray(img) if len(img.shape)==3 else img

dct_img = dct(dct(img_gray.T, norm='ortho').T, norm='ortho')
threshold = np.percentile(np.abs(dct_img), 50)
dct_compressed = dct_img * (np.abs(dct_img)>=threshold)
reconstructed = idct(idct(dct_compressed.T, norm='ortho').T, norm='ortho')

plt.subplot(1,2,1); plt.imshow(img_gray,cmap='gray'); plt.title("Gốc"); plt.axis('off')
plt.subplot(1,2,2); plt.imshow(reconstructed,cmap='gray'); plt.title("Nén"); plt.axis('off')
plt.show()
