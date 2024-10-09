# -*- coding: utf-8 -*-
"""Python 102 - Assignment 5

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d0-bonTKM0S1XawOXOTbxE0CojGrJkor
"""

class Employee:
  def __init__(self, name, id, salary, years_employed):
    self.name = name
    self.id = id
    self.salary = salary
    self.years_employed = years_employed
  def __repr__(self) -> str:
    string = f'Employee: (Name:{self.name}, ID:{self.id}, Salary:{self.salary}, Years_Employed:{self.years_employed})'
    return string
  def __str__(self) -> str:
    string = ('\nEmployee Details:' +
              '\nName:' + str(self.name) +
              '\nID:' + str(self.id) +
              '\nSalary:' + str(self.salary) +
              '\nYears Employed:' + str(self.years_employed))
    return string

employee1 = Employee("H", 58649, 80000, 2.5)
print('Representation: ', repr(employee1))
print('String representation: ', employee1)

employee2 = Employee("J", 98245, 600000, 6)
print('\nRepresentation: ', repr(employee2))
print('String representation: ', employee2)

employee3 = Employee("K", 52639, 40000, 0.6)
print('\nRepresentation: ', repr(employee3))
print('String representation: ', employee3)