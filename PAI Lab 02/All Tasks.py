Products = {
    101 : {"Name" : "HP Elitebook", "Category" : "Laptop", "Price" : 34000, "Quantity" : 4},
    102 : {"Name" : "HP Probook", "Category" : "Laptop", "Price" : 44000, "Quantity" : 0},
    103 : {"Name" : "Dell Latitude", "Category" : "Laptop", "Price" : 64000, "Quantity" : 2}
}

def productLookup(products, id):
    if id in products:
        print("------ Product Found! --------")
        print(products[id])
    else:
        print("Product Not Found!")

def updatePrice(products, id, newPrice):
    if id in products:
        products[id]["Price"] = newPrice
    else:
        print("Product Not Found!")

def updateStock(products, id, newStock):
    if id in products:
        products[id]["Quantity"] = newStock
    else:
        print("Product Not Found!")

def getOutOfStockProducts(Products):
    return [id for id in Products if Products[id]["Quantity"] == 0]



transactionIDs = []
print("-------- Enter Transaction IDs, enter -1 to stop! --------")

while(True):
    num = int(input("Enter ID: "))
    if(num == -1):
        break
    transactionIDs.append(num)

uniqueIDs = set(transactionIDs)
print(f"All Transaction IDs: {transactionIDs}")
print(f"Unique IDs: {uniqueIDs}")




courseA = set()
courseB = set()

n = int(input("Enter number of students in Course A: "))
print("Enter Course A student IDs:")
for _ in range(n):
    courseA.add(int(input()))

m = int(input("Enter number of students in Course B: "))
print("Enter Course B student IDs:")
for _ in range(m):
    courseB.add(int(input()))

bothCourses = courseA & courseB      
onlyA = courseA - courseB            
onlyB = courseB - courseA            
allStudents = courseA | courseB      

print(f"\nEnrolled in both courses: {bothCourses}")
print(f"Enrolled only in Course A: {onlyA}")
print(f"Enrolled only in Course B: {onlyB}")
print(f"All unique students: {allStudents}")




employees = {
    101 : {"Name" : "Haris", "Dept" : "CS", "Salary" : 104000, "Job Title" : "AI engineer"},
    102 : {"Name" : "Ali", "Dept" : "AI", "Salary" : 134000, "Job Title" : "ML engineer"},
    103 : {"Name" : "Ayaan", "Dept" : "SE", "Salary" : 114000, "Job Title" : "Software engineer"}
}

def searchEmployee(employees, id):
    if id in employees:
        print(f"Id Found! Employee Details: {employees[id]}")
    else:
        print("Employee not Found!")

def updateSalary(employees, id, newSalary):
    if id in employees:
        employees[id]["Salary"] = newSalary
        print(f"Salary Updated! Employee Details: {employees[id]}")
    else:
        print("Employee not Found!")

def addNewEmployee(employees, id, salary, name, dept, title):
    if id in employees:
        print(f"Employee ID {id} already exists!")
        return
    employees[id] = {"Name": name, "Dept": dept, "Salary": salary, "Job Title": title}
    print("Record Added!")

def removeEmployee(employees, id):
    if id in employees:
        del employees[id]
        print("Employee removed!")
    else:
        print("Employee not Found!")




logs = ["INFO", "ERROR", "WARNING", "INFO", "ERROR", "INFO"]

def analyzeLogs(logs):
    counts = {}
    for log in logs:
        counts[log] = counts.get(log, 0) + 1
    types = list(counts.keys())
    mostFrequent = max(counts.items(), key=lambda item: item[1])
    return counts, types, mostFrequent

counts, types, mostFrequent = analyzeLogs(logs)
print("Log Counts:", counts)
print("Log Types Present:", types)
print("Most Frequent Log Type:", mostFrequent)



cart = {}
 
def addProduct(cart, productId, name, price, quantity=1):
    if productId in cart:
        cart[productId]["quantity"] += quantity
    else:
        cart[productId] = {"name": name, "price": price, "quantity": quantity}
    print(f"Added {quantity} of {name}")
 
def removeProduct(cart, productId):
    if productId in cart:
        del cart[productId]
        print(f"Removed product {productId}")
    else:
        print("Product not found in cart!")
 
def modifyQuantity(cart, productId, newQuantity):
    if productId in cart:
        cart[productId]["quantity"] = newQuantity
        print(f"Updated quantity for {productId} to {newQuantity}")
    else:
        print("Product not found in cart!")
 
def calculateTotal(cart):
    total = 0
    for item in cart.values():
        total += item["price"] * item["quantity"]
    return total
 
def viewCart(cart):
    print(cart)
 
 
addProduct(cart, "P1", "Laptop", 150000, 1)
addProduct(cart, "P2", "Mouse", 2500, 2)
modifyQuantity(cart, "P1", 2)
viewCart(cart)
print("Cart Total:", calculateTotal(cart))
removeProduct(cart, "P2")
viewCart(cart)




emails = [
    "ali@gmail.com", "sara@yahoo.com", "ali@gmail.com", "ahmed@gmail.com",
    "sara@yahoo.com", "zain@hotmail.com"
]

uniqueEmailsUnordered = set(emails)
uniqueEmailsOrdered = list(dict.fromkeys(emails))

emailCounts = {}
for email in emails:
    emailCounts[email] = emailCounts.get(email, 0) + 1

print("Original Emails:", emails)
print("Unique Emails (unordered, fast):", uniqueEmailsUnordered)
print("Unique Emails (ordered, preserves first occurrence):", uniqueEmailsOrdered)
print("Email Occurrence Counts:", emailCounts)




config = (
    ("appName", "InventorySystem"),
    ("version", "2.3.1"),
    ("supportedEnvironments", ("dev", "staging", "production")),
    ("databaseConfig", (("host", "localhost"), ("port", 5432), ("dbName", "inventory_db")))
)
 
print("Application Config:", config)
 
config[0] = ("appName", "NewName")
 


employees = [
    ("E101", "Ali", "IT", 85000),
    ("E102", "Sara", "HR", 75000),
    ("E103", "Ahmed", "IT", 95000),
    ("E104", "Zain", "Finance", 90000)
]

employeeById = {}
for emp in employees:
    employeeById[emp[0]] = {"name": emp[1], "dept": emp[2], "salary": emp[3]}

departmentGroups = {}
for empId, name, dept, salary in employees:
    departmentGroups.setdefault(dept, []).append((empId, name, salary))

itEmployees = departmentGroups.get("IT", [])
averageSalary = sum(emp[3] for emp in employees) / len(employees)
highestPaid = max(employees, key=lambda emp: emp[3])
existingDepartments = set(dept for _, _, dept, _ in employees)

departmentCounts = {}
for _, _, dept, _ in employees:
    departmentCounts[dept] = departmentCounts.get(dept, 0) + 1

print("Employees in IT Department:", itEmployees)
print("Average Salary:", averageSalary)
print("Highest Paid Employee:", highestPaid)
print("Departments:", existingDepartments)
print("Employees per Department:", departmentCounts)
print("Lookup by Employee ID (E103):", employeeById["E103"])
