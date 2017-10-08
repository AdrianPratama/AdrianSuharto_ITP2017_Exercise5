def calculator(num1,num2,operator,format):
    if operator == "+":
        output = num1+num2
    elif operator == "-":
        output = num1-num2
    elif operator == "*":
        output = num1*num2
    elif operator == ":":
        output = num1/num2
    else:
        output = num1+num2

    if format == "integer":
        print(int(output//1))
        print("Output is an integer")
    elif format == "float":
        print(float(output))
        print("Output is a float")
    else:
        print("Unknown format!")

num1 = int(input("Please input integer 1:"))
num2 = int(input("Please input integer 2:"))
operator = input("Please input the operator:")
format = input("Please input the format:")
calculator(num1,num2,operator,format)
