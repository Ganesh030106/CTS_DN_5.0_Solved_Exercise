class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def query(self, sql):
        print(f"Executing: {sql}")

# Test
db1 = DatabaseConnection()
db2 = DatabaseConnection()
db1.query("SELECT * FROM users")
print(f"Are they the same instance? {db1 is db2}")