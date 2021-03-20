# Make sure you put hello.mp3 in the same folder as this script
from pygame import mixer

mixer.init()
mixer.music.load("hello.mp3")
mixer.music.play()
