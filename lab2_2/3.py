import turtle

turtle.shape('turtle')


turtle.penup()
with open ('new_file', 'r') as n:
    a=n.readlines()
    a = [_.rstrip() for _ in a]
    turtle.penup()
    four=a[0:12]
    one=a[12:24]
    zero=a[24:35]
    seven=a[35:48]

    b=(one,four,seven,one,zero,zero)
    for item in b:
        for i in item:
            eval(i)