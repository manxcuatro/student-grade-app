def add_students(students, name, grade):
    pass

def show_students(students):
    if len(students) ==0:
        print ("Belum Ada Data")
        return
    
    for i, s in enumerate(students, 1):
        print (f"{i}. {s['name']} - {s['grade']}")

def find_student(students, name):
    for s in students:
        if s["name"].lower() == name.lower():
            return s
        return None

def average_grade(students):
    pass