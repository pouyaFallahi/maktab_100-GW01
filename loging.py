import psycopg2
import bcrypt
class Loging_Admin:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                port="5432",
                database="hospital",
                user="pouya",
                password="1234",
            )
            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def __hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def __check_password(hashed_password, password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

    def register(self, username, password, admin_name):
        hashed_password = self.hash_password(password)

        try:
            self.cursor.execute("INSERT INTO admin (username, password, admin_name) VALUES (%s, %s, %s)", (username, hashed_password, admin_name))
            self.connection.commit()
            self.connection.close()
            return "Registration successful!"
        except psycopg2.IntegrityError:
            #نویسنده پویا فلاحی کم حافظه
            #معمولاً در مواردی ایجاد می‌شوند که تلاش برای افزودن داده به جدول دیتابیس باعث نقض محدودیت‌های اطلاعاتی (اعتبارسنجی داده) می‌شود
            #به عبارت دیگر، این خطاها به دلیل تلاش برای ایجاد رکوردهای تکراری یا نادرست در جداول رخ می‌دهند.

            self.connection.close()
            return "Username already exists. Please choose another one."

    def loging(self, username : str, password : str):
        self.cursor.execute("SELECT password FROM admin WHERE username=%s", (username))
        row = self.cursor.fetchone()

        if row and self.__hash_password(password).verify(password, row[2]):
            self.connection.close()
            return "Login successful!"
        else:
            self.connection.close()
            return "Login unsuccessful. Please check your username and password."


class Loging_Patient:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                port="5432",
                database="hospital",
                user="pouya",
                password="1234",
            )
            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def loging(self, patient_name, patient_id):
        self.cursor.execute("SELECT  patient_id FROM patient WHERE patient_name=%s", (patient_name))
        row = self.cursor.fetchone()

        if row[0] == patient_id and row[1] == patient_name:
            self.connection.close()
            return "Login successful!"
        else:
            self.connection.close()
            return "Login unsuccessful. Please check your username and password."

    def register(self, patient_id, patient_name, age):
        try:
            self.cursor.execute("INSERT INTO patient (patient_id,patient_name, patient_age) VALUES (%s, %s, %s)",
                                (patient_id, patient_name, age))
            self.connection.commit()
            self.connection.close()
            return "Registration successful!"
        except psycopg2.IntegrityError:
            # نویسنده پویا فلاحی کم حافظه
            # معمولاً در مواردی ایجاد می‌شوند که تلاش برای افزودن داده به جدول دیتابیس باعث نقض محدودیت‌های اطلاعاتی (اعتبارسنجی داده) می‌شود
            # به عبارت دیگر، این خطاها به دلیل تلاش برای ایجاد رکوردهای تکراری یا نادرست در جداول رخ می‌دهند.

            self.connection.close()
            return "Username already exists. Please choose another one."

class Logging_docter:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                port="5432",
                database="hospital",
                user="pouya",
                password="1234",
            )
            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        
    def login(self, docter_id, medical_system_code):
        self.cursor.execute(
            "SELECT docter_id, medical_system_code FROM doctor where docter_id=%s ,(docter_id,medical_system_code)")
        row = self.cursor.fetchone()

        if row[0] == docter_id and row[1] == medical_system_code:
            self.connection.close()
            return "Login successful!"
        else:
            self.connection.close()
            return "Login unsuccessful. Please check your username and password."

    def register_doctor(self, docter_id, docter_name, age, working_day, salary):
        try:
            self.cursor.execute("INSERT INTO docter (docter_id, docter_name, docter_age, working_day, salary) VALUES (%s, %s,%s, %s,%s)",
                                (docter_id, docter_name, age, working_day, salary))
            self.connection.commit()
            self.connection.close()
            return "Registration successful!"
        except psycopg2.IntegrityError:
            self.connection.close()
            return "Username already exists. Please choose an"
