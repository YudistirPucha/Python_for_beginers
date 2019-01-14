students = [] #created empty list

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student.title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

#i want to add student name
def add_student(name,student_id =332):
    student = {"name": name, "student_id": student_id}
    students.append(name)


def save_file(student):
    try:
        f =open("student.txt ", "a")  # append = "a"
        f.write(student + " | " + students_id + "\n")
        f.close()
    except Exception:
        print("could not save file")

def read_file():
    try:
        f = open("student.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


read_file()#see the list of names
print_students_titlecase()

student_name = input("enter studen name")
students_id = input("enter student ID :")

add_student(student_name, students_id)
save_file(student_name)

