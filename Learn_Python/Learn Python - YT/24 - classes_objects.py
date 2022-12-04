from Students import Student

student1 = Student('Rob', 'I.T', 3.5, True)
student1.hello()
student2 = Student('Tom', 'Business', 2.5, False)
student2.major = 'Marketing'
print(student2.major)
student2.hello()

print(student1.on_honor_roll())
print(student2.on_honor_roll())
