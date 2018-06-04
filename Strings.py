Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str_1 = 'hello world'
>>> str_1[0]
'h'
>>> str_1[5]
' '
>>> str_1[-1]
'd'
>>> str_1[-2]
'l'
>>> str_1[0:5]
'hello'
>>> str_1[0:4]
'hell'
>>> str_1[0:10:2]
'hlowr'
>>> dir(str_1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str_1.capitalize()
'Hello world'
>>> str_1.find('l')
2
>>> str_1.rfind('l')
9
>>> str_1.find('l',3)
3
>>> str_1[0] = 'bye'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    str_1[0] = 'bye'
TypeError: 'str' object does not support item assignment
>>> str_2 = 'world'
>>> str_2[:]
'world'
>>> str_2[::-1]
'dlrow'
>>> str_2[:-1]
'worl'
>>> 
