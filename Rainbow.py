import turtle

def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0)
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q

turtle.colormode(255)
sc = turtle.Screen()
pen = turtle.Turtle()

def semi_circle(col, rad, val):
    pen.color(col)
    pen.circle(rad, -180)
    pen.up()
    pen.setpos(val-85, -330)
    pen.down()
 
    pen.right(180)
 
 
sc.setup(2000, 700)
 
sc.bgcolor('black')
 
pen.right(90)
pen.width(10)
pen.speed(0)
 
for i in range(60):
    hue = i/60
    (r, g, b) = hsv_to_rgb(hue, 1.0, 1.0)
    R, G, B = int(255 * r), int(255 * g), int(255 * b)
    semi_circle((R,G,B), 10*(
      i + 8), -10*(i + 1))
 
pen.hideturtle()
