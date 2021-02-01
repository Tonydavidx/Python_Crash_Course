import cairo
import math
 
FRAMECOUNT = 100
 
#############################
 
class Shade():
    def __init__(self, radius, centerpoint):
        self.xCord, self.yCord = centerpoint
        self.radius = radius
        self.center = centerpoint
 
    def updatePos(self, newX, newY):
        self.xCord = newX
        self.yCord = newY
 
    def receiveCord(self, cords):
        x, y = cords
        self.updatePos(x, y)
 
    def drawSelf(self, context, fill):
        context.set_source_rgb(1,1,1)
        context.arc(self.xCord, self.yCord, self.radius, 0, 2*math.pi)
        if fill == True:
            context.fill()
        else:
            context.stroke()
 
 
       
 
class Positions():
    def __init__(self, frameCount, radius, center, phase):
 
        # get radians of slices depending on frame count
        self.radian = 2*math.pi/frameCount
        self.slices = []
        for x in range(frameCount):
            currentSlice = self.radian * x
            xVal = math.cos(currentSlice)
            yVal = math.sin(currentSlice)
            self.slices.append((xVal,yVal))
            continue
        # scale those coordinates by the radius
        self.storedCords = []
        self.centerpoint = center
        for each in self.slices:
            xVal = (each[0]*radius)
            yVal = (each[1]*radius)
            self.storedCords.append((xVal,yVal))
            continue
        # translate to the correct portion
        xCent, yCent = center
        for i in range(len(self.storedCords)):
            tempX = self.storedCords[i][0] + xCent
            tempY = self.storedCords[i][1] + yCent
            self.storedCords[i] = (tempX, tempY)
            continue
        # start orbit in whichever phase
        self.finalCords = self.storedCords[phase:]
        for x in self.storedCords[:phase]:
            self.finalCords.append(x)
       
         
###################################################
   
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1000, 1000)
ctx = cairo.Context (surface)
 
frames = FRAMECOUNT
 
# initial positions dont really matter except for you
blackhole = Shade(125, (500,500))
planet = Shade(25, (800, 500))
moon = Shade(5, (750,500))
 
#find planet's orbit
planetPos = Positions(FRAMECOUNT, 300, (500, 500), 0)
 
 
 
#animation
for x in range(frames):
    # Blank screen
    ctx.set_source_rgb(0, 0, 0)
    ctx.rectangle(0, 0, 1000, 1000)
    ctx.fill()
 
    #update planet position
    planet.receiveCord(planetPos.finalCords[x])
    moonPos = Positions(FRAMECOUNT, 50, planetPos.finalCords[x], x)
    moon.receiveCord(moonPos.finalCords[x])
   
 
    #draw planets
    blackhole.drawSelf(ctx, False)
    planet.drawSelf(ctx, True)
    moon.drawSelf(ctx, False)
   
 
    #draw
    ctx.stroke()
    print ('Creating Frame')
    surface.write_to_png('Frame' + str(x)+'.png')
 
print ('Finished')