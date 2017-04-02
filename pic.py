from imgproc import *
import math   



# Sort out camera stuff
#--------------------------------------------------------
my_camera = Camera(720, 480)					# Open webcam
image = my_camera.grabImage()					# Grab image from camera	
my_view = Viewer(image.width, image.height, "Shot Finder")	# Open a view the same size as captured image
my_view.displayImage(image)					# Display image


# Set up object variables
#--------------------------------------------------------
# General stuff
MyObjReturnedData = {}
ObjSearchData = {}
ObjectList = ['centre','counter']

# centre object stuff
# Centre should be somewhere near the centre of the image
SearchRadius = image.width/10
MidWidth = image.width/2
MidHeight = image.height/2
MinWidth = MidWidth - SearchRadius
MaxWidth = MidWidth + SearchRadius
MinHeight = MidHeight - SearchRadius
MaxHeight = MidHeight + SearchRadius

# Object search data
ObjSearchData['centre'] = {'MinWidth':MinWidth, 'MaxWidth':MaxWidth, 'MinHeight':MinHeight, 'MaxHeight':MaxHeight}
ObjSearchData['counter'] = {'MinWidth':5, 'MaxWidth':340, 'MinHeight':5, 'MaxHeight':230}

# Start looking for objects
#-------------------------------------------------------

# display the image on the viewer
my_view.displayImage(image)

waitTime(20000)


