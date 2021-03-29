import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning")
    elif hour>=12 and hour<15:
        print("Good Afternoon")
    else:
        print("Good Evening")
    print("I am Alpha, How can I help you!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")

    except Exception as e:

        print("Please say that again....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('edvinshabu@gmail.com','text-password')
    server.sendmail('edvinshabu@gmail.com', to, content)
    server.close()


wishMe()
while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        print("According to wikipedia...")
        print(results)
 
    elif 'youtube' in query:
        webbrowser.open("youtube.com")
    elif 'search' in query:
        webrowser.open("google.com")

    elif 'play song' in query:
        music_dir = '/home/edooo/Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'send a email' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "edwinshabu1998@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("I am unable to send this!")
    elif 'bye' in query:
        exit()
