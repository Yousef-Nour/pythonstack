local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"
# in the same file, add the following below the User class
if __name__ == "__main__":
    print(__name__)
    print(locals())
    print("directly")
    print(square(5))
    user = User("Anna")
    print(user.name)
    print(user.say_hello())
else:
    print("imported")
    print(__name__)
    print(locals())

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
  