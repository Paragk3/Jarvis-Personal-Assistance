import sys
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import shutil
import requests
import time
import json
import wolframalpha
import pyjokes
from ecapture import ecapture as ec
from urllib.request import urlopen
from playsound import playsound 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType 

from jarvisUi import Ui_MainWindow


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
        playaudio('C:\\Users\\ASUS\Downloads\\jarvis\\Jarvis.mp3')

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!") 
        playaudio('C:\\Users\\ASUS\Downloads\\jarvis\\Jarvis.mp3')  

    else:
        speak("Good Evening sir!") 
        playaudio('C:\\Users\\ASUS\Downloads\\jarvis\\Jarvis.mp3')
        
        
assname =("Jarvis 1 point o")

def playaudio(path_of_audio):
         playsound(path_of_audio) 


def usrname():
    speak("What should i call you sir")
    MainThread.uname = MainThread.takeCommand()
    speak("hello")
    speak(MainThread.uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.",MainThread.uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")

    


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('paragkhirade83@gmail.com', 'Passord')
    server.sendmail('paragkhirade83@gmail.com', to, content)
    server.close()
    
        
class MainThread(QThread):
    

    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution   
        

    def takeCommand(self):
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
            return "None"
           
        return self.query    

    def TaskExecution(self):
        wishMe()
        usrname()

        while True:
                # if 1:
                self.query =self.takeCommand()
                
                # Logic for executing tasks based on query
                if 'wikipedia' in self.query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in self.query:
                    speak("Here you go to Youtube\n")
                    webbrowser.open("youtube.com")
                    

                elif 'open google' in self.query:
                    speak("opening google for you sir\n")
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in self.query:
                    speak("opening stackoverflow for you sir\n")
                    webbrowser.open("stackoverflow.com")

                elif 'joke' in self.query:
                    speak(pyjokes.get_joke()) 

                elif "change name" in self.query:
                    speak("What would you like to call me, Sir ")
                    assname = self.takeCommand()
                    speak("Thanks for naming me")
        
                elif "what's your name" in self.query or "What is your name" in self.query:
                    speak("My friends call me")
                    speak(assname)
                    print("My friends call me", assname)          


                elif 'play music' in self.query:
                    speak("huh playing music for you sir\n")
                    music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'the time' in self.query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                elif 'how are you' in self.query:
                    speak("I am fine, Thank you")
                    speak("How are you, Sir")
        
                elif 'fine' in self.query or "good" in self.query:
                    speak("It's good to know that your fine")
            
                elif 'open code' in self.query:
                    codePath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)

                elif "can you please stop" in self.query:
                    
                    speak("yes sir why not im here for you")
                    


                elif 'search' in self.query or 'play' in self.query:
                    
                    self.query = self.query.replace("search", "")
                    self.query = self.query.replace("play", "")         
                    webbrowser.open(query)
        
                elif "who i am" in self.query:
                    speak("If you talk then definately your human.")    

                elif 'email to Parag' in self.query:
                    try:
                        speak("What should I say?")
                        content = self.takeCommand()
                        to = "paragkhirade83@gmail.com"    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Im sorry Parag. I am not able to send this email")



                elif "calculate" in self.query:
                    
                    app_id = 'UXL2X8-APKQJ3QH5Y'
                    client = wolframalpha.Client(app_id)
                    indx = query.lower().split().index('calculate')
                    query = query.split()[indx + 1:]
                    res = client.query(' '.join(query))
                    answer = next(res.results).text
                    print("The answer is " + answer)
                    speak("The answer is " + answer)

                elif "what is" in self.query or "who is" in self.query:
                    
                    # Use the same API key
                    # that we have generated earlier
                    client = wolframalpha.Client("UXL2X8-APKQJ3QH5Y")
                    res = client.query(query)
                    
                    try:
                        print (next(res.results).text)
                        speak (next(res.results).text)
                    except StopIteration:
                        print ("No results")  

                elif "write a note" in self.query:
                    speak("What should i write, sir")
                    note = self.takeCommand()
                    file = open('jarvis.txt', 'w')
                    speak("Sir, Should i include date and time")
                    snfm = self.takeCommand()
                    if 'yes' in snfm or 'sure' in snfm:
                        strTime = datetime.datetime.now().strftime("% H:% M:% S")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)
                
                elif "show note" in self.query:
                    speak("Showing Notes")
                    file = open("jarvis.txt", "r")
                    print(file.read())
                    speak(file.read(6))  

                elif "don't listen" in query or "stop listening" in self.query:
                    speak("for how much time you want to stop jarvis from listening commands")
                    a = int(self.takeCommand())
                    time.sleep(a)
                    print(a)

                elif "weather" in self.query:
                    
                    # Google Open weather website
                    # to get API of Open weather
                    api_key = 'b2a43febe87c192304d38bf8e9b27d64'
                    base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
                    speak(" City name ")
                    print("City name : ")
                    city_name = self.takeCommand()
                    complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                    response = requests.get(complete_url)
                    x = response.json()
                    
                    if x["cod"] != "404":
                        y = x["main"]
                        current_temperature = y["temp"]
                        current_pressure = y["pressure"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                    
                    else:
                        speak(" City Not Found ")
        
                elif "where is" in self.query:
                    self.query = self.query.replace("where is", "")
                    location = self.query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        
                elif "camera" in self.query or "take a photo" in self.query:
                    ec.capture(0, "Jarvis Camera ", "img.jpg")
        
                    
                elif 'news' in self.query:
                        
                    try:
                        jsonObj = urlopen("https://newsapi.org/v2/everything?q=apple&from=2021-05-30&to=2021-05-30&sortBy=popularity&apiKey=266057daf8b94bbc88408cc923e7916a")
                        data = json.load(jsonObj)
                        i = 1
                        
                        speak('here are some top news from the times of india')
                        print('''=============== TIMES OF INDIA ============'''+ '\n')
                        
                        for item in data['articles']:
                            
                            print(str(i) + '. ' + item['title'] + '\n')
                            print(item['description'] + '\n')
                            speak(str(i) + '. ' + item['title'] + '\n')
                            i += 1
                    except Exception as e:
                        
                        print(str(e))
                
                elif 'exit' in self.query:
                    speak("Thanks for giving me your time")
                    exit()    

startExecution = MainThread()

class main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    
    def startTask(self):
        
        self.ui.movie = QtGui.QMovie("C:/Jarvis the Personal Assistance/Jarvisui/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Jarvis the Personal Assistance/Jarvisui/jarvis2.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Jarvis the Personal Assistance/Jarvisui/jarvis1 gif.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:/Jarvis the Personal Assistance/Jarvisui/jarvis gif.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        

        
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        lable_time = current_time.toString('hh:mm:ss')
        lable_date = current_date.toString(Qt.ISODate) 
        self.ui.textBrowser.setText(lable_date)  
        self.ui.textBrowser_2.setText(lable_time)
    
    


app = QApplication(sys.argv)
jarvis = main()
jarvis.show()
exit(app.exec_())
    