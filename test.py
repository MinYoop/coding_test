

var = ["a", "b"]

def func():
    global var
    var=["c"]

    print(var)


func()

print(var)