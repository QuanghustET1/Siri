#import thư viện
import speech_recognition as Sr
from gtts import gTTS
import pyttsx3
from time import ctime
import os
from datetime import date
from datetime import datetime
import webbrowser

sr_ear= Sr.Recognizer()
while True:
    with Sr.Microphone() as mic:
        print("Sr: I'm Listening...")
        robot_mouth = pyttsx3.init()
        robot_mouth.say("I'm Listening")
        robot_mouth.runAndWait()
        audio= sr_ear.record(mic, duration= 5)
    print("Sr: ...")
    try:
        you= sr_ear.recognize_google(audio)
    except:
        you="..."
    #Communication

    if you=="how are you":
        robot_brain="i'm fine thanks, and you"
        
    elif you== "hello":
        robot_brain= "Hello Quang handsome"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%d/%m/%Y %H:%M:%S")
    elif "goodbye" in you:
        robot_brain="Goodbye Quang, i love you"
        print("Sr: "+robot_brain)
        robot_mouth = pyttsx3.init()
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    #Open youtube
    elif "open" in you:
        url = f"https://www.youtube.com"
        webbrowser.get().open(url)
        robot_brain="ok,open youtube"
    #Open Facebook
    elif "ok" in you:
        url = f"https://www.facebook.com"
        webbrowser.get().open(url)
        robot_brain="ok,open Facebook"
    #Music
    elif "music" in you:
        url=f"https://www.youtube.com/watch?v=qs1_yp-_V_w"
        webbrowser.get().open(url)
        robot_brain= "Ok, Have fun"
        print("Sr: "+robot_brain)
        robot_mouth = pyttsx3.init()
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    #Translate
    elif "..." in you:
        
        said= Sr.Recognizer()
        while True:
            robot_brain="What word do you want to translate"
            print("Sr: "+robot_brain)
            robot_mouth = pyttsx3.init()
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            with Sr.Microphone() as micro:            
                audio_said= said.record(micro, duration= 8)
                print("Sr: ...")
            try:
                you_said= said.recognize_google(audio_said)
            except:
                you_said="..."
            print(you_said)
            if you_said=="...":
                continue
            elif "stop" in you_said:
                robot_brain="ok, sir"
                print("Sr: "+robot_brain)
                robot_mouth = pyttsx3.init()
                robot_mouth.say(robot_brain)
                robot_mouth.runAndWait()
                break
            else:
                url=f"https://translate.google.com/?hl=vi#view=home&op=translate&sl=en&tl=vi&text="+you_said
                robot_brain= "ok, waitting me"
                print("Sr: "+robot_brain)
                robot_mouth = pyttsx3.init()
                robot_mouth.say(robot_brain)
                robot_mouth.runAndWait()
                webbrowser.get().open(url)
    if robot_brain=="ok, sir":
        break
            

        
    #Speak
    print("Sr: "+robot_brain)
    robot_mouth = pyttsx3.init()
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
