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
if '6'<= datetime.now().strftime("%H") <='9':
    print("Good morning, my bro....!!")
    robot_mouth = pyttsx3.init()
    robot_mouth.say("Good morning, my bro!")
    robot_mouth.runAndWait()
elif '10'<= datetime.now().strftime("%H") <='17':
    print("Good afternoon, bro....!!")
    robot_mouth = pyttsx3.init()
    robot_mouth.say("Good afternoon, bro...")
    robot_mouth.runAndWait()
elif '18'<= datetime.now().strftime("%H") <= '22':
    print("Good evening, bro....!!")
    robot_mouth = pyttsx3.init()
    robot_mouth.say("Good evening, Bro")
    robot_mouth.runAndWait()
elif '23' <= datetime.now().strftime("%H") <= '24':
    print("It's a bit late, man, what do you need from me?....!!")
    robot_mouth = pyttsx3.init()
    robot_mouth.say("It's a bit late, man, what do you need from me?...")
    robot_mouth.runAndWait()
elif '1' <= datetime.now().strftime("%H") <= '5':
    print("Oh, I'm sleeping, man, what do you need from me?")
    robot_mouth = pyttsx3.init()
    robot_mouth.say("Oh, I'm sleeping, man, what do you need from me?")
    robot_mouth.runAndWait()

with Sr.Microphone() as mic:
    print("Sr:Hi bro, I'm Vietnam. I'm Listening...")
    robot_mouth = pyttsx3.init()
    robot_mouth.say("Hi bro, I'm Vietnam. I'm Listening...")
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
    elif you=="hello Vietnam":
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
            if '6'<= datetime.now().strftime("%H") <='9':
                print("Have a good morning, my bro....!!")
                robot_mouth = pyttsx3.init()
                robot_mouth.say("Have a good morning, my bro!")
                robot_mouth.runAndWait()
            elif '10'<= datetime.now().strftime("%H") <='17':
                print("Have a good day, bro....!!")
                robot_mouth = pyttsx3.init()
                robot_mouth.say("Have a good day, bro...")
                robot_mouth.runAndWait()
            elif '18'<= datetime.now().strftime("%H") <= '22':
                print("Have a good evening, bro....!!")
                robot_mouth = pyttsx3.init()
                robot_mouth.say("Have a good evening, Bro")
                robot_mouth.runAndWait()
            elif '23' <= datetime.now().strftime("%H") <= '24':
                print("Good night, bro....!!")
                robot_mouth = pyttsx3.init()
                robot_mouth.say("Good night, bro...")
                robot_mouth.runAndWait()
            elif '1' <= datetime.now().strftime("%H") <= '5':
                print("Take a break early to prepare for the new day, bro")
                robot_mouth = pyttsx3.init()
                robot_mouth.say("Take a break early to prepare for the new day, bro")
                robot_mouth.runAndWait()
            break
        #Open youtube
        elif "open Youtube" in you:
            url = f"https://www.youtube.com"
            webbrowser.get().open(url)
            robot_brain="ok,open youtube"
            print("Sr: "+robot_brain)
            robot_mouth = pyttsx3.init()
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            continue
        elif "shutdown" in you:
            robot_brain="Goodbye Quang, see you again"
            print("Sr: "+robot_brain)
            robot_mouth = pyttsx3.init()
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            os.system('shutdown -s')
        #Open Facebook
        elif "open Facebook" in you:
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
        elif "Google" in you:
            
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
        else:
            continue
    else:
        continue

   
        
    
