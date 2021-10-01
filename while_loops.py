a = 3

#while a > 0:
#    print(1)
# prints forever, which is why a while loop can be dangerous

username = ''

#while username != 'pypy':
#    username = input('Enter username: ')

while True:
    username = input("Enter username: ")
    if username == 'pypy':
        break
    else:
        continue