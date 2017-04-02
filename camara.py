from imgproc import *
import math   

def FindObject (image, ObjSearchData, ObjectName):
	ObjectFound = False
	acc_x = 0
	acc_y = 0
	acc_count = 0
	print "Printing stuff..."
	print image
	print ObjSearchData
	print ObjectName
	print ObjSearchData['MinWidth']
	print "Hello I am inside function!"
	while ObjectFound is False:
	       	print "Searching for " + ObjectName + " within widths... " + str(ObjSearchData['MinWidth']) + " to " + str(ObjSearchData['MaxWidth'])
        	print "Searching for " + ObjectName + " within height... " + str(ObjSearchData['MinHeight']) + " to " + str(ObjSearchData['MaxHeight'])
	
        	# Itterate over every pixel in search area
        	for x in range(ObjSearchData['MinWidth'], ObjSearchData['MaxWidth']):

                	# colour pixel edges of search area
                	image[x, ObjSearchData['MinHeight']] = 0, 255, 255
                	image[x, ObjSearchData['MaxHeight']] = 0, 255, 255

               		for y in range(ObjSearchData['MinHeight'], ObjSearchData['MaxHeight']):
				# colour pixel edges of search area	
                        	image[ObjSearchData['MinWidth'], y] = 0, 255, 255
                        	image[ObjSearchData['MaxWidth'], y] = 0, 255, 255

				# get the value of the current pixel
                        	red, green, blue = image[x, y]
                        
				#print "Width = " + str(x) + " Height = " + str(y) + " Data = " + str(image[x,y])
                        
				if ObjectName == "centre":
					# Check if pixel is black
                        		if red < 110 and blue < 110 and green < 110:
                                		# accumulate x and y of found pixel
                                		acc_x += x
                                		acc_y += y
                                		# increment the accumulated pixels' count
                                		acc_count += 1
                                		# colour pixels which pass the test green
                                		image[x, y] = 0, 255, 0

				if ObjectName == "counter":
               				# check if pixel is red
		                        if red > green and red > blue:
               				        if red > 65 and red < 115:
                                        		if blue < 45 and blue > 5:
                                                		if green < 35 and green > 10:
                                                        		# accumulate x and y of found pixel
                                                        		acc_x += x
                                                        		acc_y += y
                                                        		# increment the accumulated pixels' count
                                                        		acc_count += 1
                                                        		# colour pixels which pass the test green
                                                        		image[x, y] = 255, 255, 0


 		# check the accumulator is greater than 0, to avoid a divide by 0
       		if acc_count > 0:
       			# calculate the mean x and y positions
       			mean_x = acc_x / acc_count
     			mean_y = acc_y / acc_count
                
			# draw a small cross in red at the mean position
               		image[mean_x + 0, mean_y - 1] = 255, 0, 0
               		image[mean_x - 1, mean_y + 0] = 255, 0, 0
               		image[mean_x + 0, mean_y + 0] = 255, 0, 0
               		image[mean_x + 1, mean_y + 0] = 255, 0, 0
               		image[mean_x + 0, mean_y + 1] = 255, 0, 0
	
			print "Found centre of " + ObjectName
			print "mean_x = " + str(mean_x)
			print "mean_y = " + str(mean_y)			
	
			ObjectFound = True

	return {'image':image, 'mean_x':mean_x, 'mean_y':mean_y}   


# Sort out camera stuff
#--------------------------------------------------------
my_camera = Camera(360, 240)					# Open webcam
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
for ObjectName in ObjectList:
	print "Finding Object = " + ObjectName
	ready = raw_input("Hit a key to continue")
	print ready 	
	if ready <> 0:
		print "OK. The current MyObjData is ..."
		MyObjReturnedData[ObjectName] = FindObject (image, ObjSearchData[ObjectName], ObjectName)
		print "My current object is... " + ObjectName
		print MyObjReturnedData[ObjectName]
	else:
		break;
print "Returned data..."
print MyObjReturnedData['centre']
print MyObjReturnedData['counter']

dist = math.hypot(MyObjReturnedData['counter']['mean_x'] - MyObjReturnedData['centre']['mean_x'], MyObjReturnedData['counter']['mean_y'] - MyObjReturnedData['counter']['mean_y'])


print "Distance from the centre = " + str(dist)


# display the image on the viewer
my_view.displayImage(image)

waitTime(0000)


