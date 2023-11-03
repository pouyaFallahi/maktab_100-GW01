import psycopg2
import DBManager


class Database:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                port="YOUR_PORT",
                database="NAME_DATABASE",
                user="POSTGERSQL_USERNAME",
                password="YOUR_PASSWORD",
            )
            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create(self, table_name : str, **values : dict) -> None:
        '''This method creates database tables for us.'''

        query_for_create_patient_table = "CREATE TABLE IF NOT EXISTS {0} ({1});".format(table_name, ", ".join(
            (str(value[0]) + " " + str(value[1])) for value in values.items()))

        self.cursor.execute(query_for_create_patient_table)
        self.connection.commit()

    def insert(self, table_name : str, **values : dict) -> None:
        '''To create and enter new information'''
        query = "INSERT INTO {0} ({1}) VALUES ".format(table_name, ", ".join(str(key) for key in values.keys()))

        value_for_insert = []

        for value in values.values():
            if isinstance(value, float) or isinstance(value, int):
                value_for_insert.append("%s" % value)
            else:
                value_for_insert.append("'%s'" % value)

        query += "({});".format(", ".join(str(value) for value in value_for_insert))

        self.cursor.execute(query)
        self.connection.commit()

    def update(self, table: str, condition: str = None, **sets):
        '''To change and edit registered information'''
        parsed_values = []
        key = 0  # Static value for getting keys in items tuple
        value = 1  # Static value for getting values in items tuple
        for item in sets.items():
            if isinstance(item[value], float) or isinstance(item[value], int):
                parsed_values.append("%s = %s" % (item[key], item[value]))
            else:
                parsed_values.append("%s = '%s'" % (item[key], item[value]))

        sql = "UPDATE {0} SET {1} ".format(table, ", ".join(parsed_values))

        if condition:
            sql += "WHERE %s;" % condition
        else:
            sql += ";"
        self.execute(sql)

    def delete(self, table: str, condition: str) -> None:
        '''To clear table information'''
        sql = "DELETE FROM %s " % table
        if condition:
            sql += "WHERE %s;" % condition
        else:
            sql += ";"

        self.execute(sql)


 
x = Database()

#CREATE TABLE PATIENT
#x.create('patient',patient_id="INT PRIMARY KEY", patient_name="VARCHAR(150) NOT NULL", patient_age ="INT NOT NULL", patient_cos="INT")


#CREATE TABLE ADMIN
#x.create('admin', admin_name="VARCHAR(15) NOT NULL", userName="VARCHAR(100)", password="VARCHAR(100)")


#CREATE TABLE PATIENT_FILE
#x.create("patient_file", file_id="INT PRIMARY KEY", patient_id="INT", docter_id="INT", data_timeVisit="timestamp", patient_history="TEXT" )
#it -> FOREIGN KEY
#ALTER TABLE patient_file ADD CONSTRAINT patient_id FOREIGN KEY (patient_id) REFERENCES patient (patient_id); -> FOREIGN KEY

#CREATE TABLE DOCTOR
#x.create("docter", docter_id="INT PRIMARY KEY", docter_name="VARCHAR(150)", docter_age="INT", working_day="VARCHAR(100)", salary="INT NOT NULL")

#CREATE TABLE VISIT
#x.create("visit", visit_id="INT PRIMARY KEY", patient_id="INT NOT NULL", docter_id="INT NOT NULL", date_visit="TIMESTAMP", order_visit="TEXT", cost_visit="INT" )
