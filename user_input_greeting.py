name = input("Enter your first name: ")
surname = input("Enter your last name: ")
#message = "Hello %s %s" % (name, surname) still works, but the next method was introduced in Python 3.6 and is cleaner.
message = f"Hello {name} {surname}"
print(message)