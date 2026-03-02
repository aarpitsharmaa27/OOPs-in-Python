class Students:
    
    year = "Student's of the Year"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

print(Students.year)
s1 = Students("Arpit", 23)
s2= Students("Keshav", 44)
print(s1.name, s1.age)
print(s2.name, s2.age)
