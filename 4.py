list_students_previously_receiving_scholarship = ["Иванов", "Петров", "Зайцева", "Галкина", "Смирнова"]
list_students_result_session = ["Иванов", "Медведев", "Зайцева", "Ворошилова", "Смирнова"]

list_result_session = [
    {"информатика": 4, "высшая алгебра": 5, "философия": 3, "история": 4},
    {"физика": 4, "высшая алгебра": 5, "философия": 4, "история": 4},
    {"информатика": 4, "мат анализ": 3, "философия": 3, "история": 4},
    {"информатика": 4, "высшая алгебра": 5, "английский": 4, "история": 4},
    {"информатика": 4, "высшая алгебра": 5, "философия": 4, "история": 4}
]

students_dict = dict(zip(list_students_result_session, list_result_session))

students_with_scholarship = []

for student in list_students_previously_receiving_scholarship:
    if student in students_dict:
        grades = students_dict[student].values()
        if all(mark > 3 for mark in grades):
            students_with_scholarship.append(student)
            
            
for student in students_with_scholarship:
    print(student)
    
print(students_dict)