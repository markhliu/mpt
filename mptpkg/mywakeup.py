# Get rid of ALSA lib error messages in Linux
import platform

if  platform.system() == "Linux":
    from ctypes import CFUNCTYPE, c_char_p, c_int, cdll
    
    # Define error handler
    error_handler = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
    # Don't do anything if there is an error message
    def py_error_handler(filename, line, function, err, fmt):
        pass
    # Pass to C
    c_error_handler = error_handler(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    
# Now define the wakeup() function for all platforms   
import speech_recognition as sr

speech = sr.Recognizer()
# define a wakeup() function to determine the status of the VPA
def wakeup():
    wakeup = "StandBy"	
    voice_input = "" 
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:        
            audio = speech.listen(source,timeout=3)
            voice_input = speech.recognize_google(audio).lower()
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    if "hello" in voice_input and "python" in voice_input:
        wakeup = "Activated" 
    elif "stop" in voice_input:
        wakeup = "ToQuit"  
    return wakeup
