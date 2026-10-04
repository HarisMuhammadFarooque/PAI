import numpy as np

arr = np.array([10, 21, 35, np.nan, 50, np.nan])
has_Nan = np.isnan(arr)

mean = np.nanmean(arr)
median = np.nanmedian(arr)
total = np.nansum(arr)
std = np.nanstd(arr)

print('\n------- Nan-aware Statistics -------')
print(f'Mean: {mean}\nMedian: {median}\nSum: {total}\nStandard deviation: {std}')

idx = np.argwhere(has_Nan == True)
arr[idx] = mean

print('\n------- Nan-Removed Array (replaced with mean) -------')
print(arr)