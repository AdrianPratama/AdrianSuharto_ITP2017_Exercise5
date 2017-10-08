def log(func):
    def func_wrapper(name):
        print("Omae wa mo shindeiru")
        func(message)
    return func_wrapper

@log
def my_function(message):
    print(message)

message = input("Please input message here:")
my_function(message)
