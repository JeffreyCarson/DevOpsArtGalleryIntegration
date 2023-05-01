#Jeffrey Carson

#Must be a simple polygon

import tkinter as tk
#import triangulate as tri

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printPoint(self):
        print(f"({self.x}, {self.y})")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printVector(self):
        print(f"<{self.x}, {self.y}>")

#finds cross product between two vertices
def crossProduct(ver1, ver2):
    #print(vec1.x * vec2.y - vec1.y * vec2.x )
    return ver1.x * ver2.y - ver1.y * ver2.x    

#returns the area of the polygon. If area is positive, we have a clickwise winding order. If negative, counterclockwise. 
def polygonArea(points):
    area = 0
    for i in range(len(points)):
        point1 = points[i]
        point2 = points[(i+1) % len(points)]

        width = point2.x - point1.x
        height = (point2.y + point1.y) / 2

        area += width * height
    return area

#takes an index of any size, returns proper index in relative position 
def getCircularIndex(list, index):
    if index >= len(list):
        return index % len(list)
    elif index < 0:
        return index % len(list)
    else:
        return index

#vector math to find out if a point(p) is within a triangle(a, b, c)
def isPointInsideTriangle(p, a, b, c):

    if polygonArea([a, b, c]) < 0:
        temp = b
        b = c
        c = temp

    ab = Vector(b.x - a.x, b.y - a.y)
    bc = Vector(c.x - b.x, c.y - b.y)
    ca = Vector(a.x - c.x, a.y - c.y)

    ap = Vector(p.x - a.x, p.y - a.y)
    bp = Vector(p.x - b.x, p.y - b.y)
    cp = Vector(p.x - c.x, p.y - c.y)

    crossProd1 = crossProduct(ab, ap)
    crossProd2 = crossProduct(bc, bp)
    crossProd3 = crossProduct(ca, cp)

    if (crossProd1 > 0 or crossProd2 > 0 or crossProd3 > 0):
        return False
    
    return True

#returns the index of an array which holds the smallest value
def returnIndexSmallestInt(arr):
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            smallestIndex = i 
    return smallestIndex

#if number is odd, return true
def isOdd(number):
    if number % 2 == 1:
        return True
    else:
        return False

#takes in array of triangles
#returns a list with each index corresponding to a color
def colorVerticies(triangles):
    
    indexColors = []
    #colors can be 1, 2, or 3. 
    degreeList = []
    for i in range(len(triangles)+2):
        degreeList.append(0)
        indexColors.append(0)
    
    for i in range(len(triangles)):
        for j in range(len(triangles[i])):
            degreeList[triangles[i][j]] += 1
    
    indexColors[0] = 1
    indexColors[1] = 2
    for i in range(1, len(indexColors)-1):
        
        if not isOdd(degreeList[i]):
            indexColors[i+1] = indexColors[i-1]
        else:
            indexColors[i+1] = 6 - indexColors[i-1] - indexColors[i]
    
    return indexColors

# Takes in a list of vertices (their index in the list represents their order in the polygon) 
# returns a list of triangles made from those indices

#must take in a simple polygon
#no colinear edges
# clockwise vertex order

def triangulatePolygon(vertices):
    indexList = []
    triangleList = []
    if len(vertices) < 3:
        print("polygon must have at least 3 vertices")
        return 1
    
    if polygonArea(vertices) < 0:
        vertices.reverse()

    for i in range(len(vertices)):
        indexList.append(i)

    while (len(indexList) > 3):
        for i in range(len(indexList)):
            
            #indices
            middle = indexList[i]
            left = indexList[getCircularIndex(indexList, i-1)]
            right = indexList[getCircularIndex(indexList, i+1)]

            #middle point, left point, right point
            mp = vertices[middle]
            lp = vertices[left]
            rp = vertices[right]

            #vector from middle to left, lp-mp
            middleToLeft = Vector(lp.x - mp.x, lp.y - mp.y)
            #vector from middle to right, rp-mp
            middleToRight = Vector(rp.x - mp.x, rp.y - mp.y)
            
            #if convex angle, move to next index for now
            if crossProduct(middleToLeft, middleToRight) < 0:
                continue

            isEar = True

            #if any other points inside potential ear, move to next index for now
            for j in range(len(vertices)):
                if j == middle or j == left or j == right:
                    continue

                testPoint = vertices[j]
                if isPointInsideTriangle(testPoint, lp, mp, rp):
                    isEar = False
                    break
            
            #if we have found a valid ear
            if isEar:
                triangle = [left, middle, right]
                triangleList.append(triangle)
            
                indexList.pop(i)
                break

    triangle = [indexList[0], indexList[1], indexList[2]]
    triangleList.append(triangle)

    return triangleList

#clears the canvas and variables
def refresh_event():
    global canEditFlag, pointList
    canvas.delete("all")
    canEditFlag = True
    pointList = []
    canvas.old_coords = None
    

#Displays polygon and its triangulations. The vertices are colorized such that each triangle has three unique colors
def color_event():
    global indexColors
    canvas.delete("all")
    triangleList = triangulatePolygon(pointList)
    if triangleList == 1:
        refresh_event()
    else:
        for i in range(len(pointList)):
            canvas.create_line(pointList[i].x, pointList[i].y, pointList[getCircularIndex(pointList, i+1)].x, pointList[getCircularIndex(pointList, i+1)].y, fill = "black")
        
        indexColors = colorVerticies(triangleList)
        for i in range(len(triangleList)):
            canvas.create_line(pointList[triangleList[i][0]].x, pointList[triangleList[i][0]].y, pointList[triangleList[i][2]].x, pointList[triangleList[i][2]].y, fill = "lightgrey")
        
        for i in range(len(pointList)):
            
            color = ''
            if indexColors[i] == 1:
                color = 'red'
            if indexColors[i] == 2:
                color = 'blue'
            if indexColors[i] == 3:
                color = 'green'
            canvas.create_oval(pointList[i].x+5, pointList[i].y+5, pointList[i].x-5, pointList[i].y-5, fill = color, outline="black")
    
    
    
#Displays the polygon with the guards placed most efficently
def guard_event():
    global indexColors
    canvas.delete("all")
    triangleList = triangulatePolygon(pointList)
    if triangleList == 1:
        refresh_event()
    else:
        for i in range(len(pointList)):
            canvas.create_line(pointList[i].x, pointList[i].y, pointList[getCircularIndex(pointList, i+1)].x, pointList[getCircularIndex(pointList, i+1)].y, fill = "black")
        colorCount = [0, 0, 0]
        
        indexColors = colorVerticies(triangleList)
        for i in range(len(indexColors)):
            if indexColors[i] == 1:
                colorCount[0] += 1
            if indexColors[i] == 2:
                colorCount[1] += 1
            if indexColors[i] == 3:
                colorCount[2] += 1
        guardColor = returnIndexSmallestInt(colorCount) + 1
        for i in range(len(indexColors)):
            color = ''
            if indexColors[i] == 1:
                color = 'red'
            if indexColors[i] == 2:
                color = 'blue'
            if indexColors[i] == 3:
                color = 'yellow'
            #If the color matches the least used color in the colorization step, then display it. Otherwise dont.
            if indexColors[i] == guardColor:
                canvas.create_oval(pointList[i].x+5, pointList[i].y+5, pointList[i].x-5, pointList[i].y-5, fill = color, outline="black")    


#displays the polygon and its triangulations
def triangulate_event():
    global canEditFlag, pointList
    canEditFlag = False
    canvas.delete("all")
    for i in range(len(pointList)):
        canvas.create_line(pointList[i].x, pointList[i].y, pointList[getCircularIndex(pointList, i+1)].x, pointList[getCircularIndex(pointList, i+1)].y, fill = "black")
    triangleList = triangulatePolygon(pointList)
    if triangleList == 1:
        refresh_event()
    else:
        for i in range(len(triangleList)):
            canvas.create_line(pointList[triangleList[i][0]].x, pointList[triangleList[i][0]].y, pointList[triangleList[i][2]].x, pointList[triangleList[i][2]].y, fill = "red")
    
#Draws a line on the screen.
def draw_line(e):
    global originPoint
    x, y = e.x, e.y
    
    if len(pointList) == 0 and y >=30:
        originPoint = Point(x, y)
    if y >= 30 and canEditFlag == True:
        pointList.append(Point(x, y))
            #x1, y1 = canvas.old_coords
        canvas.delete("all")
        for i in range(len(pointList)-1):
            canvas.create_oval(pointList[i].x+2, pointList[i].y+2, pointList[i].x-2, pointList[i].y-2, fill = "black", outline="black")
            canvas.create_line(pointList[i].x, pointList[i].y, pointList[i+1].x, pointList[i+1].y, fill = "black")
        if len(pointList) > 2:
            canvas.create_line(x, y, originPoint.x, originPoint.y, width=1, fill = "lightgrey")


# Create an instance of tkinter
win = tk.Tk()
win.title("Art Gallery Problem Visualizer [Jeffrey Carson 2022]")
win.resizable(False, False)
canEditFlag = True
originPoint = Point(0, 0)
pointList = []
indexColors = []
# Window size
win.geometry("500x500")

topframe = tk.Canvas(win, width = "500", height = "20")
topframe.pack(side = "top")

canvas = tk.Canvas(win, width=500, height=500, bg = "white")
#canvas.pack()
#canvas.old_coords = None

# Bind the left button the mouse.
win.bind('<ButtonPress-1>', draw_line)
btn = tk.Button(topframe, text ="TRIANGULATE", command = triangulate_event)
refresh_btn = tk.Button(topframe, text ="REFRESH", command = refresh_event)
color_btn = tk.Button(topframe, text ="COLORIZE", command = color_event)
guard_btn = tk.Button(topframe, text ="GUARD", command = guard_event)
guard_btn.pack(side = "right")
color_btn.pack(side = "right")
refresh_btn.pack(side = "left")
btn.pack()
canvas.pack()

def main():
    win.mainloop()

if __name__ == "__main__":
    main()