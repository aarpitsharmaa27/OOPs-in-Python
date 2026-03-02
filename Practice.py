class Students :
    def __init__(self, name , mark):
        self.name = name
        self.mark = mark

    def average (self):
        
        sum = 0
        for val in self.mark:
            sum += val
        print("Hi", self.name, "your avg score is :", sum/3)

s1 = Students("Arpit Sharma ", [90,87,92])
s1.average()

s1.name = "Sanjay"
s1.average()
