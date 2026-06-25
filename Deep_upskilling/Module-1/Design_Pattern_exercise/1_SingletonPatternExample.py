class Logger:
    _instance = None

    def __new__(cls):
        # Check if an instance already exists
        if cls._instance is None:
            # Create the instance if it doesn't exist
            cls._instance = super(Logger, cls).__new__(cls)
            print("Logger instance created.")
        return cls._instance

    def log(self, message):
        print(f"[LOG]: {message}")


# Create two variables attempting to point to Logger
logger1 = Logger()
logger2 = Logger()

# Verify both variables point to the exact same object in memory
print(f"Is logger1 the same instance as logger2? {logger1 is logger2}")

# Test the functionality
logger1.log("This is a message from logger1.")
logger2.log("This is a message from logger2.")