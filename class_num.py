#ÿ��ʵ��������count�Զ�+1 
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