class Students:
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade

class Ruf(Students):
    def __init__(self, name, grade, vibe):
        super().__init__(name, grade)
        self.vibe=vibe

    def get_info(self):
        return f"very vibe is name {self.name}m "
p1=Ruf("Ruf", "12", "very")

print(p1.get_info())