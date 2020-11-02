import pyttsx3

robot_brain="Quang, you are very handsome. I love you"
robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()