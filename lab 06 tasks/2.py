import numpy as np

np.random.seed(42)
model = np.random.rand(10, 4) * 100
print(model)

mean = model.mean(axis=0)
std_dev = model.std(axis=0)
print(f'Feature Mean: {mean}\nStandard Deviation: {std_dev}')

z = (model - mean)/std_dev
print("Standardized Mean:", z.mean(axis=0))
print("Standardized Std:", z.std(axis=0))
