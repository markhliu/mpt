# import the speech recognition module
import speech_recognition as sr

speech = sr.Recognizer()
def VTT():
    voice_input="" 
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input

# define a WakeUp() function to determine the status of the program
def WakeUp():
    ToWakeUp="StandBy"	
    voice_input="" 
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:        
            audio = speech.listen(source,timeout=2)
            voice_input = speech.recognize_google(audio).lower()
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    if "hello" in voice_input and "python" in voice_input:
            ToWakeUp="Activated" 
    elif "stop" in voice_input and ("listening" in voice_input or "program" in voice_input):
            ToWakeUp="ToQuit"  
    return ToWakeUp
