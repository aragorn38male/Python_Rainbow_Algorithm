import turtle

def hsv_to_rgb(h):
    i = int(h*6.0)
    f = (h*6.0) - i
    q = (1.0 - f)
    i = i%6
    if i == 0:
        return 1.0, f, 0.0
    if i == 1:
        return q, 1.0, 0.0
    if i == 2:
        return 0.0, 1.0, f
    if i == 3:
        return 0.0, q, 1.0
    if i == 4:
        return f, 0.0, 1.0
    if i == 5:
        return 1.0, 0.0, q

turtle.colormode(255)
sc = turtle.Screen()
pen = turtle.Turtle()

def semi_circle(col, rad, val):
    pen.color(col)
    pen.circle(rad, -180)
    pen.up()
    pen.setpos(val-85, -325)
    pen.down()
 
    pen.right(180)
 
sc.setup(2000, 700)

sc.bgcolor('black')
 
pen.right(90)
pen.width(10)
pen.speed(0)

n = 60
for i in range(n):
    hue = i/n
    (r, g, b) = hsv_to_rgb(hue)
    R, G, B = int(255 * r), int(255 * g), int(255 * b)
    semi_circle((R,G,B), 10*(
      i + 8), -10*(i + 1))
 
pen.hideturtle()
