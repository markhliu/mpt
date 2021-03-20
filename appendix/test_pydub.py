from pydub import AudioSegment
from pydub.playback import play

play(AudioSegment.from_mp3("../hello.mp3"))

