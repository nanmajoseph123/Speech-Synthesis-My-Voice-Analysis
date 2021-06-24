from gtts import gTTS
import os

hindi = "नमस्कार, मैं इस पाठ में आपका स्वागत करता हूं। धन्यवाद"
obj = gTTS(text = hindi, slow = False, lang = 'en')
obj.save('hindi?.mp3')

# Playing the converted file
os.system("mpg321 hindi?.mp3")
