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
with Sr.Microphone() as mic:
    print("Sr: I'm Listening...")
    robot_mouth = pyttsx3.init()
    robot_mouth.say("I'm Listening")
    robot_mouth.runAndWait()
    
while True:
    with Sr.Microphone() as mic:
        audio= sr_ear.record(mic, duration= 5)
    
    print("Sr: ...")
    try:
        you= sr_ear.recognize_google(audio)
    except:
        you="..."
    #Communication
    if you=="...":
        continue
    elif you=="hello brother":
        with Sr.Microphone() as mic:
            print("Sr:Hello Quang, I'm Listening...")
            robot_mouth = pyttsx3.init()
            robot_mouth.say("Hello Quang,I'm Listening")
            robot_mouth.runAndWait()
            audio= sr_ear.record(mic, duration= 5)
        print("Sr: ...")
        try:
            you= sr_ear.recognize_google(audio)
        except:
            you="..."
        if you=="...":
            continue
        if you=="how are you":
            robot_brain="i'm fine thanks"
            print("Sr: "+robot_brain)
            robot_mouth = pyttsx3.init()
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            continue
            
        elif you== "hi":
            robot_brain= "Hello Quang"
            print("Sr: "+robot_brain)
            robot_mouth = pyttsx3.init()
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            continue
        elif "today" in you:
            today = date.today()
            robot_brain = today.strftime("%B %d, %Y")
            print("Sr: "+robot_brain)
            robot_mouth = pyttsx3.init()
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            continue
        elif "time" in you:
            now = datetime.now()
            robot_brain = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Sr: "+robot_brain)
            robot_mouth = pyttsx3.init()
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            continue
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
            print("Sr: "+robot_brain)
            robot_mouth = pyttsx3.init()
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            continue
        #Open Facebook
        elif "ok ok" in you:
            url = f"https://www.facebook.com"
            webbrowser.get().open(url)
            robot_brain="ok,open Facebook"
            print("Sr: "+robot_brain)
            robot_mouth = pyttsx3.init()
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            continue
        #Music
        elif "music" in you:
            url=f"https://www.youtube.com/watch?v=qs1_yp-_V_w"
            webbrowser.get().open(url)
            robot_brain= "Ok, Have fun"
            print("Sr: "+robot_brain)
            robot_mouth = pyttsx3.init()
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            continue
        #Translate
        elif "ok" in you:
            
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
                    continue
                else:
                    url=f"https://translate.google.com/?hl=vi#view=home&op=translate&sl=en&tl=vi&text="+you_said
                    robot_brain= "ok, waitting me"
                    print("Sr: "+robot_brain)
                    robot_mouth = pyttsx3.init()
                    robot_mouth.say(robot_brain)
                    robot_mouth.runAndWait()
                    webbrowser.get().open(url)
        else:
            continue
    else:
        continue

   
        
    
