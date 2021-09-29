def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

mylist = [4, 5, 6, 9, 1]
stanley = [9, 31, 49, 119]
student_grades = {'Mary': 9.1, 'Sim': 8.8, 'John': 7.5}

print(mean(student_grades))

x = 1
y = 1

if x == 1 and y == 0:
    print('Yes')
else:
    print('No')

z = -10
if z * 2 > z:
    print('Greater')
else: 
    print('Less or Equal')

def foo(x, array):
    if x in array:
        return True
    else:
        return False

print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print (foo(1, ['1', 2, 3]))

if isinstance(x, int) or isinstance(x, float) or x == '1':
    print('Valid type!')
else:
    print('Not valid!')

def foopass(str):
    if len(str) < 8:
        return False
    else: 
        return True

print(foopass('mypass'))
print(foopass('mylongpassword'))

def footemp(temp):
    if temp > 7:
        return 'Warm'
    if temp < 7:
        return 'Cold'

print(footemp(10))
print(footemp(5))

a = 3
b = 1

if a > b:
    print('a is greater than b')
elif a == b:
    print('a is equal to b')
else:
    print('a is less than b')