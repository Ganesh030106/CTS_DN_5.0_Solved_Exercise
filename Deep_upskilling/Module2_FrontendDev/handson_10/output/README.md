# Handson-10 Tasks:

# Framework Comparison

## React
Uses Redux Toolkit and createAsyncThunk for async state management.

## Angular
Uses Services and RxJS Observables for shared state and API communication.

## Vue
Uses Pinia Stores with async actions and storeToRefs for reactive state management.

## Conclusion

Vue with Pinia provides a simple and lightweight approach for centralized state management.

# Task 1 – Build a Centralized API Service Layer

Implemented:
• Axios-based centralized API client
• Request interceptor for authentication headers
• Response interceptor for standardized response handling
• Reusable API functions for course operations
• Integration with Vue components

Result:
Course data was successfully retrieved from the API and displayed in the user interface through the centralized API layer.

# Task 2 – Advanced State Management with Pinia

Implemented:
• Pinia store for centralized state management
• Async action for fetching course data
• Loading state handling
• Error state handling
• storeToRefs for reactive state access
• Store integration within Vue components

Result:
Course data is now managed through a centralized Pinia store instead of local component state.

# Task - 3

Implemented:
• Async enrollment action using Pinia
• Store reset using $reset()
• Reactive state access using storeToRefs()
• Global application error handling
• Framework comparison documentation

Result:
Advanced state management patterns were successfully implemented using Pinia and integrated into the Vue application.