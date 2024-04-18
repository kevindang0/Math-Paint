#icons file to organize code
from pygame import *
#load all of the images
saveicon=image.load("Pics/saveiconblackwhite.png")
loadicon=image.load("Pics/openicon.png")


mathbg=image.load("Pics/mathbackground1cropped.jpg")
mathpaint=image.load("Pics/mathpainttransparent.png")
paintbrushicon=image.load("Pics/paintbrush.jpg")

pistampicon=image.load("Pics/pistamp.png")
infinityicon=image.load("Pics/infinitysymbol.jpg")
mringicon=image.load("Pics/mring.jpg")
divideicon=image.load("Pics/dividesymbol.png")
coolgraphicon=image.load("Pics/coolgraph.png")

whiteblackicon=image.load("Pics/whiteblackgradient.png")

newstamp=image.load("Pics/paintbrush.jpg")

spraypainticon=image.load("Pics/spraypainticon.png")
pencilicon=image.load("Pics/pencilicon.png")
erasericon=image.load("Pics/erasericon.jpg")
randomcircletool=image.load("Pics/paintbrush.jpg")
trashicon=image.load("Pics/trashicon.jpg")


linetoolicon=image.load("Pics/linetool.png")
squaretoolicon=image.load("Pics/squaretool.png")
circletoolicon=image.load("Pics/circletool.png")
filledtoolicon=image.load("Pics/filledsquareicon.png")

musicbackicon=image.load("Pics/musicback.png")
musicpauseicon=image.load("Pics/musicpause.png")
musicskipicon=image.load("Pics/musicskip.png")
musicplayicon=image.load("Pics/musicplay.png")


undotool=image.load("Pics/undotool.png")
redotool=image.load("Pics/redotool.png")
#transform all of the images to the appropriate size
mathbg = transform.smoothscale(mathbg, (1200, 200))
mathpaint = transform.smoothscale(mathpaint, (400, 100))

saveicon = transform.smoothscale(saveicon, (40, 40))
loadicon = transform.smoothscale(loadicon, (36, 36))

linetoolicon = transform.smoothscale(linetoolicon, (40, 40))
pencilicon = transform.smoothscale(pencilicon, (40, 40))
spraypainticon = transform.smoothscale(spraypainticon, (40, 40))
erasericon = transform.smoothscale(erasericon, (40, 40))
randomcircletool=transform.smoothscale(randomcircletool, (40, 40))
trashicon = transform.smoothscale(trashicon, (40, 40))

musicskipicon = transform.smoothscale(musicskipicon, (40, 40))
musicbackicon = transform.smoothscale(musicbackicon, (40, 40))
musicpauseicon = transform.smoothscale(musicpauseicon, (40, 40))
musicplayicon = transform.smoothscale(musicplayicon, (40, 40))

whiteblackicon = transform.smoothscale(whiteblackicon, (208,40))



undotool = transform.smoothscale(undotool, (40, 40))
redotool = transform.smoothscale(redotool, (40, 40))



pistampicon = transform.smoothscale(pistampicon, (40, 40))
infinityicon = transform.smoothscale(infinityicon, (40, 40))
mringicon = transform.smoothscale(mringicon, (40, 40))
divideicon = transform.smoothscale(divideicon, (40, 40))
coolgraphicon = transform.smoothscale(coolgraphicon, (40, 40))

mathbg = transform.smoothscale(mathbg, (1200, 200))

linetoolicon = transform.smoothscale(linetoolicon, (40, 40))
circletoolicon = transform.smoothscale(circletoolicon, (40, 40))
squaretoolicon = transform.smoothscale(squaretoolicon, (40, 40))
filledtoolicon = transform.smoothscale(filledtoolicon, (40, 40))

