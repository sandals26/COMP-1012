import math
x1 = float(input("x1: ")) #co-ordianate relative to origin, in km
y1 = float(input("y1: ")) #co-ordianate relative to origin, in km
x2 = float(input("x2: ")) #co-ordianate relative to origin, in km
y2 = float(input("y2: ")) #co-ordianate relative to origin, in km
distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
angle = math.atan2((y2-y1),(x2-x1)) * 180/math.pi #Angle made from the x axis to hypotenuse made by the x and y co-ordinates
#arctan x = pi/2 - arctan(1/x)
slope = (y2-y1)/(x2-x1)
if slope <= 1:
    angle = slope - slope**3/3 + slope**5/5 - slope**7/7 + slope**9/9 - slope**11/11 + slope**13/13 - slope**15/15 + slope**17/17 - slope**19/19 + slope**21/21 - slope**23/23 + slope**25/25 - slope**27/27 + slope**29/29 - slope**31/31 + slope**33/33 - slope**35/35 + slope**37/37 - slope**39/39 + slope**41/41 - slope**43/43 + slope**45/45 - slope**47/47 + slope**49/49
else:
    print("other")
taylorSeries = 0
print("You will walk a distance of {:.3f}km, in {:.3f} hours at a speed of 4km per hour, at an angle of {:.2f} degrees".format(distance, distance/4, angle))