class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

Abhi = Employee()
Abhi.salary = 100000
Abhi.getSalary() # Employee.getSalary(harry)