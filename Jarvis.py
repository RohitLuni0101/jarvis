import pyttsx3
import datetime
import webbrowser
import wikipedia
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir. Please tell me how  may I help you")

def InputCommand():
    command = input("enter the command: ")
    return command


if __name__=="__main__":
        wishMe()
        while True:
            query = InputCommand().lower()
            if 'open youtube' in query:
                speak("opening youtube")
                webbrowser.open('http://www.youtube.com')

            elif 'open google' in query:
                speak("opening google")
                webbrowser.open('http://www.google.com')

            elif 'open geeks' in query:
                speak("opening geeksforgeeks")
                webbrowser.open('https://www.geeksforgeeks.org/python-programming-language/?ref=shm')

            elif 'open github' in query:
                speak("opening Github")
                webbrowser.open('https://github.com')

            elif 'open mail' in query:
                speak("opening Gmail")
                webbrowser.open('https://mail.google.com')

            elif 'search' in query:
                speak("Searching wikipedia....")
                query = query.replace("search", "")
                results = wikipedia.summary(query, sentences=10)
                speak("According to Wikipedia")
                speak(results)

            elif 'play music' in query:
                music_dir ='E:\Music\Genral Music'
                song = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, song[11]))
                speak("playing music")
                print(song[11])

