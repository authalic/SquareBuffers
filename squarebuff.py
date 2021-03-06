
import arcpy

def squarebuffers(originX, originY, sideLength=1609.34):
    "Input is the center point coordinates, and the length of the sides of the 4 squares"

    quad1 = {}
    quad2 = {}
    quad3 = {}
    quad4 = {}
    
    quad1["UL"] = [originX, originY + sideLength]
    quad1["UR"] = [originX + sideLength, originY + sideLength] 
    quad1["LL"] = [originX, originY]
    quad1["LR"] = [originX + sideLength, originY]
    
    quad2["UL"] = [originX - sideLength, originY + sideLength]
    quad2["UR"] = [originX, originY + sideLength] 
    quad2["LL"] = [originX - sideLength, originY]
    quad2["LR"] = [originX, originY]
    
    quad3["UL"] = [originX - sideLength, originY]
    quad3["UR"] = [originX, originY] 
    quad3["LL"] = [originX - sideLength, originY - sideLength]
    quad3["LR"] = [originX, originY - sideLength]
    
    quad4["UL"] = [originX, originY]
    quad4["UR"] = [originX + sideLength, originY] 
    quad4["LL"] = [originX, originY - sideLength]
    quad4["LR"] = [originX + sideLength, originY - sideLength]

    quad1list = [quad1['UL'], quad1['LL'], quad1['LR'], quad1['UR'], quad1['UL']]
    quad2list = [quad2['UL'], quad2['LL'], quad2['LR'], quad2['UR'], quad2['UL']]
    quad3list = [quad3['UL'], quad3['LL'], quad3['LR'], quad3['UR'], quad3['UL']]
    quad4list = [quad4['UL'], quad4['LL'], quad4['LR'], quad4['UR'], quad4['UL']]

    coordList = [quad1list, quad2list, quad3list, quad4list]
    
    return coordList


def createFeatures(coordList):
        
    for feature in coordList:
        point = arcpy.Point()
        array = arcpy.Array()
        
        for coordPair in feature:
            point.X = coordPair[0]
            point.Y = coordPair[1]
            array.add(point)
     
        array.add(array.getObject(0))
         
        polygon = arcpy.Polygon(array)
                
        featureList.append(polygon)
    


featureList = []  #list that will contain the Polygon features 



# Loop through all of the center points here

test1X = 425000
test1Y = 4498000

test2X = 438000
test2Y = 4458000

createFeatures(squarebuffers(test1X, test1Y))
createFeatures(squarebuffers(test2X, test2Y))

arcpy.CopyFeatures_management(featureList, "C:/test/polygons.shp")



