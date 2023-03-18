# Create a variable inside a function, with the same name as the global variable
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)  # Python is fantastic


myfunc()

print("Python is " + x)  # Python is awesome
