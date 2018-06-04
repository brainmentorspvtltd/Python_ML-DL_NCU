Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = []
>>> a.append(12)
>>> a
[12]
>>> a.append(18)
>>> a.append(14)
>>> a
[12, 18, 14]
>>> a.pop()
14
>>> a.append(23,45,14,22,56,18)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.append(23,45,14,22,56,18)
TypeError: append() takes exactly one argument (6 given)
>>> a.append([23,45,14,22,56,18])
>>> a
[12, 18, [23, 45, 14, 22, 56, 18]]
>>> a[2]
[23, 45, 14, 22, 56, 18]
>>> a[2][-1]
18
>>> b = a[-1]
>>> b
[23, 45, 14, 22, 56, 18]
>>> sorted(b)
[14, 18, 22, 23, 45, 56]
>>> sorted(b, reverse = True)
[56, 45, 23, 22, 18, 14]
>>> b.sort()
>>> b
[14, 18, 22, 23, 45, 56]
>>> tup_1 = (12,34,67,11,87,23)
>>> tup_1[0]
12
>>> tup_1[0:4]
(12, 34, 67, 11)
>>> tup_1[0] = 100
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    tup_1[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> emp = name,age,salary = 'Ram',30,30000
>>> emp
('Ram', 30, 30000)
>>> name
'Ram'
>>> age
30
>>> salary
30000
>>> a = 10
>>> a = 10,
>>> a
(10,)
>>> data = {'name':'Ram','age':30,'salary':450000}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['name']
'Ram'
>>> data.keys()
dict_keys(['name', 'age', 'salary'])
>>> data.items()
dict_items([('name', 'Ram'), ('age', 30), ('salary', 450000)])
>>> data
{'name': 'Ram', 'age': 30, 'salary': 450000}
>>> for i in data:
	print(i)

	
name
age
salary
>>> for i in data.items():
	print(i)

	
('name', 'Ram')
('age', 30)
('salary', 450000)
>>> set_1 = {23,45,11,12,15,17}
>>> set_2 = {19,18,17,12,23,45}
>>> set_1.intersection(set_2)
{17, 12, 45, 23}
>>> set_1.union(set_2)
{11, 12, 45, 15, 17, 18, 19, 23}
>>> 
