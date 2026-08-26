#question 1
weight = int(input("Enter Weight: "))
height = int(input("Enter Height: "))

bmi = weight/height*2
print(f"BMI of User: {bmi}")


#question 2
print("1. Add\n 2. Subtract\n 3. Multiply\n 4. divide\n")
choice = int(input("Enter Your Choice: "))

a = int(input("Enter first No.: "))
b = int(input("Enter Second No.: "))

def add(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

if(choice == 1):
    print("Answer: ", add(a, b))
elif(choice == 2):
    print("Answer: ", a - b)
elif(choice == 3):
    print("Answer: ", a*b)
elif(choice == 4):
    if(b == 0):
        print("Division with zero not allowed!")
    else:
        print("Answer: ", a/b)
else:
    print("Invalid Choice!")


#question 3: 
size = int(input("Enter Size: "))
list1 = []
count = 0

for i in range(size):
    num = int(input("Enter no.: "))
    list1.append(num)
    if(num % 2 == 0):
        count += 1

print(f"List: {list1}, Even Count: {count}")


#question 4: 
size = int(input("Enter Size: "))
list1 = []

for i in range(size):
    list1.append(int(input(f"Enter element {i + 1}: ")))

total = sum(list1)
print(f"List: {list1}")
print(f"Sum of elements: {total}")


#question 5: 
size = int(input("Enter Size: "))
list1 = []

for i in range(size):
    list1.append(int(input(f"Enter element {i + 1}: ")))

n = int(input("Enter the number: "))

list1 = [num for num in list1 if num >= n]

print(f"List after deletion: {list1}")


#question 6: 
subjects = ["Physics", "Chemistry", "Maths"]
marks = {}

for subject in subjects:
    marks[subject] = float(input(f"Enter marks for {subject}: "))

average = sum(marks.values()) / len(marks)
highest_subject = max(marks, key=marks.get)

print("\nMarks Dictionary:", marks)
print(f"Average Marks: {average:.2f}")
print(f"Highest Marks in: {highest_subject} ({marks[highest_subject]})")


#question 7:
word = input("Enter a word: ")
reversed_word = ""

for ch in word:
    reversed_word = ch + reversed_word

print("Reversed word:", reversed_word)


#question 8: 
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#question 9: 
num = int(input("Input a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#question 10: g
n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    val = int(input(f"Enter number {i+1}: "))
    numbers.append(val)

print("The list is:", numbers)
print("Largest number is:", max(numbers))


#question 11: 
marks2 = {}
marks2["Subject1"] = float(input("Enter marks for Subject 1: "))
marks2["Subject2"] = float(input("Enter marks for Subject 2: "))
marks2["Subject3"] = float(input("Enter marks for Subject 3: "))

total_marks = sum(marks2.values())
average_marks = total_marks / len(marks2)
percentage = (total_marks / (len(marks2) * 100)) * 100   

print("\nMarks Dictionary:", marks2)
print(f"Total Marks: {total_marks}")
print(f"Average: {average_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")


#question 12:
squares = {}

for i in range(1, 16):
    squares[i] = i ** 2

print("Dictionary of squares:", squares)
