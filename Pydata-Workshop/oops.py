class Employee:
    increment = 2

    def __init__(self, fname, lname, salary, age):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.age = age
        self.increment = 5

    def increase(self):
        self.salary = self.salary * Employee.increment

    @classmethod
    def change_increment(myclass, amount):
        myclass.increment = amount

    def __add__(self, others):
        return self.salary + others.salary

        @staticmethod
        def isopen(day):
            if day == "sunday":
                return False
            else:
                return True


Pushkar = Employee("Pushkar", "Kanjani", 2000000, 18)
David = Employee("David", "Goggins", 24000000, 7)

print(Pushkar.fname)
print(Pushkar.lname)
print(Pushkar.age)
print(Pushkar.salary)
Pushkar.increase()
print(Pushkar.salary)
# print(Pushkar.__dict__)
Employee.change_increment(5.9)
Pushkar.increase()

print(David.fname)
print(David.lname)
print(David.age)
print(David.salary)
David.increase()
print(David.salary)
# print(David.__dict__)
Employee.change_increment(5.9)
Pushkar.increase()

print(Pushkar + David)


class encode(Employee):
    def _init_(self, fname, lname, salary, age, laptop, interest):
        super()._init_(fname, lname, salary, age)
        self.interest = interest
        self.laptop = laptop
