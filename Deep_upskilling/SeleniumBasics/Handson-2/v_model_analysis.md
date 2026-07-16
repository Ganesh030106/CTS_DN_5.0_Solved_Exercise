# Hands-On 2: SDLC vs TDLC – V-Model & Agile QA Integration

## Task 1: Understanding the V-Model

### 1. V-Model Diagram

```
                    Acceptance Testing
                           ↑
Requirements  --------------------------
                           ↓

                      System Testing
                           ↑
System Design --------------------------
                           ↓

                   Integration Testing
                           ↑
Architecture Design -------------------
                           ↓

                      Unit Testing
                           ↑
Module Design -------------------------
                           ↓

                          Coding
```

The V-Model explains that every development phase has a corresponding testing phase. Testing activities are planned early in the software development process, which helps in identifying defects before they become expensive to fix.

---

### 2. Mapping SDLC Phases with TDLC Phases

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|------------|--------------------------|-------------------------|
| Requirements Analysis | Acceptance Testing | Acceptance Test Plan |
| System Design | System Testing | System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan |
| Module Design | Unit Testing | Unit Test Cases |

This mapping shows that each stage of software development is directly connected to a testing activity. Preparing test artifacts during the development phase helps improve software quality.

---

### 3. Entry and Exit Criteria

#### Unit Testing

**Entry Criteria**
- Module development is completed.
- Code review has been finished.
- Development environment is ready for testing.

**Exit Criteria**
- All unit test cases have been executed.
- No critical defects remain.
- Required code coverage has been achieved.

---

#### Integration Testing

**Entry Criteria**
- Unit testing is completed successfully.
- All required modules have been integrated.

**Exit Criteria**
- Communication between modules has been tested.
- No major integration issues are found.

---

#### System Testing

**Entry Criteria**
- Integration testing has been completed.
- Test environment is available and stable.

**Exit Criteria**
- All functional requirements have been verified.
- Critical and high-priority defects have been resolved.

---

#### Acceptance Testing

**Entry Criteria**
- System testing is completed.
- Business stakeholders have approved the requirements.

**Exit Criteria**
- Users confirm that the application meets their expectations.
- The product is approved for deployment or release.

---

### 4. Early QA Involvement

#### Requirements Review

QA engineers participate in requirement discussions before development begins. This helps identify:
- Unclear or ambiguous requirements.
- Missing business rules.
- Areas that may be difficult to test later.

---

#### Design Review

QA also reviews the application design to:
- Identify possible integration risks.
- Verify that business workflows are correctly designed.
- Prepare test cases at an early stage.

Early QA involvement helps reduce defects and improves the overall quality of the software.

---

# Task 2: Agile QA and Shift-Left Testing

## 5. Challenges in the Waterfall Model

### Problem 1

Most defects are identified only after the development phase is completed. Fixing these defects at a later stage increases both cost and effort.

---

### Problem 2

If requirements are misunderstood during the initial stages, the issue may remain unnoticed until testing begins, resulting in significant rework.

---

### Problem 3

A large number of bugs are often reported near the project deadline, which can delay the software release and reduce product quality.

---

## 6. QA Responsibilities in Agile Ceremonies

### Sprint Planning

During sprint planning, the QA team:
- Reviews user stories.
- Defines acceptance criteria.
- Estimates the testing effort required for the sprint.

---

### Daily Stand-up

In the daily stand-up meeting, QA engineers:
- Share testing progress.
- Discuss any blockers or challenges.
- Update the team about newly identified defects.

---

### Sprint Review

During the sprint review, QA:
- Validates completed features.
- Demonstrates tested functionality.
- Ensures that acceptance criteria have been satisfied.

---

### Sprint Retrospective

After each sprint, QA participates in the retrospective to:
- Discuss testing challenges.
- Suggest improvements to the testing process.
- Help the team improve software quality in future sprints.

---

## 7. Shift-Left Testing Practices

### A. Reviewing Requirements Early

Instead of waiting until development is complete, QA reviews requirements at the beginning of the project. This helps identify missing information and unclear requirements before coding starts.

---

### B. Writing Test Cases Before Development (TDD / BDD)

In Shift-Left Testing, test cases are prepared before writing the actual code.

**Example:**

Before developing the `POST /api/courses/` endpoint, QA prepares API validation test cases to verify expected behavior once development is complete.

---

### C. Static Code Analysis

Static code analysis tools help identify coding issues without executing the application.

Some commonly used tools include:
- Pylint
- Flake8
- SonarQube

These tools improve code quality by detecting syntax errors, security issues, and coding standard violations early.

---

### D. API Contract Testing

API contract testing verifies that both the frontend and backend follow the same request and response structure. This helps prevent integration issues when different teams work independently.

---

## 8. Acceptance Criteria Using Gherkin

### Scenario 1: Successful Course Creation

```gherkin
Given the college administrator is logged into the system
When the administrator enters valid course details
Then the course should be created successfully
And a success message should be displayed
```

---

### Scenario 2: Duplicate Course Code

```gherkin
Given a course with the same course code already exists
When the administrator submits another course with that code
Then the system should reject the request
And an appropriate error message should be displayed
```

---

### Scenario 3: Missing Required Fields

```gherkin
Given the administrator is creating a new course
When one or more mandatory fields are left empty
Then the system should prevent the submission
And validation messages should be displayed for the missing fields
```

---

# Conclusion

Through this hands-on exercise, I gained a better understanding of how software development and software testing work together throughout the project lifecycle.

The activity helped me learn about:

- The relationship between SDLC and TDLC.
- How the V-Model connects every development phase with a corresponding testing phase.
- The importance of defining entry and exit criteria for each testing level.
- The role of QA engineers in Agile development.
- Shift-Left Testing practices that improve software quality by identifying issues early.
- Writing acceptance criteria using the Gherkin format.

Overall, this exercise improved my understanding of modern software testing practices and the importance of involving QA throughout the Software Development Life Cycle.