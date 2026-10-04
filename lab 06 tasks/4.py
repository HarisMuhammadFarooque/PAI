import numpy as np

np.random.seed(42)
sensors = 4
time_points = 6

print('-------- Per sensor Readings ----------')
sensor_readings = np.random.randint(0, 51, size=(sensors, time_points))
print(sensor_readings)

print('-------- Per sensor Mean, Min, Max, and std ----------')
print(f'\nMean: {sensor_readings.mean(axis=1)}\nMaximum: {sensor_readings.max(axis=1)}')
print(f'Minimum: {sensor_readings.min(axis=1)}\nStandard deviation: {sensor_readings.std(axis=1)}')

avg = sensor_readings.mean(axis=1)
print(f'Highest Average Sensor: {np.argmax(avg) + 1}')

threshold = int(input('Enter Threshold: '))
mask = sensor_readings > threshold

print("Mask:\n", mask)
print("Readings above threshold:", sensor_readings[mask])
print("Count:", mask.sum())

for s, t in np.argwhere(mask):
    print(f"Sensor {s + 1}, Time {t + 1}: {sensor_readings[s, t]}")