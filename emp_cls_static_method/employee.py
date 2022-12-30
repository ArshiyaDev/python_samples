# classmethods and staticmethods
# from below youtube video
# https://www.youtube.com/watch?v=rq8cL2XMM5M
# 

class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay
        
        Employee.num_of_emps += 1 
    
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount 
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def calc_uk_tax(salary:float) -> float:
        if salary <= 50000:
            return (salary * 20) / 100
        elif 50000 < salary < 80000:
            return (salary * 35) / 100
        else: 
            return (salary * 45) / 100

    def __str__(self) -> str:
        return f"\n {self.first} {self.last} \n\
        {self.email} \n\
        {self.pay}"




