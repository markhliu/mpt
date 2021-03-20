# Make sure you put hello.mp3 in the same folder as this script
# Make sure VLC Media Player is installed on your computer
from vlc import MediaPlayer

player = MediaPlayer("hello.mp3")
player.play()

