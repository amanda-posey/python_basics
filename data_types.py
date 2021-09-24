x = 10
y = '10'
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

student_grades = [9.1, 8.8, 7.5]
mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)

grade_dictionary = {'Mary': 9.1, 'Steve': 8.8, 'Mike': 7.5}
grades = grade_dictionary.values()
students = grade_dictionary.keys()
print(grades)
print(students)
