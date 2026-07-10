# Python OOP Project - Employee Management System

class Employee:
    def __init__(self,emp_id,name,age,salary):
        self.__emp_id = emp_id
        self.name = name
        self.age = age
        self.__salary = salary


    def dis(self):
        print("\n------ Employee Details ------")
        print("ID : ",self.__emp_id)
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Salary : ",self.__salary)


    def __del__(self):
        print("Object Deleted")

class Manager(Employee):
    def __init__(self,emp_id,name,age,salary,department):
        super().__init__(emp_id,name,age,salary)
        self.department = department

    def dis(self):
        super().dis()
        print("Department : ",self.department)

class Developer(Employee):
    def __init__(self,emp_id,name,age,salary,pro_lan):
        super().__init__(emp_id,name,age,salary)
        self.pro_lan = pro_lan

    def dis(self):
        super().dis()
        print("Programming Language : ",self.pro_lan)


def getdata():
    emp_id = int(input("\nEnter ID : "))
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    salary = int(input("Enter salary : "))

    return emp_id,name,age,salary


emp = None
manager = None
developer = None

while True:
    print("\n===== Employee Management System =====")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show Details")
    print("5. Check Subclass")
    print("6. Exit")

    ch = int(input("\nEnter your choice : "))

    if ch == 1:
        emp_id,name,age,salary = getdata()
        emp = Employee(emp_id,name,age,salary)

        print("\n✅ Employee Created Successfully!")

    elif ch == 2:
        emp_id,name,age,salary = getdata()
        department = input("Enter Department : ")

        manager = Manager(emp_id, name, age, salary, department)

        print("\n✅ Manager Created Successfully!")

    elif ch == 3:
        emp_id,name,age,salary = getdata()
        pro_lan = input("Enter Programming Language : ")

        developer = Developer(emp_id, name, age, salary, pro_lan)

        print("\n✅ Developer Created Successfully!")

    elif ch == 4:

        print("\n===== Show Details =====")
        print("1. Employee")
        print("2. Manager")
        print("3. Developer")

        choice = int(input("Enter Choice : "))

        if choice == 1:
            if emp is not None:
                emp.dis()
            else:
                print("\n❌ Employee Not Created!")

        elif choice == 2:
            if manager is not None:
                manager.dis()
            else:
                print("\n❌ Manager Not Created!")

        elif choice == 3:
            if developer is not None:
                developer.dis()
            else:
                print("\n❌ Developer Not Created!")

        else:
            print("\n❌ Invalid Choice!")

    elif ch == 5:
        print("\nManager is subclass of Employee : ",issubclass(Manager, Employee))
        print("Developer is subclass of Employee : ",issubclass(Developer, Employee))

    elif ch == 6:
        print("\nThank You! 🙏")
        break

    else:
        print("\n❌ Invalid Choice")