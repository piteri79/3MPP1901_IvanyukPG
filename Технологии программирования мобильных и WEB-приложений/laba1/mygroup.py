groupmates = [
    {
        "name": "Пётр",
        "surname": "Иванюк",
        "exams": ["Математика", "ООП", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Сергей",
        "surname": "Табуреткин",
        "exams": ["Русский язык", "АиГ", "КТП"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Андрей",
        "surname": "Семенов",
        "exams": ["Литература", "ИС", "КТП"],
        "marks": [4, 3, 3]
    }
]

def print_students(students, a):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        if sum(student["marks"])/len(student["marks"]) >= int(a):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

a = input('Введите средний балл: ')
print_students(groupmates, a)
