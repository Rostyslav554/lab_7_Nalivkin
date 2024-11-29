students = {
    "Налівкін": (20, 3, 85.5),
    "Дзюба": (20, 1, 90.3),
    "Литвин": (21, 3, 99.0),
    "Кальченко": (20, 3, 88.9)
}

last_name = input("Введіть прізвище студента: ")

if last_name in students:
    student_info = students[last_name]
    print(f"Інформація про студента '{last_name}':")
    print(f"Вік: {student_info[0]}")
    print(f"Курс: {student_info[1]}")
    print(f"Середній бал: {student_info[2]}")
else:
    print("Такого студента немає в базі даних.")
