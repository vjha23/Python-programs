"""program1 - create a program that ask user to enter their name and thier age
print out message that will tell them the year that they will turn 95 year old """
import datetime
print('Enter the Name')
name=input('Name: \n')
print('Enter the age')
age=input('Age: \n')
value=int((95-age) + datetime.now().year)
print('your age in 1995 year  is %s' ,value)
