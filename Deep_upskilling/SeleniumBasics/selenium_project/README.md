## Hands-On 7: Page Object Model

Implemented Page Object Model (POM) framework using:

- BasePage
- SimpleFormPage
- CheckboxPage
- DropdownPage
- InputFormPage

Benefits:
- Better maintainability
- Reduced code duplication
- Centralized locator management
- Improved test readability

Test Execution Summary:
- 5 tests passed
- 1 test skipped due to external TestMu page structure changes

## Why Page Object Model?

In a flat Selenium script, locators are repeated across multiple test files.
If a locator changes (for example, the Submit button ID changes from
'submit' to 'btn-submit'), every test must be updated.

Page Object Model stores locators in one place.
Only the page class needs modification, while all tests continue working.
This improves maintainability, readability, and reusability.