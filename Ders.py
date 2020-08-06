class Employee:
    raise_amnt = 1.04
    def __init__(self, firstName, lastName, email, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.pay = pay
    
    def fullname(self):
        return "{} {}".format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)
        return self.pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amnt = amount




emp_1 = Employee("Ramazan","SARIBAY", "ramazansaribay@gmail.com", 4000)
emp_2 = Employee("Asli", "YAZIR", "asliyazir@gmail.com", 5000)





Employee.raise_amnt = 1.06
emp_1.raise_amnt = 1.07
print(emp_1.firstName)
print(emp_1.pay)
print(emp_1.raise_amnt)
print(Employee.raise_amnt)

print(emp_2.raise_amnt)
print(Employee.raise_amnt)

print(emp_1.__dict__)
print(emp_1.fullname())
print(emp_1.apply_raise())
print(emp_2.apply_raise())

