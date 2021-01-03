import random



#basically, anytime a new rectangle is created, it is added into this list of rectangle objects as well as boolean values that change depeneding on how the coresponding
# rectangle goes into the recursive function. 

almightyListOfRects = [[]]

class svgTag:
    def __init__(self, height, width):
        self.height = height
        self.width = width

class Rectangle:
    def __init__(self, height, width, x, y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        
def writeHeader(File):

    
    File.write("<html>\n<head>\n</head>\n")

def writeFooter(File):

    
    File.write("<footer>\n\n\n</footer>")

def divideIntoFour(File, initialRectangle):

    

    # establish random height/width from SVG dimensions as well as compliments to them.

    randHeight = random.randrange(400,initialRectangle.height)
    randWidth = random.randrange(400,initialRectangle.width)
    randHeightCompliment = (initialRectangle.height - randHeight)
    randWidthCompliment = (initialRectangle.width - randWidth)

    #create four rectangles, each with a combination of the two, dividing up the SVG tag into four separate rectangles. 

    rect1 = Rectangle(randHeight,randWidth, 0, 0)
    rect2 = Rectangle(randHeight, randWidthCompliment, randWidth, 0)
    rect3 = Rectangle(randHeightCompliment, randWidth, randHeight, 0)
    rect4 = Rectangle(randHeightCompliment, randWidthCompliment, randHeight, randWidth)

    #write rectangles to HTML file

  

    return rect1, rect2, rect3, rect4 

def divideIntoFourFix(File, initialRectangle):

    
    #create random heights based on the initial rectangle (basically just the SVG tag)

    heightOfFirstRectangle = random.randrange(0, initialRectangle.height - 100)
    widthOfFirstRectangle = random.randrange(0, initialRectangle.width - 100)
    
    # assign four rectangles the values and coordinates. 

    listOfRectangles = [] 

    rect1 = Rectangle(heightOfFirstRectangle,widthOfFirstRectangle,0,0)
    rect2 = Rectangle(heightOfFirstRectangle,initialRectangle.width - widthOfFirstRectangle, widthOfFirstRectangle, 0)
    rect3 = Rectangle(initialRectangle.height - heightOfFirstRectangle, widthOfFirstRectangle, 0, heightOfFirstRectangle)
    rect4 = Rectangle(initialRectangle.height - heightOfFirstRectangle, initialRectangle.width - widthOfFirstRectangle, widthOfFirstRectangle,heightOfFirstRectangle)

    listOfRectangles.append(rect1)
    listOfRectangles.append(rect2)
    listOfRectangles.append(rect3)
    listOfRectangles.append(rect4)

    #create them and write them to the HTML file.

    for rectangle in listOfRectangles:
        createRectangle(File, rectangle.height, rectangle.width, rectangle.x, rectangle.y)


    return listOfRectangles

def createRectangle(File, Height, Width, x , y, color = "(255,255,255)"): 
    
    color = color.replace("(","")
    color = color.replace(")","")
    colorList = color.split(",")
    red = colorList[0] #random.randrange(0,255)
    green = colorList[1] #random.randrange(0,255)
    blue =  colorList[2] #random.randrange(0,255)


    File.write("\n\t<rect x = \"" + str(x) + "\" y = \"" + str(y) + "\" width=\"" + str(Width) + "\"height=\"" + str(Height) + "\"style=\"fill:rgb("+str(red)+","+str(green)+","+str(blue)+");stroke-width:3;stroke:rgb(0,0,0)\"" + "/>")

def generateSVG(File):

    randWidth = 1000
    randHeight = 700
    

    File.write("<body>\n\t<svg id = \"svgTag\" width=\"" 
    + str(randWidth)+ "\" height= \"" + str(randHeight) + "\">") 

    return randWidth, randHeight

def implementCSS(File):
    
    File.write("<style>\n\n#svgTag {\nposition: relative;\nmargin: auto;\nleft:15%;\n}\n</style>\n\n")
  
def recursiveFunction(File, OGrectangle, thisRect):

    

    #base case

    if(thisRect.height <= OGrectangle.height/2 and thisRect.width <= OGrectangle.width/2):
        #color this rect and return
        red = random.randrange(0,255)
        green = random.randrange(0,255)
        blue = random.randrange(0,255)
        colorString = ("(" + str(red) + "," + str(green) + "," + str(blue) + ")")
        createRectangle(File, thisRect.height, thisRect.width, thisRect.x, thisRect.y, colorString) 

        return


    #check to see if only height is greater than half initial size 
    elif(thisRect.height >= OGrectangle.height/2):

        #if so, divide the region into two smaller ones. 
        newHeight = random.randrange(50,thisRect.height)

        #create new rectanlge in that area above it with the new height.
        newRect = Rectangle(newHeight, thisRect.width, OGrectangle.x, OGrectangle.y + newHeight)

        #add that rectangle to the html file.
        createRectangle(File,newRect.height, newRect.width, newRect.x, newRect.y)

        #return original rectangle and new rectangle. 
        return recursiveFunction(File, OGrectangle, newRect)

    #check to see if only width is greater than half initial size
    elif(thisRect.width >= OGrectangle.width/2):

        #if so, divide region into two smaller ones.
        newWidth = random.randrange(50, thisRect.width)

        #create new rectangle in area above it with new width.
        newRect = Rectangle(thisRect.height, newWidth, OGrectangle.x + newWidth, OGrectangle.y)

        #add the rectangle to the html file.
        createRectangle(File,newRect.height, newRect.width,newRect.x,newRect.y)

        #return orignal rectangle and new rectangle. 
        return recursiveFunction(File, OGrectangle, newRect)


def divideIntoFourInTheory(File, thisRectangle, initialRectangle):


    global almightyListOfRects
    #base case:


    

    
    if(thisRectangle.height >= initialRectangle.height / 2 and thisRectangle.width >= initialRectangle.width / 2 ):
        #divide into four and return the four recursivly. 

         #create random heights based on the initial rectangle (basically just the SVG tag)

        try:

            heightOfFirstRectangle = random.randrange(int(initialRectangle.height * .33), int(initialRectangle.height * .66))
            widthOfFirstRectangle = random.randrange(int(initialRectangle.height * .33), int(initialRectangle.width * .66))
        except ValueError:
            return
        # assign four rectangles the values and coordinates. 

        listOfRectangles = [] 

        #may run into problems with 0,0 coordinate system, if problem, then make 0 the x and y of the initial rectangle. 

        rect1 = Rectangle(heightOfFirstRectangle,widthOfFirstRectangle,0,0)
        rect2 = Rectangle(heightOfFirstRectangle,initialRectangle.width - widthOfFirstRectangle, widthOfFirstRectangle, 0)
        rect3 = Rectangle(initialRectangle.height - heightOfFirstRectangle, widthOfFirstRectangle, 0, heightOfFirstRectangle)
        rect4 = Rectangle(initialRectangle.height - heightOfFirstRectangle, initialRectangle.width - widthOfFirstRectangle, widthOfFirstRectangle,heightOfFirstRectangle)

        listOfRectangles.append(rect1)
        listOfRectangles.append(rect2)
        listOfRectangles.append(rect3)
        listOfRectangles.append(rect4)

    #create them and write them to the HTML file.

        for rectangle in listOfRectangles:
            createRectangle(File, rectangle.height, rectangle.width, rectangle.x, rectangle.y)


        for rectangle in listOfRectangles:
            almightyListOfRects.append([rectangle, False])
    
    return listOfRectangles

def initialRecursiveFunction2(File, thisRectangle, initialRectangle):

    global almightyListOfRects

    #take initial rectangle width and height divided by two and put them into their own variables. 

    initialWidthdiv2 = initialRectangle.width / 2
    initialHeightdiv2 = initialRectangle.height / 2 


        #base case:

    if(thisRectangle.height <= initialHeightdiv2 and thisRectangle.width <= initialWidthdiv2):
        return

        #second base:
    elif(thisRectangle.height <= initialHeightdiv2):
            #split vertically
        randomWidth = random.randrange(initialRectangle.width / 5, initialRectangle.width)
        newRect = Rectangle(thisRectangle.height, randomWidth, thisRectangle.x, thisRectangle.y)
        almightyListOfRects.append([newRect, False])
        createRectangle(File, newRect.height, newRect.width, newRect.x, newRect.y)

        return initialRecursiveFunction2(File, newRect, initialRectangle)

    #third base case:
    elif(thisRectangle.width <= initialWidthdiv2):
        #split horizontally (new random number generation based on what is said in the packet.)
        randomHeight = random.randrange(int(initialRectangle.height * .33), int(initialRectangle.height * .66))
        newRect = Rectangle(randomHeight, thisRectangle.width, thisRectangle.x, thisRectangle.y)
        almightyListOfRects.append([newRect,False])
        createRectangle(File, newRect.height, newRect.width, newRect.x, newRect.y)

        return initialRecursiveFunction2(File,newRect,initialRectangle)



        

    
    return

def secondRecursiveFunction(File, thisRectangle, initialRectangle):


    red = "(255,0,0)"
    yellow = "(255,255,0)"
    blue = "(0,0,255)"
    listOfColors = [red, yellow, blue]

    #code to generate random colors, does not look very good.

    # randomRed = random.randrange(0,255)
    # randomGreen = random.randrange(0,255)
    # randomBlue = random.randrange(0,255)

    # randomColor = "(" + str(randomRed) + "," + str(randomGreen) + "," + str(randomBlue) + ")"
    # print(randomColor)

    # if region is big enough, maybe split. 

    try:
        randInt = random.randrange(120, int(thisRectangle.width * 1.5))
    except ValueError:
        return

    try:
        randIntHeight = random.randrange(120, int(thisRectangle.height * 1.5))
    except ValueError:
        return

    if(randInt < thisRectangle.width):
        #split the region
        newWidth = random.randrange(int(thisRectangle.width * .33), int(thisRectangle.width * .66))
        newRect = Rectangle(thisRectangle.height, newWidth, thisRectangle.x, thisRectangle.y)
        createRectangle(File, newRect.height, newRect.width, newRect.x, newRect.y) 
        return secondRecursiveFunction(File, newRect, initialRectangle)

    elif(randIntHeight < thisRectangle.height):
        #split the region.
        newHeight = random.randrange(int(thisRectangle.height * .33), int(thisRectangle.height * .66))
        newRect = Rectangle(newHeight, thisRectangle.width, thisRectangle.x, thisRectangle.y)
        createRectangle(File, newRect.height, newRect.width, newRect.x, newRect.y)
        return secondRecursiveFunction(File, newRect, initialRectangle)

    else: 
        random.shuffle(listOfColors)
        newRect = Rectangle(thisRectangle.height, thisRectangle.width, thisRectangle.x, thisRectangle.y)
        createRectangle(File, newRect.height, newRect.width, newRect.x, newRect.y, listOfColors[0])


    return



def main():

    global almightyListOfRects

    htmlFile = open(input("Enter the name of the file to write to: "),'w')

    writeHeader(htmlFile)

    implementCSS(htmlFile)

    widthOfSVG, heightOfSVG = generateSVG(htmlFile)

    initialRectangle = Rectangle(heightOfSVG, widthOfSVG, 0, 0)
    
    listOfFour = divideIntoFourInTheory(htmlFile, initialRectangle, initialRectangle)

    initialRecursiveFunction2(htmlFile, listOfFour[0], initialRectangle)
    initialRecursiveFunction2(htmlFile,listOfFour[1],initialRectangle)
    initialRecursiveFunction2(htmlFile,listOfFour[2], initialRectangle)
    initialRecursiveFunction2(htmlFile,listOfFour[3], initialRectangle)


    for rectangle in almightyListOfRects:
        try:
            secondRecursiveFunction(htmlFile, rectangle[0], initialRectangle)
        except IndexError:
            continue
        
    for rectangle in almightyListOfRects:
        try:
            secondRecursiveFunction(htmlFile, rectangle[0], initialRectangle)
        except IndexError:
            continue



  

    #use recursive function on all the rectangles in the list. 
  
    
    
    
    # rectHeight = random.randrange(100,randHeight)
    # rectWidth = random.randrange(100,randWidth)

    # createRectanlge(htmlFile, rectHeight, rectWidth)

   # recursiveFunction(htmlFile, initialRectangle)

    htmlFile.write("\n</svg>")

    htmlFile.write("\n\n</body>\n")

    writeFooter(htmlFile)

    htmlFile.close()

main()

''' DESIGN: 
-at the time of writing this, this program only draws a rectangle of random size and random color to an HTML file specified by the user. 

Steps:

    -prompt user for name of HTML file that will be written to.

    -Open file.

    -create SVG tag of a certain height and width

    - Determine if region is wider than hald the inital canvas size and taller than half the inital canvas size. 
        - If it is, split the region into four different rectangles.

        - else if the region is taller than half initial canvas size, use recursion to split it into two smaller rectangles.

        - else if the region is only wider, then split it into two smaller regions with recursion. 

    - For each region, if it is big enough split it, split it both horizontally and vertically. 
    
        - else if the region is tall enough, split it vertically

        - else if the region is wide enough split it horizontally.

        - else: if it is small enough, fill it with a random color. 


        -



    
'''





