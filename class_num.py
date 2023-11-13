#每次实例化对象count自动+1 
class Student(object) :
    
    count = 0 
    
    def __init__(self,name = "a") :
        self.name = name 
        Student.count += 1 

b = Student("b")
print(b.name) 
print(b.count)
c = Student()
print(c.count) 