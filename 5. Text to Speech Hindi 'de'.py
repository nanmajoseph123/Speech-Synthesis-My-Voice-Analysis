from gtts import gTTS
import os

hindi = "नमस्कार, मैं इस पाठ में आपका स्वागत करता हूं। धन्यवाद"
obj = gTTS(text = hindi, slow = False, lang = 'de')
obj.save('hindide.mp3')

# Playing the converted file
os.system("mpg321 hindide.mp3")
