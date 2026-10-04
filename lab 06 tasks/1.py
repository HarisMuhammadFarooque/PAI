import numpy as np

np.random.seed(42)
marks = np.random.randint(30, 100, size=(10, 5))

print("------ Each Student's average and total ------ ")
print(f"Mean: {np.mean(marks, axis=1)}\nTotal: {np.sum(marks, axis=1)}")

print("------ Each Subject's average and total ------ ")
print(f"Mean: {np.mean(marks, axis=0)}\nTotal: {np.sum(marks, axis=0)}")

std_avg = np.mean(marks, axis=1)
print(f"\nStudent with highest average marks: {std_avg.argmax() + 1}") 

result = np.where(std_avg >= 50, 'Pass', 'Fail')
count = np.sum(result == 'Pass')

print(f'Result(Students): {result}\nCount of passed Students: {count}')
