class Students():
    def __init__ (self,name,marks):
        self.name = name
        self.marks = marks
        
        print("Adding name and age of New Students...")
        #Constructor called

s1 = Students("Arpit",45)
print(s1.name, s1.marks)
# Name Called
# Again constructor called

s2 = Students("Sharmaji", 48)
print(s2.name, s2.marks) 
# Name Called
# Again constuctor Called 

s3 = Students("Sanjay", 49)
print(s3.name, s3.marks)
