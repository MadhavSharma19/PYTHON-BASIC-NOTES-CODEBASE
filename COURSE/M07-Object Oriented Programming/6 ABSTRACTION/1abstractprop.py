from abc import ABC, abstractmethod

class Database(ABC):
    @property
    @abstractmethod
    def connection_string(self):
        """Each database must provide its connection string."""
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    # Template method pattern - defines the algorithm structure
    def execute_query(self, query):
        self.connect()
        print(f"Executing: {query}")
        print(f"Using connection: {self.connection_string}")
        self.disconnect()

class MySQLDatabase(Database):
    @property
    def connection_string(self):
        return "mysql://localhost:3306/mydb"


    def connect(self):
        print("Connected to MySQL")


    def disconnect(self):
        print("Disconnected from MySQL")


class SQLiteDatabase(Database):
    @property
    def connection_string(self):
        return "sqlite:///mydb.sqlite3"


    def connect(self):
        print("Connected to SQLite")


    def disconnect(self):
        print("Disconnected from SQLite")


# Usage
db = MySQLDatabase()
db.execute_query("SELECT * FROM users")
