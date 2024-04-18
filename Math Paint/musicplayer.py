from pygame import *
#music player file

init()
mixer.init()
#some variables to keep track of what song is currently playing and whether its paused
musicindex = 1
musicPause = True

latestindex = []
latestindex.append(1)
#load first song
mixer.music.load("Music/classical1.mp3")
#play song
mixer.music.play(loops=-1)

mixer.music.set_volume(0.3)
#pause the song so that it doesnt automatically play
mixer.music.pause()
#some functions for the music player
def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()

if musicPause==True:
    pause_music()
else: 
    unpause_music()
# add one to the index to go to next song
def skipsong():
    global musicindex
    musicindex+=1
    if musicindex==4:
        musicindex=1

def backsong():
    global musicindex
    musicindex-=1
    if musicindex==0:
        musicindex=(3)
#load song and play the song
def loadsong():

    global musicindex
    if musicindex == 1:
        mixer.music.load("Music/classical1.mp3")
    if musicindex==2:
        mixer.music.load("Music/classical2.mp3") 
    if musicindex==3:
        mixer.music.load("Music/classical3.mp3")
    mixer.music.play(loops=-1)
    #append the music index (for some reason i couldnt get it to work when i was just using music index for other features)
    latestindex.append(musicindex)

