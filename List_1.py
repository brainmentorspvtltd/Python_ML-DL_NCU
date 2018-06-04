Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> emp = ['Ram',30,25000.00,'Delhi']
>>> emp[0]
'Ram'
>>> emp[0:3]
['Ram', 30, 25000.0]
>>> a = 'Delhi'
>>> a in emp
True
>>> import sys
>>> sys.getsizeof(a)
54
>>> import os
>>> os.startfile('notepad')
>>> 
