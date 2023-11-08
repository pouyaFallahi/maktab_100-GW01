import psycopg2

class Admin():
    def __init__(self): 
        
        self.connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="project",
            user="postgres",
            password="123456",
        )
        self.cursor = self.connection.cursor()


    def sum_salary_docter(self):
        self.cursor.execute("SELECT SUM(cost_visit) as sum_visit FROM visit ")
        results = self.cursor.fetchall()
        for row in results:
            sum_visit = row
            print(f'sum_visit:{sum_visit}')
        self.connection.close()
    def list_patient(self):
        
        self.cursor.execute("select patient_id,patient_name from patient")
        results=self.cursor.fetchall()
        for row in results:
            patient_id,patient_name=row
            print(f'patient_id : { patient_id} ,patient_name : {patient_name}')
        self.connection.commit()
    def list_docter(self):
        self.cursor.execute("select docter_id,docter_name from docter")
        results=self.cursor.fetchall()
        for row in results:
            docter_id,docter_name=row
            print(f'docter_id :{ docter_id } ,docter_name : {docter_name}')
        self.connection.close()
    def visit_each_docter_by_patient(self):
        
        self.cursor.execute("""
            SELECT doctor_id, patient_id, COUNT(visit_id) AS num_visits
            FROM visit
            GROUP BY doctor_id, patient_id
        """)
        results = self.cursor.fetchall()

        for row in results:
            doctor_id, patient_id, num_visits = row
            print("Doctor ID:", doctor_id, " Patient ID:", patient_id, " Number of Visits:", num_visits)
        self.connection.close()

    def visit_each_patient(self):
        
        self.cursor.execute("""
            SELECT patient_id, COUNT(visit_id) AS count_visit
            FROM visit
            GROUP BY patient_id
        """)
        results = self.cursor.fetchall()

        for row in results:
            patient_id, count_visits = row
            print( " Patient ID:", patient_id, " Number of Visits:", count_visits)
        self.connection.close()
        
    def incoming_hospital(self):
        self.cursor.execute("""
            SELECT 
                EXTRACT(WEEK FROM date_visit) AS week,
                EXTRACT(MONTH FROM date_visit) AS month,
                EXTRACT(YEAR FROM date_visit) AS year,
                SUM(cost_visit) AS total_income
            FROM visit
            GROUP BY week, month, year
            ORDER BY year, month, week
        """)
        results = self.cursor.fetchall()
        for row in results:
            week, month, year, total_income = row
            print("Week:", week, " , Month:", month, " , Year:", year, " , Total Income:", total_income)
        self.connection.close()


