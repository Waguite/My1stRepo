import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Hi Ware, what do you want to search for?")
    print ("listening...")
    audio = r.listen(source)
    print("Thinking...")

try:
    words = r.recognize_google(audio)
    speak.Speak("Ok Ware, lets look for " + r.recognize_google(audio) + "on Google.")
    wb.open("https:google.com/search?q=" + words)
    
except sr. UnknownValueError:
    print("google speech recognition could not understand audio")
except sr.requestError as e:
    print("could not request results from google speech recognition service; {0}".format(e))
