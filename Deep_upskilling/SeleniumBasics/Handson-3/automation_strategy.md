# Hands-On 3: Test Automation Process, Lifecycle & Framework Types

## Task 1: Automation Decision and Test Case Selection

### 1. Criteria for Deciding Whether a Test Case Should Be Automated

Automation is not suitable for every test case. Before automating a test, it is important to evaluate whether the effort and cost of automation are justified. Some of the common criteria are given below.

#### Criterion 1: Repetitive Execution

Test cases that need to be executed repeatedly are ideal candidates for automation.

**Application:**

The `POST /api/courses/` API is tested after every code update. Since this test is executed frequently, automating it saves both time and effort.

---

#### Criterion 2: Regression Testing

Regression tests ensure that existing features continue to work correctly after new changes are introduced. These tests are usually executed many times during development.

**Application:**

Whenever changes are made to the Course Management System, the course creation API should still function correctly. Automating this test helps detect regressions quickly.

---

#### Criterion 3: Stable Functionality

Features that rarely change are good candidates for automation because the scripts require minimal maintenance.

**Application:**

The API structure for creating a course remains mostly unchanged, making it suitable for automated testing.

---

#### Criterion 4: Data-Driven Testing

Some test cases require the same steps to be executed using multiple input values. Automation makes this process faster and more efficient.

**Application:**

Different combinations of course names, course codes, departments, and credit values can be tested automatically using external test data.

---

#### Criterion 5: High Business Impact

Business-critical functionalities should always be verified to reduce the risk of failures.

**Application:**

Course creation is one of the core features of the Course Management System, so automating its validation improves reliability.

---

## 2. Choosing Between Manual and Automated Testing

| Test Case | Decision | Reason |
|-----------|----------|--------|
| Regression testing of CRUD APIs after every code change | Automate | Executed frequently and suitable for automation |
| Exploratory testing of a newly developed search feature | Manual | Requires human observation and creativity |
| Performance testing with 100 concurrent users | Automate | Load testing tools can simulate multiple users efficiently |
| Login page UI testing | Automate | Stable functionality executed regularly |
| Verifying Swagger documentation | Manual | Requires human review and interpretation |
| Smoke testing after every deployment | Automate | Quick validation is needed before releasing the application |

---

## 3. Test Automation ROI (Return on Investment)

### Definition

Test Automation ROI measures whether the time invested in developing automation scripts is worthwhile when compared with repeated manual execution.

### Given

- Automation Development Time = **4 hours**
- Manual Execution Time = **30 minutes (0.5 hours)**

### ROI Calculation

Number of manual executions required to recover the automation effort:

```
4 ÷ 0.5 = 8
```

Therefore, the automation script becomes beneficial after approximately **8 executions**.

### Maintenance Consideration

Suppose maintenance effort increases by **20% after the 10th execution**.

Although maintenance requires additional effort, automation still becomes more cost-effective over time because manual execution would consume much more time in the long run.

---

## 4. Flaky Tests

### Definition

A flaky test is a test that sometimes passes and sometimes fails even though there are no actual changes in the application. Such tests reduce confidence in the automation suite.

### Example

Consider a Selenium test that clicks a button immediately after the page loads.

- On a fast system, the button loads quickly and the test passes.
- On a slower system, the button is not yet available, causing the test to fail.

The failure is caused by timing issues rather than defects in the application.

### Best Practices to Prevent Flaky Tests

#### 1. Use Explicit Waits

Instead of using fixed delays like:

```python
time.sleep(3)
```

Use explicit waits such as:

```python
WebDriverWait(driver, 10)
```

This waits only until the required element becomes available.

---

#### 2. Use Stable Locators

Reliable locators make automation scripts more stable.

Preferred locators include:
- ID
- Name
- CSS Selector

Avoid using long or fragile XPath expressions whenever possible.

---

#### 3. Keep Tests Independent

Every test case should start with a clean environment and should not depend on another test. Independent tests are easier to maintain and less likely to become flaky.

---

# Task 2: Comparing Automation Framework Types

## 5. Comparison of Automation Frameworks

### Linear Framework

#### Description

A Linear Framework is the simplest type of automation framework where all test steps are written in a single script and executed one after another.

#### Advantage

- Easy to create and understand.

#### Disadvantage

- Difficult to maintain as the project grows.

#### Example

A single automation script that performs login, creates a course, and verifies the result.

---

### Modular Framework

#### Description

The application is divided into smaller reusable modules, and each module has its own automation script.

#### Advantage

- Promotes code reuse.
- Easier to maintain.

#### Disadvantage

- Requires proper planning before implementation.

#### Example

Separate automation modules for:
- Login
- Course Management
- Student Management

---

### Data-Driven Framework

#### Description

Test data is stored separately from the test scripts, allowing the same script to run with multiple input values.

#### Advantage

- Supports multiple test scenarios using one script.

#### Disadvantage

- Managing external test data adds complexity.

#### Example

Executing the course creation test using 50 different course records stored in a CSV or Excel file.

---

### Keyword-Driven Framework

#### Description

Testing actions are represented using predefined keywords, making test creation easier for non-technical users.

#### Advantage

- Allows business users or manual testers to contribute.

#### Disadvantage

- Initial framework development is more complex.

#### Example

Common keywords include:
- Login
- CreateCourse
- VerifyCourse
- Logout

---

### Hybrid Framework

#### Description

A Hybrid Framework combines the advantages of Modular, Data-Driven, and Keyword-Driven frameworks into a single solution.

#### Advantage

- Highly flexible
- Easy to maintain
- Suitable for large enterprise projects

#### Disadvantage

- More complex to design and implement.

#### Example

A Selenium automation framework used for a large Course Management System with reusable modules, external test data, and keyword-based execution.

---

## 6. Recommended Framework

### Project Requirements

The testing team needs to:

- Test login using 50 different user credentials.
- Reuse the login functionality across 20 different test cases.
- Allow both technical and non-technical team members to participate.

### Recommended Solution

A **Hybrid Framework** is the most suitable choice because it combines:

- Modular Framework
- Data-Driven Framework
- Keyword-Driven Framework

### Justification

**Modular Framework**
- Makes the login functionality reusable across multiple test cases.

**Data-Driven Framework**
- Supports testing with different username and password combinations.

**Keyword-Driven Framework**
- Enables non-technical users to execute and understand automated tests more easily.

Overall, a Hybrid Framework provides the best balance of scalability, maintainability, and flexibility.

---

## 7. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/
│
├── config/
│   └── config.py
│
├── test_data/
│   ├── login_data.csv
│   └── course_data.csv
│
├── pages/
│   ├── login_page.py
│   ├── course_page.py
│   └── student_page.py
│
├── utilities/
│   ├── logger.py
│   ├── excel_reader.py
│   └── screenshot.py
│
├── tests/
│   ├── test_login.py
│   ├── test_course_creation.py
│   └── test_student_enrollment.py
│
├── reports/
│
├── screenshots/
│
└── requirements.txt
```

### Description of Each Folder

- **config/** – Stores configuration files such as browser settings and environment details.
- **test_data/** – Contains external test data like CSV or Excel files.
- **pages/** – Includes Page Object Model (POM) classes for different application pages.
- **utilities/** – Contains reusable helper functions such as logging, reading data, and capturing screenshots.
- **tests/** – Stores all automated test scripts.
- **reports/** – Contains execution reports generated after running the tests.
- **screenshots/** – Stores screenshots captured whenever a test fails.
- **requirements.txt** – Lists all Python packages required for the automation project.

---

# Conclusion

Through this hands-on exercise, I learned how to decide which test cases should be automated and when manual testing is more appropriate.

This activity also helped me understand:

- The criteria for selecting automation candidates.
- The difference between manual and automated testing.
- How Test Automation ROI is calculated.
- The causes of flaky tests and methods to prevent them.
- Different types of automation frameworks.
- Why Hybrid Frameworks are commonly used in enterprise applications.
- How an automation framework is organized using a structured folder hierarchy.

Overall, this exercise strengthened my understanding of automation testing concepts and the practical design of scalable test automation frameworks.