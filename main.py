import loging
from menu import Menu, Item
from loging import Loging_Admin, Loging_Patient, Logging_docter


# import os
#
# os.system('cls')
def patient():
    patient_menu = Menu("Patient Menu")
    register_item = Item("sign or login", register_loging_patient)
    contact_us_item = Item("contact_us", contact_us)
    patient_menu.add_item(register_item)
    patient_menu.add_item(contact_us_item)
    patient_menu.display()
    patient_menu.execute()


def doctor():
    doctor_menu = Menu("doctor Menu")
    register_item = Item("sign or login", register_login_docter)
    contact_us_item = Item("contact_us", contact_us)
    doctor_menu.add_item(register_item)
    doctor_menu.add_item(contact_us_item)
    doctor_menu.display()
    doctor_menu.execute()


def admin():
    admin_menu = Menu("Admin Menu")
    register_item_admin = Item("sign or login", register_login_admin)
    contact_us_item = Item("contact_us", contact_us)
    admin_menu.add_item(register_item_admin)
    admin_menu.add_item(contact_us_item)
    admin_menu.display()
    admin_menu.execute()


def register_admin():
    register_admin_meni = Menu("Admin Menu")
    user_name = input("enter your username: ")
    password = input("enter your password: ")
    admin_name = input("enter your admin name: ")
    la = Loging_Admin()
    print(la.register(user_name, password, admin_name))
    register_admin_meni.display()
    register_admin_meni.execute()


def register_patient():
    register_user_menu = Menu("Patient Menu")
    patient_name = input("pls enter your name: ")
    patient_id = int(input("pls enter your id: "))
    age = int(input("enter your age: "))
    lp = Loging_Patient()
    print(lp.register(patient_id, patient_name, age))
    register_user_menu.display()
    register_user_menu.execute()


def register_docter():
    register_doctor_menu = Menu("Doctor Menu")
    docter_id = int(input("enter your docter_id: "))
    docter_name = input("enter your docter_name: ")
    age = int(input("enter your age: "))
    working_day = input("enter your working_day: ")
    salary = int(input("enter your salary: "))
    rd = Logging_docter()
    print(rd.register_doctor(docter_id, docter_name, age, working_day, salary))
    register_doctor_menu.display()
    register_doctor_menu.execute()


def loging_admin():
    loging_admin_menu = Menu("Admin Menu")
    user_name = input("enter your user_name: ")
    password = input("enter your password: ")
    la = Loging_Admin()
    print(la.loging(user_name, password))
    loging_admin_menu.display()
    loging_admin_menu.execute()


def loging_patient():
    loging_patient_menu = Menu("Patient Menu")
    patient_id = input("enter your patient_id: ")
    patient_name = input("enter your patient_name: ")
    lp = Loging_Patient()
    print(lp.loging(patient_id, patient_name))
    loging_patient_menu.display()
    loging_patient_menu.execute()


def loging_docter():
    loging_docter_menu = Menu("Docter Menu")
    docter_id = input("enter your docter_id: ")
    medical_system_code = input("enter your medical_system_code: ")
    pl = Logging_docter()
    print(pl.login(docter_id, medical_system_code))
    loging_docter_menu.display()
    loging_docter_menu.execute()


def register_loging_patient():
    register_loging_patient_menu = Menu("register loging patient")
    loging_item = Item("Loging", loging_patient)
    register_item = Item("Register", register_patient)
    register_loging_patient_menu.add_item(loging_item)
    register_loging_patient_menu.add_item(register_item)
    register_loging_patient_menu.display()
    register_loging_patient_menu.execute()


def register_login_docter():
    register_login_docter_menu = Menu("register loging Doctor")
    loging_item = Item("Loging", loging_docter)
    register_item = Item("Register", register_docter)
    register_login_docter_menu.add_item(loging_item)
    register_login_docter_menu.add_item(register_item)
    register_login_docter_menu.display()
    register_login_docter_menu.execute()


def register_login_admin():
    register_login_admin_menu = Menu("register loging admin")
    loging_item = Item("Loging", loging_admin)
    register_item = Item("Register", register_admin)
    register_login_admin_menu.add_item(loging_item)
    register_login_admin_menu.add_item(register_item)
    register_login_admin_menu.display()
    register_login_admin_menu.execute()


def contact_us():
    print("a work from maktab sharifs 100th cycle ,group 2")


menu = Menu("Main")
item_patient = Item("Patient", patient)
item_doctor = Item("Doctor", doctor)
item_admin = Item("Admin", admin)

menu.add_item(item_patient)
menu.add_item(item_doctor)
menu.add_item(item_admin)


menu.display()
menu.execute()
