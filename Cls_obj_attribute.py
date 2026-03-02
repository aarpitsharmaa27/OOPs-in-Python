class Students:

    college_name = "CGC Landran"    #class attribute
    name = "Anonymous"          # class object stored in single memory
    
    def __init__(self, name, age):  
        self.name = name            #Object attribute
        self.age = age

s1 = Students("Arpit", 23)
print(s1.name, s1.age) 
print(Students.college_name)

# Only object attribute name got printed because
# object > class

