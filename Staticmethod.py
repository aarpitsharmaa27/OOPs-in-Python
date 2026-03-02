#-------------Statis Methods----------------#

#   Methods that don't use the parameter (work at class level)

class Students:
    def __init__(self,name,age):
        self.name = name
        self.age =  age
    
    
    @staticmethod       #to call function withour self we use static method
    def hello():    # if i call this function without self it shows error
        print("HEllo")
    
s1 = Students("Arpit", 23)
print(s1.name,s1.age)
s1.hello()