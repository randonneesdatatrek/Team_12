#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Actions performed with the help of the Tutorial
#from https://scikit-image.org/docs/stable/auto_examples/applications/plot_coins_segmentation.html

import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from skimage import io
from skimage.feature import canny
from skimage.util import compare_images
import os

test = os.getcwd()
print(test)
os.chdir('C:\\Users\\Basile PC\\Desktop\\Python\\Test Slik')
image = io.imread("Slik GFP-z31.tif")
#Edge based segmentation

edge_roberts = filters.roberts(image)
edge_sobel = filters.sobel(image)
edge_canny = canny(image/255.)
edge_canny1 = canny(image/255., sigma=2)
edge_canny2 = canny(image/255., sigma=2.5)
edge_canny3 = canny(image/255., sigma=3)

fig, axes = plt.subplots(ncols=3, nrows=2, sharex=True, sharey=True,
                         figsize=(20, 6))

axes[0,0].imshow(edge_roberts, cmap=plt.cm.gray)
axes[0,0].set_title('Roberts Edge Detection')

axes[0,1].imshow(edge_sobel, cmap=plt.cm.gray)
axes[0,1].set_title('Sobel Edge Detection')

axes[0,2].imshow(edge_canny, cmap=plt.cm.gray)
axes[0,2].set_title('Canny Edge Detection')

axes[1,0].imshow(edge_canny1, cmap=plt.cm.gray)
axes[1,0].set_title('Canny Edge Detection, Sigma=2')

axes[1,1].imshow(edge_canny2, cmap=plt.cm.gray)
axes[1,1].set_title('Canny Edge Detection, Sigma=2.5')

axes[1,2].imshow(edge_canny3, cmap=plt.cm.gray)
axes[1,2].set_title('Canny Edge Detection, Sigma=3')


print('Edge based segmentation')
plt.tight_layout()
plt.show()


# In[2]:


#Test removal of small objects
from scipy import ndimage as ndi
fill_Cell = ndi.binary_fill_holes(edge_canny)
label_objects, nb_labels = ndi.label(fill_Cell)
sizes = np.bincount(label_objects.ravel())
mask_sizes = sizes > 20
mask_sizes[0] = 0
Cell_cleaned = mask_sizes[label_objects]


# In[3]:


fig, axes = plt.subplots(ncols=2, sharex=True, sharey=True,
                         figsize=(20, 6))
print('Removal of small objects after Canny filtering')
axes[0].imshow(fill_Cell, cmap=plt.cm.gray)
axes[1].imshow(Cell_cleaned, cmap=plt.cm.gray)
axes[1].set_title('Fill_Cell cleaned')


# In[4]:


#Region based segmentation
print('Test region based segmentation')

from skimage.filters import sobel
elevation_map = sobel(image)
fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(elevation_map, cmap=plt.cm.gray)
ax.set_title('elevation map')
ax.axis('off')


# In[11]:


from skimage import segmentation
markers = np.zeros_like(image)
markers[image < 600] = 2
markers[image > 1000] = 1
fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(markers, cmap=plt.cm.nipy_spectral)
ax.set_title('markers')
ax.axis('off')


# In[34]:


segmentation_sobel = segmentation.watershed(elevation_map, markers)

fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(segmentation_sobel, cmap=plt.cm.gray)
ax.set_title('segmentation')
ax.axis('off')


# In[35]:


#Last method segmentation
from skimage.color import label2rgb
segmentation_sobel = segmentation.watershed(elevation_map, markers)

segmentation_sobel = ndi.binary_fill_holes(segmentation_sobel - 2)
labeled_cell, _ = ndi.label(segmentation_sobel)
image_label_overlay = label2rgb(labeled_cell, image=image, bg_label=0)

fig, axes = plt.subplots(1, 2, figsize=(20, 6), sharey=True)
axes[0].imshow(image, cmap=plt.cm.gray)
axes[0].contour(segmentation_sobel, [0.5], linewidths=1.2, colors='y')
axes[1].imshow(image_label_overlay)

for a in axes:
    a.axis('off')

plt.tight_layout()

plt.show()


# In[19]:


help(contour)


# In[ ]:




