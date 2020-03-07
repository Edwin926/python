# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:19:17 2020

@author: CEC
"""

class Employee:
    'common base class for al employees'
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("Total Employee %d"%Employee.empCount)
    def displayEmployee(self):
        print("Name:",self.name,",Salary:",self.salary)
emp1=Employee("Zara",2000)
emp2=Employee("manni",5000)
emp3=Employee("Kevin",2500)
emp4=Employee("Leo",1500)
emp1.displayEmployee()
emp1.displayCount()
emp4.displayCount()