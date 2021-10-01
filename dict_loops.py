student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

for grade in student_grades.values():
    print(grade)

for grade in student_grades.keys():
    print(grade)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))

for number in phone_numbers.values():
    print(number.replace('+', '00'))