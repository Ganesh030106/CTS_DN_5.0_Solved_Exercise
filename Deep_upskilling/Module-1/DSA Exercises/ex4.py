employees = []

employees.append(["E101", "Madhi", "Developer"])
employees.append(["E102", "Anu", "Tester"])
employees.append(["E103", "Ravi", "Designer"])

print("Employee Records")

for emp in employees:
    print(emp)

search_id = input("Enter Employee ID: ")

for emp in employees:

    if emp[0] == search_id:
        print("Employee Found")
        print(emp)
        break

employees.pop(0)

print("\nAfter Deletion")

for emp in employees:
    print(emp)