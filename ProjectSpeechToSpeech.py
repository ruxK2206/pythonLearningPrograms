import speech_recognition as sr
import pyttsx3
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak something...")
    recognizer.adjust_for_ambient_noise(source)  
    audio_data = recognizer.listen(source)       
try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio_data)
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print("Error occurred during recognition: {0}".format(e))
engine = pyttsx3.init()
engine.setProperty('rate', 150)    
engine.setProperty('volume', 0.9)  
engine.say(text)
engine.runAndWait()
