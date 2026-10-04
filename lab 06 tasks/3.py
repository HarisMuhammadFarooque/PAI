import numpy as np

np.random.seed(42)
image = np.random.randint(0, 256, size=(3, 3))
print(image)

max_intensity = np.max(image)
min_intensity = np.min(image)
mean_intensity = np.mean(image)

print(f'Maximum Intensity: {max_intensity}\nMinimum Intensity: {min_intensity}\nMean: {mean_intensity}')

threshold = 100
mask = image > threshold
threshold_image = np.where(mask, 1, 0)

print("Binary Mask:\n", mask)
print(f'Thresholded Image: {threshold_image}')