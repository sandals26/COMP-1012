LAKE_AREA = 2 #in km squred
COLLECTION_AREA = 100 #in km squared
CHANGE_IN_LAKE = 1 # in meters
#surroundingArea * rainfall / lake area = change in lake height
rainfall = CHANGE_IN_LAKE*LAKE_AREA*(10**3)/COLLECTION_AREA #rainfall in mm
print("To raise the lake height by {} meter, it would have to rain {:.1f} millimeters".format(CHANGE_IN_LAKE, rainfall))

