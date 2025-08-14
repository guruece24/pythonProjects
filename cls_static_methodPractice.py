class Employee:
    company = "HCL"

    def printCompany(self):
        print(self.company)

    @classmethod
    def change_Company(cls, newCompany):
        cls.company = newCompany

    @staticmethod
    def change_Company_Static(newCompany):
        company = newCompany
        print(f"inside static method {company}")


e = Employee()
e.printCompany()

Employee.change_Company("Infosys")
print(Employee.company)

Employee.change_Company_Static("ABB")
print(Employee.company)


#Another Program
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(54,4))