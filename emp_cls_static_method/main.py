from employee import Employee

emp1 = Employee('Mike', 'Brown' , 40000)
emp2 = Employee('Sarah', 'Hudson' , 55000)


##############################

emp_str1 = 'John-Doe-70000'
emp_str2 = 'Steve-Smith-30000'
emp_str3 = 'Babak-Jahangiri-90000'

## its not a good method everytime parse the string
#  we can make a static emthod to do this in the class

#first, last, pay = emp_str1.split('-')
#new_emp_1 = Employee(first,last,pay)

#print(Employee.raise_amt)

Employee.set_raise_amt(1.05)
#emp1.set_raise_amt(1.05)  this also works
#emp2.set_raise_amt(1.05)  this also works


#create new instance from string with static method
new_emp1 = Employee.from_string(emp_str1)
print(new_emp1) # whitout magic method __str__  : <employee.Employee object at 0x7ff4a7ef5310>

#calculate tax base on salary
print(Employee.calc_uk_tax(55000))


#print(emp1.raise_amt)
#print(emp2.raise_amt)




