from Tkinter import *
import math
master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()
centerX = float(100)
centerY = float(50)
width = float(160)
hight = float(50)
angle = float(45)
#fuer die funktion create_CoolRectangle // for the function create_CoolRectangle
Ax = centerX-width/2
Ay = centerY+hight/2
b = (centerX-Ax)
a = (Ay-centerY)
Radius = math.sqrt(a*a+b*b) #nur ein bischen Pytagoras // just a bit of Pytagoras
tanAlpha = b/a
Alpha = math.atan(tanAlpha) #der untere Winkel des Dreickes AMP (P ist der Mittelpunkt der Strecke AD) // the bottom angle of the triangle AMP (when P is the in the middle of A and D) ) 
Beta = math.radians(180-(180-angle)/2-math.degrees(Alpha)) #der obere Winkel des Dreieckes QA'A // the top angle of the triangle QA'A 
AA1 = 2*(math.sin(math.radians(angle/2))*(Radius)) #wir teilen erst das gleichschenklige Dreieck AA'M in zwei rechtwinklige auf (angle/2), ermitteln dann das lengenverhaeltnis der Hypotenuse (Radius) zu Gegenkathete (sin(...)), dann die Laenge der Gegenkathete (sin(...)/Radius), und schlieslich die laenge der ganzen Seite AA' (2*(...)) // at first we split the isosceles triangle AA'M in two rigth-angeld ones (angle/2), we go on with getting the hypotenuse's (Radius) ration to the angles opposite leg (sin(...)), then the opposite leg's absolut lenght (sin(...)/Radius), and finish with the lenght of AA'(2*(...)) 
A1x = Ax+(1/math.sin(math.radians(Beta)))*AA1
A1y = Ay+(1/math.cos(math.radians(Beta)))*AA1
w.create_polygon(A1x, centerY, centerX, centerY, A1x, A1y, fill = "white", outline = "black")

print "Ax =", Ax
print "Ay =", Ay
print "a =", a
print "b =", b
print "Radius =", Radius
print "tanAlpha =", tanAlpha
print "Alpha =", Alpha, math.degrees(Alpha)
print "Beta =" , Beta, math.degrees(Beta)
print "AA' = " , AA1
print "A'x =" , A1x
print "A'y =" , A1y
print math.sin(math.radians(angle/2))*Radius
print (1/math.cos(math.radians(Beta)))*AA1
w.create_polygon(Ax, Ay, centerX, Ay, centerX, centerY, fill = "white", outline = "black")

mainloop()
