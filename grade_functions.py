def add_students(students, name, grade):
    pass

def show_students(students):
    pass

def find_student(students, name):
    for s in students:
        if s["name"].lower() == name.lower():
            return s
        return None

def average_grade(students):
    pass