import getpass
def decorator_un(print_func):
    
    def testun():
        username = getpass.getuser()
        if username == "claudiaacerra":
            print("****You Have Correct Permissions****")
            return print_func()
        else:
            return "wrong user"
    return testun

@ decorator_un
def print_to_file():
    with open("file.txt", "r") as f:
        data = f.readlines()
        for num, line in enumerate(data, 1):
            print(num, line)

    return "****Success****"

print(print_to_file())