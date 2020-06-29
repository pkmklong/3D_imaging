import pydicom
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt


dcm = pydicom.dcmread("../datasets/image1.dcm")

print(f"Modality: {dcm.Modality}")

pixels = np.copy(dcm.pixel_array)
print(f"min: {np.min(pixels)}, max: {np.max(pixels)}")

wc = 2472
ww = 4144

hu_min = wc - ww/2
hu_max = wc + ww/2

pixels[np.where(pixels < hu_min)] = hu_min
pixels[np.where(pixels > hu_max)] = hu_max
pixels = (pixels - hu_min)/(hu_max - hu_min)

plt.imshow(pixels, cmap = "gray")

print(f"min: {np.min(pixels)}, max: {np.max(pixels)}")

out = (pixels*0xff).astype(np.uint8)
im = Image.fromarray(out, mode="L")
im.save("out.png")
