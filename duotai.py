class Animal(object ):
    
    def run(self) :
        print("animal is running ") 
        
class Cat(Animal) :
    
    def run(self) : 
        print("cat is runing .. ")


def run_twice(Animal):
    Animal.run()
    Animal.run()

cat = Cat() 
animal = Animal()

run_twice(animal ) 
