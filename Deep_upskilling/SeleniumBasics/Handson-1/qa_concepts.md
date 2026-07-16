# Hands-On 1: QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Understanding Different Types of Testing

### 1. Test Cases for Different Testing Levels

#### Unit Testing
**Test Case:**  
Check whether the `create_course()` function creates a new course successfully when all the required details are provided.

**Testing Type:** Functional Testing

---

#### Integration Testing
**Test Case:**  
Verify that the `POST /api/courses/` API correctly stores the course information in the database and returns an HTTP 201 (Created) response.

**Testing Type:** Functional Testing

---

#### System Testing
**Test Case:**  
Create a course using the API and verify that it is saved in the database. Then retrieve the course using the `GET /api/courses/` API to ensure the complete system works as expected.

**Testing Type:** Functional Testing

---

#### User Acceptance Testing (UAT)
**Test Case:**  
A college administrator creates a new course, and a student verifies that the course is visible and available for enrollment.

**Testing Type:** Functional Testing

---

### 2. Example of a Non-Functional Test

#### Performance Testing

**Test Case:**  
Verify that the `GET /api/courses/` endpoint responds within 2 seconds when 500 users access it simultaneously.

**Testing Type:** Non-Functional Testing

---

### 3. Black-Box Testing vs White-Box Testing

#### Black-Box Testing
Black-box testing focuses on checking whether the application works correctly from the user's perspective. The tester does not need to know how the code is written. Only the inputs and outputs are verified to ensure the expected functionality.

**Usually Performed By:** QA Engineers or Testers

---

#### White-Box Testing
White-box testing focuses on the internal structure of the application. The tester examines the source code, program logic, conditions, and execution paths to ensure everything works correctly.

**Usually Performed By:** Developers

---

| Feature | Black-Box Testing | White-Box Testing |
|---------|-------------------|-------------------|
| Knowledge of Code | Not Required | Required |
| Main Focus | Functionality | Internal Logic |
| Performed By | QA Testers | Developers |
| Example | API Testing | Unit Testing |

---

### 4. Test Cases for `POST /api/courses/`

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Status |
|--------------|-------------|---------------|------------|-----------------|---------------|--------|
| TC_COURSE_001 | Create a course using valid data | API server is running | Send a POST request with valid course details | Course is created successfully and HTTP 201 is returned | - | - |
| TC_COURSE_002 | Create a course using an existing course code | Course code already exists | Send a POST request with a duplicate course code | HTTP 409 Conflict should be returned | - | - |
| TC_COURSE_003 | Create a course without mandatory fields | API server is running | Send a POST request without required fields | HTTP 400 Bad Request should be returned | - | - |

---

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

The defect lifecycle describes the journey of a bug from the time it is identified until it is closed.

```
New
  ↓
Assigned
  ↓
Open
  ↓
Fixed
  ↓
Retest
  ↓
Verified
  ↓
Closed
```

### Rejected Defect Flow

```
New
  ↓
Assigned
  ↓
Rejected
```

A defect is rejected if it cannot be reproduced, is not actually a bug, or the application is working as intended.

---

### Deferred Defect Flow

```
Open
  ↓
Deferred
```

A defect is marked as deferred when fixing it is postponed to a future release because it is not considered urgent.

---

## 6. Severity and Priority Classification

### Bug A

**Issue:**  
The `POST /api/courses/` API returns HTTP 500 Internal Server Error for every request.

- **Severity:** Critical
- **Priority:** P1

**Reason:**  
This is a major issue because users cannot create any courses. Since it affects the core functionality of the application, it must be fixed immediately.

---

### Bug B

**Issue:**  
Course names longer than 150 characters are automatically truncated without any warning.

- **Severity:** Medium
- **Priority:** P2

**Reason:**  
Although the application continues to work, important data may be lost, which affects data quality.

---

### Bug C

**Issue:**  
There is a spelling mistake on the Swagger documentation page.

- **Severity:** Low
- **Priority:** P4

**Reason:**  
This is only a cosmetic issue and does not affect the application's functionality.

---

### Bug D

**Issue:**  
The login API occasionally returns HTTP 401 Unauthorized on the first login attempt.

- **Severity:** High
- **Priority:** P1

**Reason:**  
Users may not be able to log in consistently. Since authentication is a critical feature, the issue should be resolved as soon as possible.

---

## 7. Defect Report

### Defect ID
**BUG-001**

### Title
POST `/api/courses/` returns HTTP 500 Internal Server Error.

### Environment
Development Environment

### Build Version
v1.0

### Severity
Critical

### Priority
P1

### Steps to Reproduce

1. Start the API server.
2. Open the Swagger UI.
3. Navigate to the `POST /api/courses/` endpoint.
4. Enter valid course details.
5. Click **Execute**.

### Expected Result

The course should be created successfully, and the API should return **HTTP 201 Created**.

### Actual Result

The API returns **HTTP 500 Internal Server Error**, and the course is not created.

### Attachment

Screenshot showing the HTTP 500 error.

---

## 8. Difference Between Severity and Priority

### Severity
Severity indicates how much a defect affects the application's functionality or performance.

### Priority
Priority indicates how quickly the defect should be fixed based on business requirements.

### Example

Suppose there is a spelling mistake in the title displayed on the CEO's dashboard.

- **Severity:** Low (because the application still works correctly)
- **Priority:** High (because it is visible to senior management and should be corrected immediately)

This example shows that severity and priority are not always the same.

---

# Conclusion

Through this hands-on exercise, I gained a better understanding of:

- Different levels of software testing
- Functional and non-functional testing
- Black-box and white-box testing
- Writing effective test cases
- The complete defect lifecycle
- Severity and priority classification
- Preparing a professional defect report

Overall, this activity helped me understand how software testing ensures that an application is reliable, stable, and meets user requirements before it is released.