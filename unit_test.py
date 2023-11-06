from database import Database
import unittest, logging
from unittest.mock import MagicMock
from logger_file import Logger, log_function

class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.obj = Database()
        self.obj.execute = MagicMock()
        self.obj.connection = MagicMock()
        self.obj.cursor = MagicMock()

    @log_function(Logger('Use test function'), log_level=logging.INFO)
    def test_create_table(self):
        values = {
            'admin_name': 'VARCHAR(255) NOT NULL',
            'username': 'VARCHAR(255)',
            'password': 'VARCHAR(255)'
        }
        self.obj.create("pateint", **values)
        
        expected_query = "CREATE TABLE IF NOT EXISTS pateint (admin_name VARCHAR(255) NOT NULL, username VARCHAR(255), password VARCHAR(255));"
        self.obj.cursor.execute.assert_called_once_with(expected_query)
        self.obj.connection.commit.assert_called_once()

    @log_function(Logger('Use test function'), log_level=logging.INFO)
    def test_insert_table(self):
        values = {"admin_name": "admin_1", "username": "user", "password": "123456"}
        self.obj.insert("pateint", **values)
        expected_query = "INSERT INTO pateint (admin_name, username, password) VALUES ('admin_1', 'user', '123456');"
        self.obj.cursor.execute.assert_called_once_with(expected_query)
        self.obj.connection.commit.assert_called_once()

    @log_function(Logger('Use test function'), log_level=logging.INFO)
    def test_update_table(self):
        self.obj.update("pateint", "username ='user'", admin_name="admin_1", username="usersss", password="123456")
        expected_sql = ("UPDATE pateint SET admin_name = 'admin_1', username = 'usersss', password = '123456' WHERE username ='user';")
        self.obj.execute.assert_called_once_with(expected_sql)

    @log_function(Logger('Use test function'), log_level=logging.INFO)
    def test_delete_table(self):
        self.obj.delete("pateint", "username ='usersss'")
        expected_sql = "DELETE FROM pateint WHERE username ='usersss';"
        self.obj.execute.assert_called_once_with(expected_sql)


if __name__ == "__main__":
    unittest.main()
