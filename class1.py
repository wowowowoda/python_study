class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

# test1
# b = Student("z3",90)

# b.age = 30 

# print(type(b)) 


class Student2(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
        
        
b = Student2("z3",100)
print(b.__name)


class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
        
    def get_name(self) :
        return self.__name
    def get_gender(self) :
        return self.__gender 
    
    def set_gender(self,gender) :
        self.__gender = gender 