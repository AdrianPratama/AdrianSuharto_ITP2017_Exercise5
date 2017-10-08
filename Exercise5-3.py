def hypotenuse(a,b):
    try:
        return (a+b).sqrt()
    except TypeError:
        return None

c = int(input("Please input number 1 here"))
d = int(input("Please input number 2 here"))
hypotenuse(c,d)

e = str(input("Please input string 1 here"))
f = str(input("Please input string 2 here"))
hypotenuse(e,f)

g = int(input("Please input integer here"))
h = str(input("Please input string here"))
hypotenuse(g,h)
