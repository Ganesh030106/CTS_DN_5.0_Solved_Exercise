# Module 2: Data Structures & Algorithms Exercises

This module contains practical Python implementations of foundational **Data Structures & Algorithms (DSA)** applied to real-world business scenarios such as inventory management, e-commerce searching/sorting, task queues, employee management, and financial forecasting.

---

## 📂 Directory Structure

```text
Module-2/
├── DSA Exercises/
│   ├── 1_Inventory_management.py  # Array/List Operations & Stock Management
│   ├── 2_E-commerce.py            # Search Algorithms (Linear & Binary Search)
│   ├── 3_Sorting_customers.py     # Sorting Algorithms (Bubble, Quick, Merge Sort)
│   ├── 4_Employee_management.py   # Array & List Records Management
│   ├── 5_Task_management.py       # Linked Lists (Singly & Doubly Linked List)
│   ├── 6_Library_management.py    # Binary Search & Linear Search in Book Catalog
│   └── 7_Financial_Forecast.py    # Recursion & Dynamic Programming Algorithms
└── output/                        # Output logs and performance benchmarks
```

---

## 📑 Problem Scenarios & Algorithmic Solutions

| Exercise File | Core DSA Concept | Real-World Application / Problem Statement |
|---|---|---|
| [1_Inventory_management.py](file:///e:/Placement/CTS/Deep_upskilling/Module-2/DSA%20Exercises/1_Inventory_management.py) | **Arrays & List Operations** | Inventory Stock Tracking System: Insert, update, delete, and list products by ID and quantity. |
| [2_E-commerce.py](file:///e:/Placement/CTS/Deep_upskilling/Module-2/DSA%20Exercises/2_E-commerce.py) | **Searching Algorithms** | Product Search Engine: Comparing Linear Search ($O(N)$) vs. Binary Search ($O(\log N)$) on sorted product catalogs. |
| [3_Sorting_customers.py](file:///e:/Placement/CTS/Deep_upskilling/Module-2/DSA%20Exercises/3_Sorting_customers.py) | **Sorting Algorithms** | Customer Orders Sorting: Implementing Bubble Sort, Insertion Sort, Quick Sort, and Merge Sort algorithms. |
| [4_Employee_management.py](file:///e:/Placement/CTS/Deep_upskilling/Module-2/DSA%20Exercises/4_Employee_management.py) | **Arrays & Record Structures** | Employee Information Management System: Searching, displaying, and filtering employee records. |
| [5_Task_management.py](file:///e:/Placement/CTS/Deep_upskilling/Module-2/DSA%20Exercises/5_Task_management.py) | **Linked Lists** | Task Management Queue: Singly Linked List implementation for dynamic task insertion, traversal, and deletion. |
| [6_Library_management.py](file:///e:/Placement/CTS/Deep_upskilling/Module-2/DSA%20Exercises/6_Library_management.py) | **Binary Search Trees / Searching** | Library Book Catalog System: Quick search and lookup for book availability using Binary Search. |
| [7_Financial_Forecast.py](file:///e:/Placement/CTS/Deep_upskilling/Module-2/DSA%20Exercises/7_Financial_Forecast.py) | **Recursion & Dynamic Programming** | Financial Forecasting Model: Predicting growth and compound interest trajectories using recursive functions. |

---

## ⚡ How to Run Exercises

Run any DSA exercise script using Python:

```bash
# Navigate to DSA Exercises folder
cd Placement/CTS/Deep_upskilling/Module-2/DSA\ Exercises

# Run individual DSA exercise scripts
python 1_Inventory_management.py
python 2_E-commerce.py
python 3_Sorting_customers.py
python 4_Employee_management.py
python 5_Task_management.py
python 6_Library_management.py
python 7_Financial_Forecast.py
```

---

## 📊 Complexity Analysis & Key Takeaways

- **Time Complexity Optimization**: Understanding trade-offs between $O(N^2)$ sorting (Bubble Sort) vs $O(N \log N)$ (Quick/Merge Sort).
- **Space Complexity**: Efficient memory management using in-place algorithms and linked list nodes.
- **Recursion vs Iteration**: Applying memoization and base cases to prevent stack overflow in financial prediction models.
