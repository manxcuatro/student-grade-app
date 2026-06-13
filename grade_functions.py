def add_students(students, name, grade):
    students.append({
        "name": name,
        "grade": grade
    })

def show_students(students):
    pass

def find_student(students, name):
    pass

def average_grade(students):
    if len(students) == 0:
        return 0
    
    total = sum(s["grade"] for s in students)
    return total / len(students)

