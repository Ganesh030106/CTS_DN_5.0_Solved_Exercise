products = ["Laptop", "Mouse", "Keyboard",
            "Monitor", "Printer"]

target = input("Enter Product Name: ")

# Linear Search
found = False

for i in range(len(products)):

    if products[i] == target:
        print("Linear Search -> Found at", i)
        found = True
        break

if not found:
    print("Not Found")

# Binary Search

products.sort()

low = 0
high = len(products) - 1

while low <= high:

    mid = (low + high) // 2

    if products[mid] == target:
        print("Binary Search -> Found")
        break

    elif target > products[mid]:
        low = mid + 1

    else:
        high = mid - 1