from grade_functions import *

students = []

while True:
    print("\n=== MENU ===")
    print("1. Tambah")
    print("2. Tampil")
    print("3. Cari")
    print("4. Rata-rata")
    print("5. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        name = input("Nama: ")
        grade = int(input("Nilai: "))
        add_student(students, name, grade)

    elif pilihan == "2":
        show_students(students)

    elif pilihan == "3":
        name = input("Cari nama: ")
        print(find_student(students, name))

    elif pilihan == "4":
        print(average_grade(students))

    elif pilihan == "5":
        break