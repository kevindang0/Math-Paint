#i set all of the button rectangles here to organize the code
from pygame import *
from musicplayer import *

tool=""

width,height=1200,800
screen=display.set_mode((width,height))
currentcolor = (100,0,0)
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
ORANGE=(255,127,80)
#set all of the variables
paintslidercolor = GREEN
stampslidercolor = GREEN
radius=5
sliderx=59
stampsliderx=540
colorsliderx=580
volsliderx = 580
buttonlayer1=2
buttonlayer2=50
buttonlayer3=96

myClock=time.Clock()
canvasRect=Rect(0,200,1200,600)

#i can change the buttons layout without having to indivdually change each number
buttonyoffset=10
button1xoffset=100
button2xoffset=230
button3xoffset=280
button4xoffset=450
#set all of the rectangle variables
saveRect=Rect(4,buttonlayer1+buttonyoffset,40,40)
loadRect=Rect(4,buttonlayer2+buttonyoffset,40,40)

undoRect=Rect(46,buttonlayer1+buttonyoffset,40,40)
redoRect=Rect(46,buttonlayer2+buttonyoffset,40,40)

pencilRect=Rect(44+button1xoffset,buttonlayer1+buttonyoffset,40,40)
eraserRect=Rect(86+button1xoffset, buttonlayer1+buttonyoffset ,40,40)
spraypaint=Rect(2+button1xoffset,buttonlayer1+buttonyoffset,40,40)
brushRect=Rect(128+button1xoffset,buttonlayer1+buttonyoffset,40,40)
trashRect=Rect(170+button1xoffset,buttonlayer1+buttonyoffset,40,40)

colChange=Rect(170+button1xoffset,buttonlayer2+buttonyoffset,40,40)
currentcolorvisual=Rect(172+button1xoffset,52+buttonyoffset,36,36)


musskip=Rect(634+button4xoffset,buttonlayer1+buttonyoffset,40,40)
muspause=Rect(592+button4xoffset, buttonlayer1+buttonyoffset, 40,40)
musback=Rect(550+button4xoffset,buttonlayer1+buttonyoffset,40,40)


paintsizeSlider=Rect(2+button1xoffset,buttonlayer2+buttonyoffset,124,40)
sizeCircle=Rect(128+button1xoffset, buttonlayer2+buttonyoffset, 40,40)
paintsliderSlide=Rect(sliderx+button1xoffset,buttonlayer2+buttonyoffset,10,38)
paintsizeSliderCollison=Rect(16+button1xoffset,buttonlayer2+buttonyoffset,112,40)

colhueSlider=Rect(250+button2xoffset,buttonlayer2+buttonyoffset,208,40)
#Rect(252+button2xoffset,50+buttonyoffset,200,40)
colorsliderSlide=Rect(colorsliderx,buttonlayer2+buttonyoffset,10,38)
colorhueSliderCollison=Rect(252+button2xoffset,buttonlayer2+buttonyoffset,196,40)

drawRect=Rect(250+button2xoffset,96+buttonyoffset,40,40)
drawLine=Rect(292+button2xoffset,96+buttonyoffset,40,40)
drawOval=Rect(334+button2xoffset,96+buttonyoffset,40,40)
filledCheckbox=Rect(376+button2xoffset,96+buttonyoffset,40,40)
#unfilledCheckbox=Rect(418+button2xoffset,50+buttonyoffset,40,40)

colorsave1=Rect(250+button2xoffset,buttonlayer1+buttonyoffset,40,40)
colorsave2=Rect(292+button2xoffset,buttonlayer1+buttonyoffset,40,40)
colorsave3=Rect(334+button2xoffset,buttonlayer1+buttonyoffset,40,40)
colorsave4=Rect(376+button2xoffset,buttonlayer1+buttonyoffset,40,40)
colorsave5=Rect(418+button2xoffset,buttonlayer1+buttonyoffset,40,40)

savedcolor1=Rect(252+button2xoffset,4+buttonyoffset,36,36)
savedcolor2=Rect(294+button2xoffset,4+buttonyoffset,36,36)
savedcolor3=Rect(336+button2xoffset,4+buttonyoffset,36,36)
savedcolor4=Rect(378+button2xoffset,4+buttonyoffset,36,36)
savedcolor5=Rect(420+button2xoffset,4+buttonyoffset,36,36)

#colorboxRect=Rect(200,150,800,475)

stamp1Rect = Rect(450+button3xoffset,buttonlayer1+buttonyoffset,40,40)
stamp2Rect = Rect(492+button3xoffset,buttonlayer1+buttonyoffset,40,40)
stamp3Rect = Rect(534+button3xoffset,buttonlayer1+buttonyoffset,40,40)
stamp4Rect = Rect(576+button3xoffset,buttonlayer1+buttonyoffset,40,40)
stamp5Rect = Rect(618+button3xoffset,buttonlayer1+buttonyoffset,40,40)

stampLoadRect = Rect(618+button3xoffset,buttonlayer2+buttonyoffset,40,40)

stamSlider=Rect(450+button3xoffset,buttonlayer2+buttonyoffset,208,40)
stampsizeSliderCollison=Rect(450+button3xoffset,buttonlayer2+buttonyoffset,196,40)
stampsliderSlide=Rect(stampsliderx+button3xoffset,52+buttonyoffset,10,38)

volSlider=Rect(550+button4xoffset,buttonlayer2+buttonyoffset,124,40)
volSliderCollison=Rect(552+button4xoffset,buttonlayer2+buttonyoffset,112,40)
volsliderSlide=Rect(volsliderx+button4xoffset,52+buttonyoffset,10,38)

toolDescriptionRect = Rect(250+button2xoffset,42+buttonlayer3+buttonyoffset,400,50)

musDescriptionRect = Rect(510+button4xoffset,42+buttonlayer2+buttonyoffset,200,90)
#draw canvas
draw.rect(screen, WHITE, (canvasRect))
#list of all the button names for the draw buttons function (in main.py)
button_names = [
        "saveRect", "loadRect", "undoRect", "redoRect","pencilRect", "eraserRect", "spraypaint", "brushRect","colChange",
        "trashRect","sizeCircle","musback", "muspause", "musskip", "drawLine", "drawOval", "drawRect",
        "filledCheckbox", "colorsave1", "colorsave2", "colorsave3",
        "colorsave4", "colorsave5", "stamp1Rect", "stamp2Rect", "stamp3Rect", "stamp4Rect", "stamp5Rect", "paintsizeSlider",
          "stamSlider", "stampLoadRect","colhueSlider", "musDescriptionRect", "volSlider"
    ]
#load color wheel
colorwheel=image.load("Pics/colorwheel.png")
colorwheel=transform.smoothscale(colorwheel,(150,150))

screen.blit(colorwheel,(325,10))
draw.rect(screen,GREEN,sizeCircle)

savedColors=[(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255)]


        

selectedColor =(0,0,0)




