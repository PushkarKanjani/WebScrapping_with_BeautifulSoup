def increase(self):
       self.salary = self.salary * Employee.increment

    @classmethod
    def change_increment(myclass, amount):
        myclass.increment = amount