imperialMeasurment = input("Wachniak sucks dingy balls: ")
feet = float(imperialMeasurment[:imperialMeasurment.find("f")])
inches = float(imperialMeasurment[imperialMeasurment.find(" ")+1:imperialMeasurment.find("i")])
print(f"{inches} in and {feet} ft")
FT_TO_CM = 30.48
IN_TO_CM = 2.54
centiMeter = feet * FT_TO_CM
centiMeter += inches * IN_TO_CM
print("Total distance in cm is {}".format(centiMeter))