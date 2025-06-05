import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Intializing Voicely......")
    while True:
        # Listen for the wake word "Voicely"
        # Obtain audio from microphone
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                print("Recognizing.....")
            word = r.recognize_google(audio)
            if(word.lower() == "voicely"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Voicely active......")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
        except Exception as e:
            print("Error; {0}".format(e))