class Students :
    def __init__ (self,fullname, age):
        self.name = fullname
        self.age = age

    def hello(self):        #This is method
        print("Welcome Student", self.name)
    def ages(self):
        print("Hey !,",self.name ,"Your age is ", self.age)

    def old(self):
        return self.age

s1 = Students("Arpit Sharma", 23)
print(s1.name, s1.age)
s1.hello()
s1.ages()

print(s1.old())