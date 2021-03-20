# Make sure you put hello.mp3 in the same folder as this script
from pydub import AudioSegment
from pydub.playback import play

play(AudioSegment.from_mp3("hello.mp3"))

