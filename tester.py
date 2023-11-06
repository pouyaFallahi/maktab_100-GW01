import unittest, sqlite3, logging
from logger_file import Logger, log_function

# Replace 'your_database.db' with your actual database file
DATABASE_FILE = 'your_database.db'


class TestDatabase(unittest.TestCase):
    @log_function(Logger('Use setUp function'), log_level=logging.INFO)
    def setUp(self):
        # Set up a database connection and cursor before each test
        self.conn = sqlite3.connect(DATABASE_FILE)
        self.cursor = self.conn.cursor()
    @log_function(Logger('Use tearDown function'), log_level=logging.INFO)
    def tearDown(self):
        # Clean up resources after each test
        self.conn.close()
    @log_function(Logger('Use test function'), log_level=logging.INFO)
    def test_table_exists(self):
        # Test if a specific table exists in the database
        table_name = 'your_table_name'
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    @log_function(Logger('Use test function'), log_level=logging.INFO)
    def test_data_insertion(self):
        # Test data insertion into the database
        data = ("John", "Doe", 30)
        query = "INSERT INTO your_table_name (first_name, last_name, age) VALUES (?, ?, ?);"
        self.cursor.execute(query, data)
        self.conn.commit()

        # Check if the data was inserted correctly
        query = "SELECT first_name, last_name, age FROM your_table_name WHERE first_name='John';"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result, data)


if __name__ == '__main__':
    unittest.main()
