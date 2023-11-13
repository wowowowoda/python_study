class Screen(object):
    
    def __init__(self,x = 16 ,y = 9) :
        self.__width = x  
        self.__height = y
        self.__resolution = x * y 
    
    @property   #读
    def width(self) :
        return self.__width 
    
    @property  #读
    def  height(self) :
        return self.__height 
     
    @property   # ֻ只读
    def resolution(self) :
        return self.__resolution 
     
    @width.setter  #写
    def width(self,value) :
        self.__width = value 
    
    @height.setter  #写
    def  height(self,value):
        self.__height = value 
        
