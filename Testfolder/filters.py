from PIL import Image
def load_img(filename):
    imgObject = Image.open(filename)
    return imgObject

def show_img(imgObject):
    imgObject.show()

def save_img(imgObject, newImageName):
    imgObject.save(newImageName, "jpeg")
    show_img(imgObject)

    #obamacon filter
def obamacon(imgObject):
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)
    colorpixels = list(imgObject.getdata())
    list_length=len(colorpixels)
    for i in range(list_length):
    	#print(i)
    	redcolor = colorpixels[i][0]
    	bluecolor = colorpixels[i][1]
    	greencolor = colorpixels[i][2]
    	sum = redcolor + bluecolor + greencolor

    	print(sum)
    	if sum < 182:
    		colorpixels[i] = darkBlue
    	elif sum >= 182 and sum < 364:
    		colorpixels[i] = red
    	elif sum >= 364 and sum< 546:
    		colorpixels[i] = lightBlue
    	else:
    		colorpixels[i]= yellow
    filteredImage = Image.new("RGB", imgObject.size)
    filteredImage.putdata(colorpixels)
    return filteredImage
