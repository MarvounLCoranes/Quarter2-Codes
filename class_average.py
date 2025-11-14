students = int(input("Enter number of students:"))
subject = int(input("Enter number of subjects:"))
average = 0
grade = 0
class_av = 0
for i in range(1,students+1):
    average = 0
    print("Student",i)
    for j in range(0,subject):
        grade = 0
        grade = int(input("Enter Score:"))
        average = average + grade
    average = average/subject
    print("Average for Student ", i, " = ",average)
    class_av = class_av + average
class_av = class_av/students
print("Class Average = ",class_av)