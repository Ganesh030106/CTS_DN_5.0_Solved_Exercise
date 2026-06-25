books = [
    "Python",
    "Java",
    "C Programming",
    "Data Structures",
    "Operating Systems"
]

title = input("Enter Book Name: ")

for book in books:

    if book.lower() == title.lower():
        print("Book Available")
        break
else:
    print("Book Not Found")