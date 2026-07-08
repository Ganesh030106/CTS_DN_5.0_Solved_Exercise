# Microservices Decomposition

| Service Name | Responsibility | Endpoints | Database |
|-------------|---------------|-----------|----------|
| Course Service | Course CRUD | /api/courses | coursemanager.db |
| Student Service | Student CRUD + Enrollment | /api/students | studentmanager.db |
| Auth Service | Register/Login | /api/auth | auth.db |
| Notification Service | Email Notifications | Internal | notification.db |