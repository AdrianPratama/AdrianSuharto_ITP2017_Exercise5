a = lambda x : x*x
print(a(5))

b = lambda ax, ay: (ax*ax + ay*ay)**(0.5)
print(b(3,4))

c=lambda *bx: sum(bx)/len(bx)
print(c(1,2,6))

d=lambda by: "".join(set(by))
print(d("Thisisgospel"))

def e(cx):
    return cx*cx
print(e(5))

def f(dx, dy):
    return (dx*dx+dy*dy)**(0.5)
print(f(3,4))

def g(*cy):
    return sum(cy)/len(cy)
print(g(1,2,6))

def h(y):
    return "".join(set(y))
print(h("Forthefallenones"))
