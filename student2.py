class student2:
    grade =10
    name = "Urooj"
    def introduction(self):
        print("Hi I am a student ")
    def details(self):
        print("My name is", self.name)
        print("I study in grade", self.grade)
ob = student2()
ob.introduction()
ob.details()