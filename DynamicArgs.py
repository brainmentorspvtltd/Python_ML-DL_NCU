## *args
## **kwargs
def emp(name,age,*address):
    print("Name : {}, Age : {}".format(name,age))
    print("Address : {}".format(address))

#emp('Ram',30,'Delhi')
#emp('Ram',34,'Delhi','Gurgaon','Noida')

def student(**details):
    print(details)

student(name = 'Ram', address = 'Delhi', hobby = 'cricket')
student(name = 'Shyam', address = 'UP')
student(name = 'Mohan',hobby = 'football', age = 15)
