import pyttsx3
import datetime
import webbrowser
import wikipedia
import os
from requests import get
import pywhatkit
import smtplib
import sys

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gamil.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id ', 'your password')
    server.sendmail('your email id', to, content)
    server.close()

if __name__=="__main__":
        wishMe()
        while True:
            query = InputCommand().lower()
            if 'open youtube' in query:
                speak("opening youtube")
                webbrowser.open('http://www.youtube.com')

            elif 'open google' in query:
                speak("sir, what should i search on google")
                cd = InputCommand().lower()
                webbrowser.open(f"{cd}")

            elif 'open geeks' in query:
                speak("opening geeksforgeeks")
                webbrowser.open('https://www.geeksforgeeks.org/python-programming-language/?ref=shm')

            elif 'open github' in query:
                speak("opening Github")
                webbrowser.open('https://github.com/RohitLuni0101')

            elif 'open stackoverflow' in query:
                speak("opening Stackoverflow")
                webbrowser.open('https://stackoverflow.com')

            elif 'open mail' in query:
                speak("opening Gmail")
                webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

            elif 'open notepad' in query:
                speak('Opening Notepad')
                Npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(Npath)

            elif 'open control' in query:
                speak('Opening control')
                os.system("start control panel")

            elif 'open command' in query:
                speak('Opening command prompt')
                os.system("start cmd")

            elif 'open pc' in query:
                speak('Opening This Pc')
                os.system("start This PC")

            elif 'wikipedia' in query:
                speak("Searching wikipedia....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)


            elif 'play music' in query:
                music_dir ="E:\Music\Genral Music"
                song = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, song[11]))
                speak("playing music")

            elif 'ip address' in query:
                ip = get('https://api.ipify.org').text
                speak(f'Your Ip Address is {ip}')

            elif 'search youtube' in query:
                speak("sir, what should i search on youtube")
                query = InputCommand().lower()
                pywhatkit.playonyt(query)

            elif 'email to rohit' in query:
                try:
                    speak("sir, what should i say?")
                    content = InputCommand().lower()
                    to = "email id"
                    sendEmail(to, content)
                    speak("Email has been sent to ")
                except Exception as e:
                    print(e)
                    speak("sorry sir, i am not able to sent this mail to rohit")

            elif 'no thanks' in query:
                speak("thanks for using me sir, have a good day.")
                sys.exit()

            speak("sir, do you have any other work")

