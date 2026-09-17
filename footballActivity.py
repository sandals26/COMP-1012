import math
INITIAL_SPEED = 19 #in m/s
ANGLE = math.pi/4 # in radians
DISPLACEMENT = 30 # in meters
GRAVITY = 9.8 #in m/s^2
HEIGHT_OF_GOALPOST = 3 #In meters
# t = d(m)/(v(m/s) * cos(theta)) = s
time = DISPLACEMENT/(INITIAL_SPEED*math.cos(ANGLE))
print("time the ball is in the air for {:.2f} seconds".format(time))
heightOfBall = INITIAL_SPEED*math.sin(ANGLE)*time - GRAVITY*(time**2)/2
print("The height that the ball reaches {} meters it is {:.2f} meters in the air".format(DISPLACEMENT,heightOfBall))
if(heightOfBall > HEIGHT_OF_GOALPOST):
    print("The ball went in the goal")
else:
    print("The ball was too low")