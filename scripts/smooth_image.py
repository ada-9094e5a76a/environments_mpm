try:
    from envtest import smooth_image
except ImportError:
    from skimage.filters import gaussian

    def smooth_image(image, sigma):
        return gaussian(image, sigma=sigma, mode="nearest", preserve_range=True)

from skimage import data
import matplotlib.pyplot as plt


image = data.camera()
sigma = 5

smoothed_image = smooth_image(image, sigma)

f = plt.figure()
f.add_subplot(1, 2, 1)
plt.imshow(image)
f.add_subplot(1, 2, 2)
plt.imshow(smoothed_image)
plt.show(block=True)