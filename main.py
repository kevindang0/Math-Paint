#Made by Kevin Dang
from pygame import *
from random import *
from math import *
#import all necessary libraries
from tkinter import *
from tkinter import filedialog
#import my own files
from resources import *
from musicplayer import *
from icons import *

#setup variables
paintslidercolor=GREEN
stampslidercolor=GREEN
colorhueSlidercolor=GREEN
listUndo = []
fixstampbug=0
#some variables to track whether an action is done (for undo)
undoEnsure=False

pi=image.load("Pics/pistamp.png")
infinity=image.load("Pics/infinitysymbol.jpg")
mring=image.load("Pics/mring.jpg")
divide=image.load("Pics/dividesymbol.png")
coolgraph=image.load("Pics/coolgraph.png")
#keeps track of the current stamp size to change the size using the slider
currentstampsizex=330
currentstampsizey=330
# checks if the size of the stamp changes to fix a blurry bug
stampsizechecker=currentstampsizex
#put an empty string to set up the variable
undoCapture=""

currentcolor = (0,0,0)

font.init()

calibriFont=font.SysFont("Calibri",20)

#printcolwheel = False

filled=0
sliderx=59+button1xoffset
#slider coordinates that will change to update the slider position
mouseup =False
tool=""
col=BLACK

drawing=False
#function to draw the buttons
def drawbuttons():

    draw.rect(screen, WHITE, toolDescriptionRect)
    draw.rect(screen, BLACK, toolDescriptionRect,2)
    draw.rect(screen, WHITE, musDescriptionRect)
    for i in range(5):  
             
        rectanglePosition = eval("colorsave" + str(i+1))
        #uses eval to allow me to accept a string as an argument
        draw.rect(screen, savedColors[i], rectanglePosition)
    #make sure these variables are accessible
    global currentcolor, selectedColor, paintslidercolor, stampslidercolor, toolDescription
    mx, my = mouse.get_pos()

    for button_name in button_names:
        button_rect = eval(button_name)
        #draws buttons for all of the buttons in the list (in resources)
        if button_rect.collidepoint(mx, my):
            draw.rect(screen, ORANGE, button_rect, 2)
            toolDescription = button_name[0:5]
        else:
            draw.rect(screen, GREEN, button_rect, 2)


        
#function to clear the screen
def clearscreen(colorclear):
    draw.rect(screen,colorclear,canvasRect)
#list to check when a tool is selected (for undo/redo)
listtools = ["pencil", "eraser", "spraypaint","brush","Line","Rect","Oval","stamp"]
#if the tool is in the list of tools, take a screenshot (so no screenshots if just random clicks)

#dictionary to store info about the tools
toolDescriptions = {

    "undoR": "Undo your last action",
    "redoR": "Redo your undo",

    "saveR": "Save the canvas as an image",
    "loadR": "Load an image onto the canvas",
    
    
    "none": "Hover over a button to see what it does",
    "spray": "Draws circles in a radius from the mouse",
    "penci": "Draws a 1 px line. Not affected by size changes",
    "erase": "Erases drawn things. Affected by size changes",
    "brush": "Draws circles with different hues",
    "trash": "Fills the screen with your current color",

    "colwh": "Click on the color wheel to get a color",

    "musba": "Go back to the previous song",
    "mussk": "Skip the current song",
    "muspa": "Pause/play the current song",
    "musDe": "Display the current song",


     

    "paint": "Adjusts the size of the tool you're using",
    "colhu": "Modifies the color's lightness/darkness",
    "colCh": "Displays current color. Click on the color wheel",
    "sizeC": "Displays the current color and size of tool",
    "color": "Saving Colors (Rclick to save/Lclick to load)",
    "stamS": "Change the size of the stamps",

    "muse": "Displays the current song",
    "volSl": "Adjust the volume of the music",

    "drawR": "Draws a rectangle",
    "drawL": "Draws a straight line",
    "drawO": "Draws an ellipse",
    "fille": "Fill shapes with solid color",

    "stamp": "Imprint an image on the canvas",
    "stampslider": "Adjusts the size of the stamp"
}
#function to check if the current tool is in the dictionary and prints out the info
def loadtoolDescription(currenttool):
    if toolDescription in toolDescriptions:
        myText=calibriFont.render(toolDescriptions[toolDescription], FALSE, BLACK)
        screen.blit(myText,(260+button2xoffset,55+buttonlayer3+buttonyoffset))
#i used a dictionary to store the description of the music
musicDescriptions = {
    "nowplaying":"Now Playing:",

    "classical1": "My Dearest Friends",
    "composer1":"By Lena Raine",
    
    "classical2": "Lines Song",
    "composer2":"By NUMBERROCK",

    "classical3": "The Pi Song",
    "composer3":"By AsapSCIENCE",
}
#make a function to load the description of the song
def loadmusicDescription(currentsong):
    #if music is not paused, load description
    if musicPause==False:
        if currentsong in musicDescriptions:
            musictext=calibriFont.render(musicDescriptions["nowplaying"], FALSE, BLACK)
            screen.blit(musictext,(520+button4xoffset,50+buttonlayer2+buttonyoffset))
            musictext=calibriFont.render(musicDescriptions[currentsong], FALSE, BLACK)
            screen.blit(musictext,(520+button4xoffset,80+buttonlayer2+buttonyoffset))

            musictext=calibriFont.render(musicDescriptions[("composer"+str(latestindex[-1]))], FALSE, BLACK)
            screen.blit(musictext,(520+button4xoffset,110+buttonlayer2+buttonyoffset))
    #if music is paused, write music is paused
    else:
        musictext=calibriFont.render("Music is paused", FALSE, BLACK)
        screen.blit(musictext,(520+button4xoffset,51+buttonlayer2+buttonyoffset))
#make functions to blit the pause and play icons
def setmusiconpause():
    screen.blit(musicpauseicon,(592+button4xoffset, buttonlayer1+buttonyoffset))
def setmusiconplay():
    screen.blit(musicplayicon,(592+button4xoffset, buttonlayer1+buttonyoffset))
#icons
#________________________________________________________#
#blit all of the icons (info about icons stored in icons.py)
tool="none"

screen.blit(mathbg,(0,0))
screen.blit(mathpaint,(-10,110))

screen.blit(saveicon,(4,2+buttonyoffset))
screen.blit(loadicon,(6,52+buttonyoffset))

screen.blit(undotool,(46,2+buttonyoffset))
screen.blit(redotool,(46,50+buttonyoffset))

screen.blit(spraypainticon,(2+button1xoffset,2+buttonyoffset))
screen.blit(pencilicon,(44+button1xoffset,2+buttonyoffset))
screen.blit(erasericon,(86+button1xoffset,2+buttonyoffset))
screen.blit(randomcircletool,(128+button1xoffset,2+buttonyoffset))
screen.blit(trashicon,(170+button1xoffset,2+buttonyoffset))

screen.blit(musicbackicon,(550+button4xoffset,buttonlayer1+buttonyoffset))
screen.blit(musicplayicon,(592+button4xoffset, buttonlayer1+buttonyoffset))
screen.blit(musicskipicon,(634+button4xoffset,buttonlayer1+buttonyoffset))

screen.blit(whiteblackicon,(250+button2xoffset,buttonlayer2+buttonyoffset))

screen.blit(linetoolicon,(292+button2xoffset,96+buttonyoffset))
screen.blit(circletoolicon,(334+button2xoffset,96+buttonyoffset))
screen.blit(squaretoolicon,(250+button2xoffset,96+buttonyoffset))
screen.blit(filledtoolicon,(376+button2xoffset,96+buttonyoffset))

screen.blit(pistampicon,(450+button3xoffset,2+buttonyoffset))
screen.blit(infinityicon,(492+button3xoffset,2+buttonyoffset))
screen.blit(mringicon,(534+button3xoffset,2+buttonyoffset))
screen.blit(divideicon,(576+button3xoffset,2+buttonyoffset))
screen.blit(coolgraphicon,(618+button3xoffset,2+buttonyoffset))

#________________________________________________________#




selectedstamp = -1

colorbox=0
#list to store the saved colors (for saving colors feature)
savedColors=[(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255)]
newColor=(0,0,0)
newvaluestampslider=0
#more setting up variables
currentselection = -1
screencaptured=0
running=True
sx,sy=0,0
drawing_history = []
redo_history = []
rightClick=False

colorHue=0
#load and transform color wheel img
colorwheel=image.load("Pics/colorwheel.png")
colorwheel=transform.smoothscale(colorwheel,(150,150))
screen.blit(colorwheel,(325,10))
draw.rect(screen, currentcolor, currentcolorvisual)
#run these once only
while running:
    
    

    for evt in event.get():
 
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:#left click
               sx,sy=evt.pos#initial click position

                
            elif evt.button==3:
                rightClick=True
                #if right click, set a variable to true and reset at the end of loop
        
        elif evt.type == MOUSEBUTTONUP:
            screenCap = screen.subsurface(canvasRect).copy()

            mouseup=True
            #if mouseup is detected, set variable to true, reset at end

            if tool in listtools and canvasRect.collidepoint(mx,my) or undoEnsure==True:
                #some logic for the undo redo features.
                undoCapture = screen.subsurface(canvasRect).copy()
                #if tool is selected, and user mouseups on screen, take a picture 
                drawing_history.append(undoCapture) 
                
                redo_history.clear()
                undoEnsure=False
                #if user draws, they can't redo 

    toolDescription="none"
        

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
        

        
        #some logic for the color wheel option
    if hypot(mx-395,my-78) < 72:
        hoveringoverCircle = True
        #printcolwheel = True
        # if mouse is less than the radius from the center of the colorwheel, hovering over circle is true

        toolDescription="colwh"

        
    else: hoveringoverCircle=False


    keys = key.get_pressed()
    if screencaptured==0:
        undoCapture = screen.subsurface(canvasRect).copy()
        drawing_history.append(undoCapture) 
        screencaptured=1
        #takes a picture once at the start so theres something in the drawing history list

    sliderSlide=Rect(sliderx,48+buttonyoffset,10,46)

    #for the stamp and shape tools
    if tool == "stamp" and mb[0]:
        #they have to be able to blit an empty screen and update with a new shape 
        screen.blit(screenCap,canvasRect)
# i tried doing if tool=="oval" or tool =="rect", etc, and canvasrect.collidpoint but for some reason undo didnt work for some of the shapes
    if canvasRect.collidepoint(sx,sy):
        if tool == "Oval":
            screen.blit(screenCap,canvasRect)
        elif tool == "Line":
            screen.blit(screenCap,canvasRect)
        elif tool == "Rect":
            screen.blit(screenCap,canvasRect)

    #transform the images with the current stamp size
    pi = transform.smoothscale(pi, (currentstampsizex, currentstampsizey))
    infinity = transform.smoothscale(infinity, (currentstampsizex, currentstampsizey))
    mring = transform.smoothscale(mring, (currentstampsizex, currentstampsizey))
    divide = transform.smoothscale(divide, (currentstampsizex, currentstampsizey))
    coolgraph = transform.smoothscale(coolgraph, (currentstampsizex, currentstampsizey))
    listpics = [pi, infinity, mring, divide, coolgraph]
    #list of pics to use when


    #call function to draw the buttons
    drawbuttons()
    #update the sliders with the new position
    stampsliderSlide=Rect(stampsliderx+button3xoffset,48+buttonyoffset,10,46)

    colorsliderSlide=Rect(colorsliderx+button3xoffset,48+buttonyoffset,10,46)

    screenCap=screen.subsurface(canvasRect).copy()

    #check if user rightclicks on color saving boxes
    if rightClick==True:
        for i in range(5):
            if (eval("colorsave" + str(i+1))).collidepoint(mx,my):
                savedColors[i]=currentcolor


    #selecting the tool
    if mouseup==True:
        #use mouseup to only detect a change once (wont constantly activate if user holds down mouse)
        if pencilRect.collidepoint(mx,my):
            tool="pencil"
        if eraserRect.collidepoint(mx,my):
            tool="eraser"
        if spraypaint.collidepoint(mx,my):
            tool="spraypaint"
        if brushRect.collidepoint(mx,my):
            tool="brush"
            
        if musskip.collidepoint(mx,my):
            musicPause=False
            skipsong()
            loadsong()
            setmusiconpause()
            #call functions to skip, load song


            mixer.music.play(loops=-1)
        if muspause.collidepoint(mx,my):
            if musicPause==False:
                
                pause_music()
                musicPause=True
                setmusiconplay()
            else:
                unpause_music()
                #set music paused to false
                musicPause=False
                setmusiconpause()
                
            
         
        if musback.collidepoint(mx,my):
            setmusiconpause()
            #change icon to pause icon (because song now plays)
            musicPause=False
            backsong()
            loadsong()
            loadmusicDescription("classical"+str(latestindex[-1]))
            #load music description

            
            

            
        #checks if filled checkbox is clicked, changes a variable
        if filledCheckbox.collidepoint(mx,my):
            if filled==0:
                filled=1
            
            else:
                filled=0
                
            #saves images
        if saveRect.collidepoint(mx,my):
            fname=filedialog.asksaveasfilename(defaultextension=".png")
            if fname != "": #makes sure there is a filename
                image.save(screen.subsurface(canvasRect),fname)
        #load images
        if loadRect.collidepoint(mx,my):
            
            fname=filedialog.askopenfilename()
            if fname != "":
                undoEnsure=True
                undoCapture = screen.subsurface(canvasRect).copy()
                drawing_history.append(undoCapture) 
                newimage=image.load(fname)
                #makes sure image is not too big, transforms image to make sure it fits
                if (newimage.get_width()) > 1200:
                    newimage = transform.scale(newimage, (1200, newimage.get_height()))
                if (newimage.get_height()) > 600:
                    newimage = transform.scale(newimage, (newimage.get_width(), 600))
                clearscreen(WHITE)
                screen.blit(newimage,(0,200))
        #checks whether a stamp button is clicked
        for i in range(5):
            if (eval("stamp" + str(i+1)+"Rect")).collidepoint(mx,my):
                tool="stamp"
                selectedstamp=i
        #if the tool is stamped, and user mouseups on screen
        if tool == "stamp" and canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)
            #blit stamp onto screen
            screen.blit(screenCap,canvasRect)
            screen.blit(listpics[selectedstamp],(mx-currentstampsizex//2,my-currentstampsizey//2))
            #make sure mouse is center of the stamp
            screenCap=screen.subsurface(canvasRect).copy()
            screen.set_clip(None) 
        #checks if user clicks on rect, oval, line tools
        if drawRect.collidepoint(mx,my):
            tool = "Rect"
        if drawOval.collidepoint(mx,my):
            tool = "Oval"
        if drawLine.collidepoint(mx,my):
            tool = "Line"
            #allows user to get a new color is mouse is over color wheel
        if hoveringoverCircle==True:
            currentcolor = screen.get_at((mx, my))
            newColor = screen.get_at((mx, my))
        #some logic for the color saving feature
        for i in range(5):
            #use eval to make more efficient code
            if (eval("colorsave" + str(i+1))).collidepoint(mx,my):
                currentcolor=savedColors[i]
                draw.rect(screen, currentcolor, currentcolorvisual)

        
        if undoRect.collidepoint(mx, my):
                screen.set_clip(None)
                #if drawing history has something in it
                if len(drawing_history) > 1:
                    #move the image stored in drawing history to redo history
                    redo_history.append(drawing_history.pop())
                    if len(drawing_history)>=1:
                        #blit the previous screen
                        screen.blit(drawing_history[-1], canvasRect)


        if redoRect.collidepoint(mx, my):
                screen.set_clip(canvasRect)
                #if theres some in redo history
                if len(redo_history) > 0:
                    #move the image back to drawing history
                    drawing_history.append(redo_history.pop())
                    
                    if len(drawing_history)>1:
                        #blits the image from before the undo
                        screen.blit(drawing_history[-1], canvasRect)

        if trashRect.collidepoint(mx,my):
            #takes a screenshot from before the screen fill and adds to drawing history for undo
            undoCapture = screen.subsurface(canvasRect).copy()
            drawing_history.append(undoCapture) 
            #clear redo history
            redo_history.clear()
            undoEnsure=True
            #fills screen with current color
            clearscreen(currentcolor)





         
    #all of the logic for the sliders
    if mb[0]:
        #if mouse clicks on slider, move sliderx to mx
        if paintsizeSliderCollison.collidepoint(mx+3,my):
            sliderx = mx - 5
            #increases radius if mx is higher, decreases if lower
            radius = (sliderx-button1xoffset + 50) // 10

        if stampsizeSliderCollison.collidepoint(mx,my):
            stampsliderx = mx-button3xoffset
            #logic for the stamp sizes
            currentstampsizex = round((mx-600)*1.5)
            currentstampsizey = currentstampsizex

        if colorhueSliderCollison.collidepoint(mx,my):
            colorsliderx = mx
            #logic for changing the hue of the colors
            currentHue = ((mx-83)/500)**(2)
            oldColor=list(newColor)#converts color to a list that can be modified
            currentcolor=list(currentcolor)
            # does changes to all r,g,b values of the current color
            for i in range(3):
                currentcolor[i] = min(255, max(0,round(oldColor[i]*currentHue)))
            currentcolor=tuple(currentcolor)
            #converts it back to a tuple
        if volSliderCollison.collidepoint(mx,my):
            volume = round((mx*0.9)-902)
            #logic for the volume sliders
            volsliderx=mx-button4xoffset
            mixer.music.set_volume(volume/100)
            #change volume of music (from 0.0 - 1.0)
            
            

    #using the tools, checks if mouse button down and over canvas
    if mb[0] and canvasRect.collidepoint(sx,sy):
        #clips canvas so only canvas changes
        screen.set_clip(canvasRect)
        randomcol=[]
        randomintx = randint(10-(radius*2),10+(radius*2))
        randominty = randint(10-(radius*2),10+(radius*2))
        #creates some random numbers for the brush tool
        for i in range(3):
            randomcolgenerator = (randint(currentcolor[i]-30,currentcolor[i]+30))
            if randomcolgenerator>255:
                randomcolgenerator=255
            elif randomcolgenerator<0:
                randomcolgenerator=0
            randomcol.append(randomcolgenerator)
        randomradius=(randint(0,20))
        
        #checks what tool is selected and does their function
        if tool=="pencil":
          draw.line(screen,currentcolor,(omx,omy),(mx,my))

        if tool=="eraser":
          draw.circle(screen,WHITE,(mx,my),radius)

        #draws circles in a certain radius
        if tool=="spraypaint":
            for i in range((radius+5)):
                randomintx = randint(-((radius+5)*2),((radius+5)*2))
                randominty = randint(-((radius+5)*2),((radius+5)*2))
                #makes sure circles are not too far from mouse (to have a circle)
                if hypot(randomintx, randominty) <= (radius+10):
                    draw.circle(screen,currentcolor,(mx+randomintx,my+randominty),(radius+10)*0.1)
        #draws some random circles with slightly varying colors
        if tool=="brush":

            brushtoolcolor=list(currentcolor)
            draw.circle(screen,randomcol,(mx+randomintx,my+randominty),(radius+10-randomradius))
        #saves an image of the screen and blits the image then wipes the screen(to update position)
        if tool =="stamp":
            screenCap=screen.subsurface(canvasRect).copy()
            screen.set_clip(canvasRect)
            screen.blit(listpics[selectedstamp],(mx-currentstampsizex//2,my-currentstampsizey//2))
            
            

        
        #shape tools, these use the position of the mouse when its first clicked, and current mouse position
        if tool == "Line":
            draw.line(screen, currentcolor, (sx, sy), (mx, my), radius)

        elif tool == "Rect":
            drawNewRect=Rect(sx,sy,mx-sx,my-sy)
            #normalize to make sure shapes can be drawn any way (even if mx is less than sx)
            drawNewRect.normalize()
            if filled==True:
                draw.rect(screen, currentcolor, drawNewRect)
            else:
                draw.rect(screen, currentcolor, drawNewRect,radius)

        elif tool == "Oval":
            #similar logic to rectangle
            drawNewOval=Rect(sx,sy,mx-sx,my-sy)
            drawNewOval.normalize()
            if filled==True:
                draw.ellipse(screen, currentcolor, drawNewOval)
            else:
                draw.ellipse(screen, currentcolor, drawNewOval,radius)
        screen.set_clip(None) 
    #sets slider colors to green
    paintslidercolor=GREEN
    stampslidercolor=GREEN
    colorhueSlidercolor=GREEN
    volSlidercolor=GREEN
    #if mouse goes over sliders, turn color to orange
    if paintsizeSlider.collidepoint(mx,my):
        paintslidercolor = ORANGE
    if stamSlider.collidepoint(mx,my):
        stampslidercolor = ORANGE
    if colhueSlider.collidepoint(mx,my):
        colorhueSlidercolor = ORANGE   
    if volSlider.collidepoint(mx,my):
        volSlidercolor = ORANGE  
         

    #set clips to none because no longer drawing
    screen.set_clip(None)
    
    draw.rect(screen, currentcolor, currentcolorvisual)
    #some logic for the sliders
    #draws a white square over the slider 
    draw.rect(screen, WHITE, (2+button1xoffset, 52 + buttonyoffset, 124, 38))
    draw.rect(screen, paintslidercolor, paintsizeSlider, 2)
    draw.rect(screen, RED, (sliderx, 52 + buttonyoffset, 10, 38), 10)
    draw.rect(screen, WHITE, (130+button1xoffset, 52 + buttonyoffset, 36, 36), 30)
    draw.circle(screen, currentcolor, (148+button1xoffset, 70 + buttonyoffset), radius) 
    #draws a new slider with the update position
    draw.rect(screen, WHITE, (450+button3xoffset, 50 + buttonyoffset, 208, 38))
    draw.rect(screen, stampslidercolor, stamSlider, 2)
    draw.rect(screen, RED, (stampsliderx+button3xoffset, 52 + buttonyoffset, 10, 38), 10)
    #blit the gradient image for the color slider
    screen.blit(whiteblackicon,(250+button2xoffset,buttonlayer2+buttonyoffset))
    draw.rect(screen, colorhueSlidercolor, colhueSlider, 2)
    draw.rect(screen, RED, (colorsliderx, 52 + buttonyoffset, 10, 38), 10)

    draw.rect(screen, WHITE, ((550+button4xoffset,buttonlayer2+buttonyoffset,124,40)))
    draw.rect(screen, volSlidercolor, volSlider, 2)
    draw.rect(screen, RED, (volsliderx+button4xoffset, 52 + buttonyoffset, 10, 38), 10)
    #calls function load the tool description
    loadtoolDescription(toolDescription)
    #fix the stamp bug
    fixstampbug+=1
    #i had an issue where if i tried to change the size of the stamps the stamps would get extremely blurry.
    if fixstampbug>=60 and stampsizechecker!=currentstampsizex and not stamSlider.collidepoint(mx,my): 
        #i fixed this by reloading the stamps every 1/6 of second if the size changed, and only if the size was not currently being changed.
        pi=image.load("Pics/pistamp.png")
        #this helps reduce the lag(by adding more conditions to reload)
        infinity=image.load("Pics/infinitysymbol.jpg")
        mring=image.load("Pics/mring.jpg")
        divide=image.load("Pics/dividesymbol.png")
        coolgraph=image.load("Pics/coolgraph.png")
        stampsizechecker=currentstampsizex

        fixstampbug=0
    #if tool is selected, turn their box to red
    if tool=="pencil":
        draw.rect(screen, RED, pencilRect, 2)
    if tool=="spraypaint":
        draw.rect(screen, RED, spraypaint, 2)
    if tool=="eraser":
        draw.rect(screen, RED, eraserRect, 2)
    if tool=="brush":
        draw.rect(screen, RED, brushRect, 2)
    if tool=="Line":
        draw.rect(screen, RED, drawLine, 2)
    if tool=="Oval":
        draw.rect(screen, RED, drawOval, 2)
    if tool=="Rect":
        draw.rect(screen, RED, drawRect, 2)
    if tool == "stamp":
        for i in range(5):
            #use eval for more efficient code
            if selectedstamp == i:
                stamp_rect = eval("stamp" + str(i + 1) + "Rect")
                draw.rect(screen, RED, stamp_rect, 2)
    if filled==1:
        draw.rect(screen,RED,filledCheckbox,2)

    
    #load music description, all files are classical with a num at the end
    loadmusicDescription("classical"+str(latestindex[-1]))
    #set all variables to false
    rightClick=False
    mouseup=False
    hoveringoverCircle=False
    #printcolwheel=False
    omx,omy=mx,my
    
    myClock.tick(240)
    display.flip()
    display.set_caption(str(myClock.get_fps()))

            
quit()
