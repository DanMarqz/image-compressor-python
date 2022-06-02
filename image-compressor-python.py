from PIL import Image

# Input for the user
imageRoute = input(':: ~ Enter the path and name of the image to convert > ')
imageNewName = input(':: ~ Enter the name of the new image to export with its extension [.jpg, .png...] > ')
imageNewRoute = input(':: ~ Enter the destination where the image is going to be exported [By default it is saved in the image path] > ')

# Variables to define the route without the name of the image
myList = []
countDirBar = imageRoute.count('/')
counter = 0

# Loop to get the route without the name of the image
while (counter < countDirBar):
  if imageRoute.find('/', counter) == 0:
    myList.append(0)
    counter = counter + 1
  else:
    found = imageRoute.find('/', myList[counter - 1] + 1)
    myList.append(found)
    counter = counter + 1

# Define the route to export image
if imageNewRoute == '' :
  imageNewRoute = imageRoute[ 0 : myList[len(myList) - 1] + 1 ]
else :
  imageNewRoute = imageNewRoute

# Process to export the image
myImage = Image.open(imageRoute)
myImage = myImage.convert('RGB')
myImage.save( imageNewRoute + imageNewName  , quality = 30 )

print(':: ~ Image compressed successfully! The new image is saved in the following route: ' + imageNewRoute + imageNewName)
