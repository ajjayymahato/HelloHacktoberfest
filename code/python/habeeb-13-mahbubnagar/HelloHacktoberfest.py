from gtts import gTTS
import os

text = "Hello, Hacktoberfest!"

tts = gTTS(text)

tts.save("output.mp3")

os.system("start output.mp3")