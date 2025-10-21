class Students:
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade

    def studying(self):
        print(f"{self.name} is studying")

p1=Students("Ruf", 12)
p2=Students("Dark", 15)

p1.studying()
print(p1)
