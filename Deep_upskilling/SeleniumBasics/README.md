# Selenium Basics & Web Automation Testing Framework

This directory contains the hands-on exercises and full test automation framework for the **Selenium & Quality Assurance (QA)** module of the CTS Digital Nurture program.

It spans foundational QA methodologies, V-Model process analysis, test automation strategy documentation, and an end-to-end Python-Selenium test automation suite using PyTest and Page Object Model (POM).

---

## 📂 Directory Structure

```text
SeleniumBasics/
│
├── Handson-1/               # QA & Testing Concepts Overview
│   └── qa_concepts.md       # STLC, Black-box vs White-box, Test Levels
│
├── Handson-2/               # SDLC & V-Model Analysis
│   └── v_model_analysis.md  # Verification & Validation Phases
│
├── Handson-3/               # Automation Strategy & Framework Planning
│   └── automation_strategy.md # ROI Analysis, Tool Selection & Strategy
│
├── Handson-4/               # Selenium WebDriver Basics & Navigation
│   ├── Task-1/              # Browser Operations & URL Navigation
│   └── Task-2/              # Basic Web Page Element Locators
│
├── Handson-5/               # Web Elements & Form Handling
│   ├── Task-1/              # Input Boxes, Buttons & Dropdowns
│   └── Task-2/              # Checkboxes, Radio Buttons & Alerts
│
├── Handson-6/               # Synchronization & Wait Strategies
│   ├── Task-1/              # Implicit Wait Implementation
│   └── Task-2/              # Explicit Wait & Expected Conditions
│
├── Handson-7/               # Advanced Interactions & Frames
│   ├── Task-1/              # Actions Class (Drag & Drop, Hover)
│   └── Task-2/              # Switching Frames & Windows
│
├── selenium_project/        # End-to-End Test Automation Framework
│   ├── conftest.py          # PyTest Fixtures (Driver setup/teardown)
│   ├── setup_test.py        # WebDriver Initialization Verification
│   ├── locators_test.py     # Locators (ID, XPath, CSS Selector)
│   ├── navigation_test.py   # Browser History & Navigation Suite
│   ├── waits_test.py        # Explicit & Implicit Wait Tests
│   ├── test_playground.py   # Interactive Component Test Suite
│   ├── pages/               # Page Object Model (POM) Classes
│   ├── screenshots/         # Automated Failure Screenshots
│   └── report.html          # PyTest HTML Test Execution Report
│
└── requirements.txt         # Selenium, PyTest, and Dependency packages
```

---

## 🧪 Hands-On Module Breakdown

| Hands-On | Category | Core Topics Covered |
|---|---|---|
| **Handson-1** | **QA Concepts** | Software Testing Life Cycle (STLC), Defect Life Cycle, Manual vs Automation Testing. |
| **Handson-2** | **V-Model Analysis** | V-Model verification and validation stages, Requirement Analysis to Acceptance Testing mapping. |
| **Handson-3** | **Automation Strategy** | Test Automation Feasibility, ROI calculation, Test Suite Selection criteria. |
| **Handson-4** | **WebDriver Basics** | Browser launch, driver instantiation (Chrome/Edge), page title verification, basic locators. |
| **Handson-5** | **Form Controls** | Interacting with text fields, dropdown options (Select class), alerts/popups handling. |
| **Handson-6** | **Synchronization** | Managing dynamic content loading with `WebDriverWait` and `expected_conditions`. |
| **Handson-7** | **Advanced Actions** | Mouse actions, context click, double click, iframe switching, multi-window switching. |
| **selenium_project** | **Framework Suite** | Production-ready **PyTest + Selenium POM Framework** with HTML test report generation. |

---

## 🛠️ Tech Stack & Dependencies

- **Programming Language**: Python 3.9+
- **Automation Engine**: Selenium WebDriver (v4.x)
- **Test Runner Framework**: PyTest
- **Reporting**: PyTest-HTML plugin
- **Design Pattern**: Page Object Model (POM)

---

## ⚡ How to Set Up and Run Tests

### 1. Install Dependencies
```bash
cd Placement/CTS/Deep_upskilling/SeleniumBasics
pip install -r requirements.txt
```

### 2. Run Individual Test Scripts
```bash
cd selenium_project
python -m pytest setup_test.py
python -m pytest locators_test.py
python -m pytest navigation_test.py
python -m pytest waits_test.py
```

### 3. Execute Complete Test Suite with HTML Report
```bash
pytest --html=report.html --self-contained-html
```

---

## 🎯 Framework Features & Best Practices
- **Page Object Model (POM)**: Decouples test scripts from UI locators for high maintainability.
- **Dynamic Waits**: Replaces brittle sleep statements with robust `WebDriverWait` explicit synchronization.
- **Automated Reporting**: Generates interactive HTML execution reports complete with status breakdowns.
