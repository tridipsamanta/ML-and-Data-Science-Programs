import pyttsx3

engine = pyttsx3.init()

text = input("Enter text to speak: ")

engine.say(text)
engine.runAndWait()

engine.setProperty('rate', 100)  # speech speed
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female (varies by OS)
