# CTS Digital Nurture 5.0 – Upskilling Coding Exercises

Welcome to the **Upskilling Coding Exercises** repository of the **Cognizant Digital Nurture 5.0 Program**. This repository contains a total of **80 solved coding exercises** (55 Python programming exercises and 25 SQL database exercises) along with database table schema definitions and reference handbooks.

---

## 📂 Repository Architecture

```text
Upskilling_coding_exercises/
│
├── DN5.0-Upskilling-Handbook-Python.pdf  # Python Curriculum & Reference Guide
│
├── SQL/                                  # 25 Database & SQL Query Exercises
│   ├── tables.sql                        # EventManagement Database Schema & Sample Data
│   ├── ex_no_1.sql to ex_no_25.sql       # SQL Query Solution Files
│   └── README.md                         # Detailed SQL Module Documentation
│
└── python/                               # 55 Python Coding Exercises
    ├── ex_no_1.py to ex_no_55.py         # Python Solution Scripts
    └── README.md                         # Detailed Python Module Documentation
```

---

## 🛠️ Summary of Exercises

| Subfolder | Domain | Total Exercises | Key Topics Covered |
|---|---|---|---|
| 📄 [SQL/](file:///e:/Placement/CTS/Upskilling_coding_exercises/SQL/README.md) | **Relational Databases & SQL** | **25 Exercises** | EventManagement Schema, DDL/DML, INNER/LEFT Joins, Group By, Aggregations (`COUNT`, `SUM`, `AVG`), Subqueries, Filtering (`WHERE`, `HAVING`). |
| 📄 [python/](file:///e:/Placement/CTS/Upskilling_coding_exercises/python/README.md) | **Python Fundamentals & OOP** | **55 Exercises** | Data Types, String Manipulation, Conditionals, Loops, Lists, Dictionaries, Functions, Recursion, Object-Oriented Programming (OOP), File Handling, Matrix Operations. |

---

## 📚 Handbook & Curriculum Reference
- **Document**: `DN5.0-Upskilling-Handbook-Python.pdf`
- **Topics**: Comprehensive guide covering Python syntax, data structures, control flow, functions, OOP concepts, database interaction, and SQL fundamentals.

---

## 🚀 Execution Instructions

### Running SQL Queries
1. Import and execute `SQL/tables.sql` into MySQL Server or PostgreSQL to set up the `EventManagement` database and populate initial sample data.
2. Execute individual query files `ex_no_1.sql` through `ex_no_25.sql` using MySQL Workbench, DBeaver, or command line interface:
   ```bash
   mysql -u root -p EventManagement < SQL/ex_no_1.sql
   ```

### Running Python Exercises
Run any Python exercise using standard Python 3:
```bash
# Navigate to python folder
cd Placement/CTS/Upskilling_coding_exercises/python

# Execute any exercise script
python ex_no_1.py
python ex_no_10.py
python ex_no_55.py
```
