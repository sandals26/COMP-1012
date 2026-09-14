import math
x1 = float(input("x1: ")) #co-ordianate relative to origin, in km
y1 = float(input("y1: ")) #co-ordianate relative to origin, in km
x2 = float(input("x2: ")) #co-ordianate relative to origin, in km
y2 = float(input("y2: ")) #co-ordianate relative to origin, in km
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
angle = math.atan2((y2-y1),(x2-x1)) * 180/math.pi #Angle made from the x axis to hypotenuse made by the x and y co-ordinates
print("You will walk a distance of {:.3f}km, in {:.3f} hours at a speed of 4km per hour, at an angle of {:.3f} degrees".format(distance, distance/4, angle))