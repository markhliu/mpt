from io import BytesIO

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Convert text to speech in Spanish
tts = gTTS(text='Buenos días',lang='es')
# Create a temporary file 
voice = BytesIO()
# Save the voice output as an audio file
tts.write_to_fp(voice)
# Play the audio file
voice.seek(0)
play(AudioSegment.from_mp3(voice))
