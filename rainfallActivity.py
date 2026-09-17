lakeArea = 2 #in km squred
surroundingArea = 100 #in km squared
CHANGE_IN_LAKE = 1 # in meters
#surroundingArea * rainfall / lake area = change in lake height
rainfall = CHANGE_IN_LAKE*lakeArea*(10**3)/surroundingArea #rainfall in mm
print("To raise the lake height by {} meter, it would have to rain {:.1f} millimeters".format(CHANGE_IN_LAKE, rainfall))

