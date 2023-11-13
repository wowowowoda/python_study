class Student(object):
    
    count = 0

    def __init__(self, name = "a"):

        Student.count += 1
        
b = Student() 

print(b.count)
c = Student() 
print(b.count )