from gtts import gTTS 
import os 
mytext = 'My Name is Sanchit'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 
os.system("welcome.mp3")
