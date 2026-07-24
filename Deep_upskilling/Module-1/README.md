# Module 1: Software Design Patterns in Python

This folder contains hands-on implementations of essential **Creational**, **Structural**, and **Behavioral** software design patterns using Python. Design patterns provide reusable solutions to common software design problems, improving code maintainability, scalability, and adherence to SOLID principles.

---

## 📂 Directory Structure

```text
Module-1/
├── Design_Pattern_exercise/
│   ├── 1_SingletonPatternExample.py  # Creational: Logger / Config Singleton
│   ├── 2_Factory_method.py          # Creational: Document / Notification Factory
│   ├── 3_Builder.py                 # Creational: Complex Object Construction
│   ├── 4_Adapter_pattern.py         # Structural: Incompatible Interface Adaptation
│   ├── 5_Decorator_Pattern.py       # Structural: Dynamic Behavior Addition
│   ├── 6_Proxy_Pattern.py           # Structural: Access Control & Lazy Loading
│   ├── 7_Observer_pattern.py        # Behavioral: Event-Driven Notification Mechanism
│   ├── 8_Design_Pattern_exercise.py # Behavioral: Strategy Pattern Implementation
│   ├── 9_Command_pattern.py         # Behavioral: Encapsulating Requests as Objects
│   ├── 10_MVC_Pattern.py            # Architectural: Model-View-Controller Design
│   └── 11_Dependency_pattern.py     # Architectural: Dependency Injection Pattern
└── output/                          # Verification logs and execution outputs
```

---

## 📑 Implemented Design Patterns & Exercises

| Exercise File | Design Pattern Category | Pattern Name | Key Concepts & Use Cases |
|---|---|---|---|
| [1_SingletonPatternExample.py](file:///e:/Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise/1_SingletonPatternExample.py) | Creational | **Singleton Pattern** | Ensures a class has only one instance and provides a global access point (e.g., Logger, DB Pool). |
| [2_Factory_method.py](file:///e:/Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise/2_Factory_method.py) | Creational | **Factory Method** | Defines an interface for creating objects, delegating instantiation logic to subclasses. |
| [3_Builder.py](file:///e:/Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise/3_Builder.py) | Creational | **Builder Pattern** | Separates complex object construction from its representation (step-by-step construction). |
| [4_Adapter_pattern.py](file:///e:/Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise/4_Adapter_pattern.py) | Structural | **Adapter Pattern** | Allows objects with incompatible interfaces to collaborate by converting interfaces. |
| [5_Decorator_Pattern.py](file:///e:/Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise/5_Decorator_Pattern.py) | Structural | **Decorator Pattern** | Dynamically adds new responsibilities to objects without altering existing code. |
| [6_Proxy_Pattern.py](file:///e:/Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise/6_Proxy_Pattern.py) | Structural | **Proxy Pattern** | Provides a surrogate or placeholder for another object to control access, caching, or lazy initialization. |
| [7_Observer_pattern.py](file:///e:/Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise/7_Observer_pattern.py) | Behavioral | **Observer Pattern** | Defines a one-to-many dependency where multiple observers are notified automatically of state changes. |
| [8_Design_Pattern_exercise.py](file:///e:/Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise/8_Design_Pattern_exercise.py) | Behavioral | **Strategy Pattern** | Encapsulates interchangeable algorithms (e.g., payment processing strategies). |
| [9_Command_pattern.py](file:///e:/Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise/9_Command_pattern.py) | Behavioral | **Command Pattern** | Encapsulates a request as an object, allowing parameterization and queueing of requests. |
| [10_MVC_Pattern.py](file:///e:/Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise/10_MVC_Pattern.py) | Architectural | **Model-View-Controller** | Decouples data model, user interface view, and business logic control flow. |
| [11_Dependency_pattern.py](file:///e:/Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise/11_Dependency_pattern.py) | Architectural | **Dependency Injection** | Injects dependencies from external sources rather than instantiating them hardcoded inside classes. |

---

## ⚡ How to Run Exercises

Execute any pattern exercise script directly using Python:

```bash
# Navigate to Module-1 directory
cd Placement/CTS/Deep_upskilling/Module-1/Design_Pattern_exercise

# Run individual design pattern scripts
python 1_SingletonPatternExample.py
python 2_Factory_method.py
python 3_Builder.py
python 4_Adapter_pattern.py
python 5_Decorator_Pattern.py
python 6_Proxy_Pattern.py
python 7_Observer_pattern.py
python 8_Design_Pattern_exercise.py
python 9_Command_pattern.py
python 10_MVC_Pattern.py
python 11_Dependency_pattern.py
```

---

## 🧠 Key Learning Outcomes
- Understanding object-oriented programming (OOP) principles in Python.
- Applying GoF (Gang of Four) creational, structural, and behavioral design patterns.
- Structuring extensible codebase architecture adhering to the Open-Closed Principle (OCP) and Single Responsibility Principle (SRP).
