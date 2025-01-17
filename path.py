x = 0
y = 1

smoothing = 0.9
weight = 0.1
tolerance = 0.132
#Puts dots in the middle
def interpolate(path, spacing):

    newPath = [path[0]]
    segments = len(path)-1
    initialRatio = 100 / ((spacing + 1) * 100)

    for i in range(0, segments):
        ratio = 100 / ((spacing + 1) * 100)
        for j in range(0, spacing+1):
            deltaPoint = [path[i+1][x] - path[i][x], path[i+1][y] - path[i][y]]
            scaledPoint = [deltaPoint[x]*ratio, deltaPoint[y]*ratio]
            nextPoint = [int(path[i][x]+scaledPoint[x]), int(path[i][y]+scaledPoint[y])]

            newPath.append(nextPoint)
            ratio += initialRatio
    return newPath
#Take a path of points and turns the point into a quintic piecewise polynomial, AKA turns jagged into smooth path
def smooth(path):
    newPath = [[w[0], w[1]] for w in path]
    change = tolerance

    while change >= tolerance:
        change = 0
        for i in range(1, len(path)-1):
            for j in range(len(path[i])):
                aux = newPath[i][j] # Smooth Current

                current = path[i][j]

                previousSmooth = newPath[i-1][j]
                nextSmooth = newPath[i+1][j]

                newPath[i][j] += smoothing * current-aux + weight * previousSmooth+nextSmooth - 2 * aux

                #newPath[i][j] += smoothing*(float(path[i][j])-float(newPath[i][j])) + weight*(float(newPath[i-1][j])+float(newPath[i+1][j])-2*float(newPath[i][j]))
                change += abs(aux - newPath[i][j])

    return newPath

#Useless
def normalize(pos, screenWidth, screenHeight):
    posX = pos[x]
    posY = pos[y]

    normX = posX
    normY = posY
    return [normX, normY]
    