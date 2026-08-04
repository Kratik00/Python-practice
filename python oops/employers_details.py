class Employee:
    employee_count = 101

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.emp_id = 'e' + str(self.employee_count)
        Employee.employee_count += 1

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Designation: {self.designation}")
        print(f"Employee Id: {self.emp_id}")
    @classmethod
    def total_employee(cls):
        return cls.employee_count - 101

emp = Employee("Sandeep", 4000, "Peon")
emp.show_details()
print(emp.total_employee())