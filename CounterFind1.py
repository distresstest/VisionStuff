from imgproc import *
import math   


# Set up inital variables/constants
MidSqrConst = 4


# open the webcam
my_camera = Camera(360, 240)

# grab an image from the camera
image = my_camera.grabImage()

# open a view, setting the view to the size of the captured image
my_view = Viewer(image.width, image.height, "Shot Finder")


my_view.displayImage(image)

# Take a reference image and find the centre

print "Looking for centre point"

# Centre should be somewhere near the centre of the image

# initialise x and y position accumulators
acc_x = 0
acc_y = 0
acc_count = 0

CentreFound = False
SearchRadius = image.width/16
MidWidth = image.width/2
MidHeight = image.height/2

MinWidth = MidWidth - SearchRadius
MaxWidth = MidWidth + SearchRadius
MinHeight = MidHeight - SearchRadius
MaxHeight = MidHeight + SearchRadius

while CentreFound is False:
	print "Searching for centre within widths... " + str(MinWidth) + " to " + str(MaxWidth)
        print "Searching for centre within height... " + str(MinHeight) + " to " + str(MaxHeight)
	
	# Itterate over every pixel in search area
        for x in range(MinWidth, MaxWidth):

		# colour pixel edges of search area
 		image[x, MinHeight] = 0, 255, 255
                image[x, MaxHeight] = 0, 255, 255
			
                for y in range(MinHeight, MaxHeight):
	                image[MinWidth, y] = 0, 255, 255
       			image[MaxWidth, y] = 0, 255, 255

			#	print "Analysing pixel in column " + str(x) + " row " + str(y) 
                        # get the value of the current pixel
                        red, green, blue = image[x, y]
			#print "Width = " + str(x) + " Height = " + str(y) + " Data = " + str(image[x,y])
                        # Check if pixel is black
                        if red < 110 and blue < 110 and green < 110:
                        	# accumulate x and y of found pixel
                                acc_x += x
                                acc_y += y
                                # increment the accumulated pixels' count
                                acc_count += 1
                                # colour pixels which pass the test green
                                image[x, y] = 0, 255, 0
							
        # check the accumulator is greater than 0, to avoid a divide by 0
        if acc_count > 0:
                # calculate the mean x and y positions
                CPmean_x = acc_x / acc_count
                CPmean_y = acc_y / acc_count
                
		# draw a small cross in red at the mean position
                image[CPmean_x + 0, CPmean_y - 1] = 255, 0, 0
                image[CPmean_x - 1, CPmean_y + 0] = 255, 0, 0
                image[CPmean_x + 0, CPmean_y + 0] = 255, 0, 0
                image[CPmean_x + 1, CPmean_y + 0] = 255, 0, 0
                image[CPmean_x + 0, CPmean_y + 1] = 255, 0, 0
	
		print "Found centre point!"	
		print "Centre Point mean_x = " + str(CPmean_x)
		print "Centre Poin mean_y = " + str(CPmean_y)			
	
	CentreFound = True

# display the image on the viewer
my_view.displayImage(image)

waitTime(10000)


# Take a throw and analyse the position

print "Please take a throw!!!"

print "Now looking for counter"

bob = 1

#while True:
if bob >= 1:
	MinWidth = 50 
	MaxWidth = 150
	MinHeight = 75 
	MaxHeight = 152
        
	#x and y position accumulators 
	acc_x = 0 
	acc_y = 0 

	# number of pixels accumulated 
	acc_count = 0 
        
        # grab an image from the camera
        my_image = my_camera.grabImage()
	
	print "Searching for centre within widths... " + str(MinWidth) + " to " + str(MaxWidth)
        print "Searching for centre within height... " + str(MinHeight) + " to " + str(MaxHeight)

        # Itterate over every pixel in search area
        for x in range(MinWidth, MaxWidth):

                # colour pixel edges of search area
                image[x, MinHeight] = 0, 255, 255
                image[x, MaxHeight] = 0, 255, 255

                for y in range(MinHeight, MaxHeight):
                        image[MinWidth, y] = 0, 255, 255
                        image[MaxWidth, y] = 0, 255, 255

			# get the value of the current pixel 
			red, green, blue = image[x, y] 
                        #print "Width = " + str(x) + " Height = " + str(y) + " Data = " + str(image[x,y])
			
			ColCat = False		
			
			# Check if pixel is black	
			if red < 70 and blue < 70 and green < 70:
				image[x, y] = 0, 0, 0
          			ColCat = True

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
							ColCat = True

			# If ColCat Still false then set to white
			#if ColCat == False:
			#	image[x, y] = 255, 255, 255 

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

		print "Counter mean_x = " + str(mean_x)
		print "Counter mean_y = " + str(mean_y)
	

        # display the image on the viewer
        my_view.displayImage(image)

dist = math.hypot(mean_x - CPmean_x, mean_y -CPmean_y) 

print "CPmean_x = " + str(CPmean_x)
print "mean_x = " + str(mean_x)

print "Distance = " + str(dist)

waitTime(15000)

