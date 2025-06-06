import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "492f089dc50143c9a89420fed37393f8"

def speak(text):
    engine.say(text)
    engine.runAndWait()


def aiprocess(command):
    client = OpenAI(
        api_key = "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"
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "system", "content": "You are a virtual assitant named Voicely skilled in general tasks like ALexa and google cloud"},
        {"role": "user", "content": command}
    ]
    )
    return (completion.choices[0].message.content)


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey=492f089dc50143c9a89420fed37393f8")
        if r.status_code == 200:
            #Parse the JSON response
            data = r.json()
            #Extract the articles
            articles = data.get('articles', [])
            #Print the headlines
            for article in articles:
                speak(article['title'])
    
    else:
        #Let OpenAI handle the request
        output = aiprocess(c)
        speak(output)


if __name__ == "__main__":
    speak("Intializing Voicely......")
    while True:
        # Listen for the wake word "Voicely"
        # Obtain audio from microphone
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source, timeout=5, phrase_time_limit=6)
                print("Recognizing.....")
            word = r.recognize_google(audio)
            print("heard: ", word)
            if(word.lower() == "hello"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Voicely active......")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))