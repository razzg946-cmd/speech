import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 170)     # speed
engine.setProperty("volume", 1.0)   # volume (0.0 to 1.0)

# Take input from user
text = input("Enter something to speak: ")

engine.say(text)
engine.runAndWait()
