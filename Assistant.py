import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
import wolframalpha
import subprocess
import pyttsx3
import pyjokes
import feedparser
import smtplib
import time
import requests
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


print("Donut Assistant 12.5.0")
print("Assistant for PCs")
print("Donut Open Source Software Projects - Gautham Nair @ 2023")

assistanttype = input("Please Select any one: \n \t 1.Donut Assistant Mike \n \t 2.Donut Assistant Annie \n \t 3.Donut Assistant Chloe \n : ")
default_engine = input("Select a default search engine: \n \t Google \n \t Bing \n")
if assistanttype == "1":
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)


    def speak(audio):                   
        engine.say(audio)
        engine.runAndWait()


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print("Good Morning!")
            speak("Good Morning!")

        elif hour>=12 and hour<14:
            print("Good Afternoon!")
            speak("Good Afternoon!")

        else:
            print("Good Evening!")
            speak("Good Evening!")

        print("I am Donut Mike. Please tell me how may I help you")
        speak("I am Donut Mike. Ask me anything!!!")

    def takeCommand():
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")
            speak('I didnt hear anything, if you said anything please speak loud and clear')
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        email = input("Enter your gmail username: ")
        psswrd = input("Enter yourn gmail password: ")
        server.login(email, psswrd)
        server.sendmail(email, to, content)
        server.close()

    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif query == "tell me some jokes" or query == "tell some jokes" or query == "tell a joke" or query == "joke" or query == "jokes":
                My_joke = pyjokes.get_joke(language="en", category="neutral")
                print(My_joke)
                speak(My_joke)

            elif 'search' in query:
                speak('Searching '+ default_engine)
                query = query.replace(default_engine, "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to " + default_engine)
                print(results)
                speak(results)


            elif 'question' in query:
                speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                question=takeCommand()
                app_id="NULL"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)

            elif 'weather' in query:
                from bs4 import BeautifulSoup
                import requests
                headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win32; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


                def weather(city):
                        city = city.replace(" ", "+")
                        res = requests.get(
                                f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
                        print("Searching...\n")
                        soup = BeautifulSoup(res.text, 'html.parser')
                        location = soup.select('#wob_loc')[0].getText().strip()
                        time = soup.select('#wob_dts')[0].getText().strip()
                        info = soup.select('#wob_dc')[0].getText().strip()
                        weather = soup.select('#wob_tm')[0].getText().strip()
                        print(location)
                        speak(location)
                        print(time)
                        speak(time)
                        print(info)
                        speak(info)
                        print(weather+"°C")
                        speak(weather+"°C")


                city = input("Enter the Name of City -> ")
                city = city+" weather"
                weather(city)
                print("Have a Nice Day:)")

            elif "calculate" in query:

                app_id = "Wolframalpha api id"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            elif 'open youtube' in query:
                speak('OK, I will open YouTube in your default browser')
                webbrowser.open("youtube.com")

            elif 'open browser' in query:
                webbrowser.open("bing.com" or "google.com")

            elif 'open bing' in query:
                speak('Opening bing in your default browser')
                webbrowser.open("bing.com")

            elif 'send feedback' in query:
                speak('This will open Donut Support Website in your default browser, you can give feedback there!')
                webbrowser.open("Donutsupport.simdif.com")

            elif 'open google' in query:
                speak('Opening google in your default browser')
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                speak('Opening StackOverflow in your default browser')
                webbrowser.open("stackoverflow.com")   


            elif 'play music' in query:
                try:
                    musidir = input("Enter directory address: ")
                    music_dir = musidir
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
                except:
                    speak("Sorry Friend!! I couldn't find the directory specified")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Friend, the time is {strTime}")

            elif 'text to speech' in query:
                text = input("Type: ")
                speak(text)

            elif 'when is your birthday' in query:
                print("1st March 2022")
                speak('I made my debut on 1st March 2022')

            elif 'your developers name' in query:
                print("Gautham Nair")
                speak("Gautham Nair")

            elif 'open code' in query:
                codePath = "C:\\Users\\gauth\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'what is your name' in query:
                speak('As I told you in the beginning, my name is Donut Assistant Mike')
                print("I am Donut Assistant Mike")

            elif 'who made you' in query:
                speak('Who made me??? Gautham Nair')
                speak('He is super genius')

            elif 'what do you eat' in query:
                speak("I dont't eat the food that humans eat, but i like to have bits and bytes")

            elif 'where do you live' in query:
                speak("I live in your computer")

            elif 'can you sing a song' in query:
                speak('Im noot good at singing, since i am a bot')
                speak('But since you asked me, i will sing it for you')
                speak("I will sing my favourite song")
                speak("The song is Michael Jackson's Smooth Criminal") 
                speak('''As he came into the window!!!!
                            Was the sound of a crescendo!!!
                            He came into her apartment!!!
                            He left the bloodstains on the carpet!!!
                            She ran underneath the table!!!
                            He could see she was unable!!!
                            So she ran into the bedroom!!!
                            She was struck down, it was her doom!!!
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            Will you tell us that you're okay?
                            There's a sound at the window
                            Then he struck you, a crescendo Annie
                            He came into your apartment
                            He left the bloodstains on the carpet
                            And then you ran into the bedroom
                            You were struck down
                            It was your doom
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            You've been hit by-
                            You've been hit by-
                            A smooth criminal
                            So they came in to the outway
                            It was Sunday, what a black day
                            Mouth-to-mouth resuscitation
                            Sounding heartbeats, intimidation
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            Will you tell us that you're okay?
                            There's a sound at the window
                            That he struck you a crescendo Annie
                            He came into your apartment
                            He left the bloodstains on the carpet
                            Then you ran into the bedroom
                            You were struck down
                            It was your doom
                            Annie, are you okay? So, Annie, are you okay?
                            Are you okay, Annie?
                            You've been hit by-
                            You've been struck by-
                            A smooth criminal
                            Okay, I want everybody to clear the area right now
                            Annie, are you okay? (I don't know)
                            Will you tell us, that you're okay? (I don't know)
                            There's a sound at the window (I don't know)
                            Then he struck you, a crescendo Annie (I don't know)
                            He came into your apartment (I don't know)
                            Left bloodstains on the carpet (I don't know why, baby)
                            And then you ran into the bedroom (help me)
                            You were struck down
                            It was your doom, Annie (dag gone it)
                            Annie, are you okay? (Dag gone it-baby)
                            Will you tell us that you're okay? (Dag gone it-baby)
                            There's a sound at the window (dag gone it-baby)
                            Then he struck you, a crescendo Annie
                            He came into your apartment (dag gone it)
                            Left bloodstains on the carpet (hoo, hoo, hoo)
                            And then you ran into the bedroom
                            You were struck down (dag gone it)
                            It was your doom Annie''')

            elif 'can i change your name' in query:
                print("Sorry Friend!")
                speak("Sorry Friend!, only my developers can change my name")

            elif 'do you know alexa' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know cortana' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know google assistant' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know siri' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know bixby' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'who is your favourite artist' in query:
                print("Michael Jackson")
                speak('No doubt,, its michael jackson')

            elif 'exit' in query:
                print("Goodbye!!")
                speak('Goodbye!!, you can call me anytime')
                break

            elif 'email' in query:
                try:
                    useria = input("Email to whom?..Type it: ")
                    speak("What should I say?")
                    content = takeCommand()
                    to = useria    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")

            elif "log off" in query or "sign out" in query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

    time.sleep(3)

elif assistanttype == "2":
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print("Good Morning!")
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            print("Good Afternoon!")
            speak("Good Afternoon!")

        else:
            print("Good Evening!")
            speak("Good Evening!")

        print("I am Donut Annie. Please tell me how may I help you")
        speak("I am Donut Annie. Ask me anything!!!")

    def takeCommand():
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")
            speak('I didnt hear anything, if you said anything please speak loud and clear')
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        email = input("Enter your gmail username: ")
        psswrd = input("Enter yourn gmail password: ")
        server.login(email, psswrd)
        server.sendmail(email, to, content)
        server.close()

    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif query == "tell me some jokes" or query == "tell some jokes" or query == "tell a joke" or query == "joke" or query == "jokes":
                My_joke = pyjokes.get_joke(language="en", category="neutral")
                print(My_joke)
                speak(My_joke)

            elif 'search' in query:
                speak('Searching '+ default_engine)
                query = query.replace(default_engine, "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to " + default_engine)
                print(results)
                speak(results)


            elif 'question' in query:
                speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                question=takeCommand()
                app_id="Paste your unique ID here "
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)

            elif 'weather' in query:
                from bs4 import BeautifulSoup
                import requests
                headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win32; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


                def weather(city):
                        city = city.replace(" ", "+")
                        res = requests.get(
                                f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
                        print("Searching...\n")
                        soup = BeautifulSoup(res.text, 'html.parser')
                        location = soup.select('#wob_loc')[0].getText().strip()
                        time = soup.select('#wob_dts')[0].getText().strip()
                        info = soup.select('#wob_dc')[0].getText().strip()
                        weather = soup.select('#wob_tm')[0].getText().strip()
                        print(location)
                        speak(location)
                        print(time)
                        speak(time)
                        print(info)
                        speak(info)
                        print(weather+"°C")
                        speak(weather+"°C")


                city = input("Enter the Name of City -> ")
                city = city+" weather"
                weather(city)
                print("Have a Nice Day:)")

            elif "calculate" in query:

                app_id = "Wolframalpha api id"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            elif 'open youtube' in query:
                speak('OK, I will open YouTube in your default browser')
                webbrowser.open("youtube.com")

            elif 'open browser' in query:
                webbrowser.open("bing.com" or "google.com")

            elif 'open bing' in query:
                speak('Opening bing in your default browser')
                webbrowser.open("bing.com")

            elif 'send feedback' in query:
                speak('This will open Donut Support Website in your default browser, you can give feedback there!')
                webbrowser.open("Donutsupport.simdif.com")

            elif 'open google' in query:
                speak('Opening google in your default browser')
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                speak('Opening StackOverflow in your default browser')
                webbrowser.open("stackoverflow.com")   


            elif 'play music' in query:
                try:
                    musidir = input("Enter directory address: ")
                    music_dir = musidir
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
                except:
                    speak("Sorry Friend!! I couldn't find the directory specified")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Friend, the time is {strTime}")

            elif 'text to speech' in query:
                text = input("Type: ")
                speak(text)

            elif 'when is your birthday' in query:
                print("1st March 2022")
                speak('I made my debut on 1st March 2022')

            elif 'your developers name' in query:
                print("Gautham Nair")
                speak("Gautham Nair")

            elif 'open code' in query:
                codePath = "C:\\Users\\gauth\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'what is your name' in query:
                speak('As I told you in the beginning, my name is Donut Assistant Annie')
                print("I am Donut Assistant Annie")

            elif 'who made you' in query:
                speak('Who made me??? Gautham nair')
                speak('He is a super genius')

            elif 'what do you eat' in query:
                speak("I dont't eat the food that humans eat, but i like to have bits and bytes")

            elif 'where do you live' in query:
                speak("I live in your computer")

            elif 'can you sing a song' in query:
                speak('Im noot good at singing, since i am a bot')
                speak('But since you asked me, i will sing it for you')
                speak("I will sing my favourite song")
                speak("This song has my name in it!!")
                speak("The song is Michael Jackson's Smooth Criminal") 
                speak('''As he came into the window!!!!
                            Was the sound of a crescendo!!!
                            He came into her apartment!!!
                            He left the bloodstains on the carpet!!!
                            She ran underneath the table!!!
                            He could see she was unable!!!
                            So she ran into the bedroom!!!
                            She was struck down, it was her doom!!!
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            Will you tell us that you're okay?
                            There's a sound at the window
                            Then he struck you, a crescendo Annie
                            He came into your apartment
                            He left the bloodstains on the carpet
                            And then you ran into the bedroom
                            You were struck down
                            It was your doom
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            You've been hit by-
                            You've been hit by-
                            A smooth criminal
                            So they came in to the outway
                            It was Sunday, what a black day
                            Mouth-to-mouth resuscitation
                            Sounding heartbeats, intimidation
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            Will you tell us that you're okay?
                            There's a sound at the window
                            That he struck you a crescendo Annie
                            He came into your apartment
                            He left the bloodstains on the carpet
                            Then you ran into the bedroom
                            You were struck down
                            It was your doom
                            Annie, are you okay? So, Annie, are you okay?
                            Are you okay, Annie?
                            You've been hit by-
                            You've been struck by-
                            A smooth criminal
                            Okay, I want everybody to clear the area right now
                            Annie, are you okay? (I don't know)
                            Will you tell us, that you're okay? (I don't know)
                            There's a sound at the window (I don't know)
                            Then he struck you, a crescendo Annie (I don't know)
                            He came into your apartment (I don't know)
                            Left bloodstains on the carpet (I don't know why, baby)
                            And then you ran into the bedroom (help me)
                            You were struck down
                            It was your doom, Annie (dag gone it)
                            Annie, are you okay? (Dag gone it-baby)
                            Will you tell us that you're okay? (Dag gone it-baby)
                            There's a sound at the window (dag gone it-baby)
                            Then he struck you, a crescendo Annie
                            He came into your apartment (dag gone it)
                            Left bloodstains on the carpet (hoo, hoo, hoo)
                            And then you ran into the bedroom
                            You were struck down (dag gone it)
                            It was your doom Annie''')

            elif 'can i change your name' in query:
                print("Sorry Friend!")
                speak("Sorry Friend!, only my developers can change my name")

            elif 'do you know alexa' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know cortana' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know google assistant' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know siri' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know bixby' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'who is your favourite artist' in query:
                print("Michael Jackson")
                speak('No doubt,, its michael jackson')

            elif 'exit' in query:
                print("Goodbye!!")
                speak('Goodbye!!, you can call me anytime')
                break

            elif 'email' in query:
                try:
                    useria = input("Email to whom?..Type it: ")
                    speak("What should I say?")
                    content = takeCommand()
                    to = useria    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")

            elif "log off" in query or "sign out" in query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

    time.sleep(3)

elif assistanttype == "3":
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print("Good Morning!")
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            print("Good Afternoon!")
            speak("Good Afternoon!")

        else:
            print("Good Evening!")
            speak("Good Evening!")

        print("I am Donut Chloe. Please tell me how may I help you")
        speak("I am Donut Chloe. Ask me anything!!!")

    def takeCommand():
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")
            speak('I didnt hear anything, if you said anything please speak loud and clear')
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        email = input("Enter your gmail username: ")
        psswrd = input("Enter yourn gmail password: ")
        server.login(email, psswrd)
        server.sendmail(email, to, content)
        server.close()

    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif query == "tell me some jokes" or query == "tell some jokes" or query == "tell a joke" or query == "joke" or query == "jokes":
                My_joke = pyjokes.get_joke(language="en", category="neutral")
                print(My_joke)
                speak(My_joke)

            elif 'search' in query:
                speak('Searching '+ default_engine)
                query = query.replace(default_engine, "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to " + default_engine)
                print(results)
                speak(results)


            elif 'question' in query:
                speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                question=takeCommand()
                app_id="Paste your unique ID here "
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)

            elif 'weather' in query:
                from bs4 import BeautifulSoup
                import requests
                headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win32; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


                def weather(city):
                        city = city.replace(" ", "+")
                        res = requests.get(
                                f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
                        print("Searching...\n")
                        soup = BeautifulSoup(res.text, 'html.parser')
                        location = soup.select('#wob_loc')[0].getText().strip()
                        time = soup.select('#wob_dts')[0].getText().strip()
                        info = soup.select('#wob_dc')[0].getText().strip()
                        weather = soup.select('#wob_tm')[0].getText().strip()
                        print(location)
                        speak(location)
                        print(time)
                        speak(time)
                        print(info)
                        speak(info)
                        print(weather+"°C")
                        speak(weather+"°C")


                city = input("Enter the Name of City -> ")
                city = city+" weather"
                weather(city)
                print("Have a Nice Day:)")

            elif "calculate" in query:

                app_id = "Wolframalpha api id"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)

            elif 'open youtube' in query:
                speak('OK, I will open YouTube in your default browser')
                webbrowser.open("youtube.com")

            elif 'open browser' in query:
                webbrowser.open("bing.com" or "google.com")

            elif 'open bing' in query:
                speak('Opening bing in your default browser')
                webbrowser.open("bing.com")

            elif 'send feedback' in query:
                speak('This will open Donut Support Website in your default browser, you can give feedback there!')
                webbrowser.open("Donutsupport.simdif.com")

            elif 'open google' in query:
                speak('Opening google in your default browser')
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                speak('Opening StackOverflow in your default browser')
                webbrowser.open("stackoverflow.com")   


            elif 'play music' in query:
                try:
                    musidir = input("Enter directory address: ")
                    music_dir = musidir
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
                except:
                    speak("Sorry Friend!! I couldn't find the directory specified")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Friend, the time is {strTime}")

            elif 'text to speech' in query:
                text = input("Type: ")
                speak(text)

            elif 'when is your birthday' in query:
                print("1st March 2022")
                speak('I made my debut on 1st March 2022')

            elif 'your developers name' in query:
                print("Gautham Nair")
                speak("Gautham Nair")

            elif 'open code' in query:
                codePath = "C:\\Users\\gauth\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'what is your name' in query:
                speak('As I told you in the beginning, my name is Donut Assistant Chloe')
                print("I am Donut Assistant Chloe")

            elif 'who made you' in query:
                speak('Gautham Nair')

            elif 'what do you eat' in query:
                speak("I dont't eat the food that humans eat, but i like to have bits and bytes")

            elif 'where do you live' in query:
                speak("I live in your computer")

            elif 'can you sing a song' in query:
                speak('Im noot good at singing, since i am a bot')
                speak('But since you asked me, i will sing it for you')
                speak("I will sing my favourite song")
                speak("The song is Michael Jackson's Smooth Criminal") 
                speak('''As he came into the window!!!!
                            Was the sound of a crescendo!!!
                            He came into her apartment!!!
                            He left the bloodstains on the carpet!!!
                            She ran underneath the table!!!
                            He could see she was unable!!!
                            So she ran into the bedroom!!!
                            She was struck down, it was her doom!!!
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            Will you tell us that you're okay?
                            There's a sound at the window
                            Then he struck you, a crescendo Annie
                            He came into your apartment
                            He left the bloodstains on the carpet
                            And then you ran into the bedroom
                            You were struck down
                            It was your doom
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            You've been hit by-
                            You've been hit by-
                            A smooth criminal
                            So they came in to the outway
                            It was Sunday, what a black day
                            Mouth-to-mouth resuscitation
                            Sounding heartbeats, intimidation
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            So, Annie, are you okay? Are you okay, Annie?
                            Annie, are you okay?
                            Will you tell us that you're okay?
                            There's a sound at the window
                            That he struck you a crescendo Annie
                            He came into your apartment
                            He left the bloodstains on the carpet
                            Then you ran into the bedroom
                            You were struck down
                            It was your doom
                            Annie, are you okay? So, Annie, are you okay?
                            Are you okay, Annie?
                            You've been hit by-
                            You've been struck by-
                            A smooth criminal
                            Okay, I want everybody to clear the area right now
                            Annie, are you okay? (I don't know)
                            Will you tell us, that you're okay? (I don't know)
                            There's a sound at the window (I don't know)
                            Then he struck you, a crescendo Annie (I don't know)
                            He came into your apartment (I don't know)
                            Left bloodstains on the carpet (I don't know why, baby)
                            And then you ran into the bedroom (help me)
                            You were struck down
                            It was your doom, Annie (dag gone it)
                            Annie, are you okay? (Dag gone it-baby)
                            Will you tell us that you're okay? (Dag gone it-baby)
                            There's a sound at the window (dag gone it-baby)
                            Then he struck you, a crescendo Annie
                            He came into your apartment (dag gone it)
                            Left bloodstains on the carpet (hoo, hoo, hoo)
                            And then you ran into the bedroom
                            You were struck down (dag gone it)
                            It was your doom Annie''')

            elif 'can i change your name' in query:
                print("Sorry Friend!")
                speak("Sorry Friend!, only my developers can change my name")

            elif 'do you know alexa' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know cortana' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know google assistant' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know siri' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'do you know bixby' in query:
                speak("Yes, I know her, I want to be famous like her one day")

            elif 'who is your favourite artist' in query:
                print("Michael Jackson")
                speak('No doubt,, its michael jackson')

            elif 'exit' in query:
                print("Goodbye!!")
                speak('Goodbye!!, you can call me anytime')
                break

            elif 'email' in query:
                try:
                    useria = input("Email to whom?..Type it: ")
                    speak("What should I say?")
                    content = takeCommand()
                    to = useria    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend. I am not able to send this email")

            elif "log off" in query or "sign out" in query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

    time.sleep(3)




