def calculator(num,format,operator):
    if num:
        output = num[0]
        if operator == "+" or operator == "addition" or operator == "":
            for i in num[1:]:
                output += i
        elif operator == "-" or operator == "subtraction":
            for i in num[1:]:
                output -= i
        elif operator == "*" or operator == "multiplication":
            for i in num[1:]:
                output *= i
        elif operator == "/" or operator == "division":
            for i in num[1:]:
                output /= i

        if format == "integer":
            return print(int(output//1))
        elif format == "float":
            return print(float(output))
        elif format == "":
            return print(output)
        else:
            print("Unknown format!")
    else:
        raise Exception("No input detected!")

def check(numbers):
    list = []
    if numbers == "":
        return list
    elif len(numbers) == 1:
        list.append(int(numbers))
        return list
    elif "," in numbers:
        numbers = numbers.split(",")
        for i in numbers:
            if "." in i:
                list.append(float(i))
            elif "." not in i:
                list.append(int(i))
        return list

numbers = input("Your list of number please (Example: 1,2,3,4,5) :")
num = check(numbers)
operator = input("Please input the operator:")
format = input("Please input the format:")
calculator(num,format,operator)




