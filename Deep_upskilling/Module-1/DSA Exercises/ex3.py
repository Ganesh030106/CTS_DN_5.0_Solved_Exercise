orders = [4500, 9000, 1200, 7000, 3000]

print("Original Orders")
print(orders)

# Bubble Sort

bubble = orders.copy()

for i in range(len(bubble)):

    for j in range(len(bubble)-1):

        if bubble[j] > bubble[j+1]:
            bubble[j], bubble[j+1] = bubble[j+1], bubble[j]

print("\nBubble Sort")
print(bubble)


# Quick Sort

def quick_sort(data):

    if len(data) <= 1:
        return data

    pivot = data[-1]

    left = []
    right = []

    for num in data[:-1]:

        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


print("\nQuick Sort")
print(quick_sort(orders))