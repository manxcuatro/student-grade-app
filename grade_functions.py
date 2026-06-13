def add_students(students, name, grade):
    pass

def show_students(students):
    if len(students) ==0:
        print ("Belum Ada Data")
        return
    
    for i, s in enumerate(students, 1):
        print (f"{i}. {s['name']} - {s['grade']}")

def find_student(students, name):
    pass

def average_grade(students):
    pass