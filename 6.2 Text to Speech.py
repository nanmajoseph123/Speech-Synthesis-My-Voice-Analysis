from gtts import gTTS
import os

# We open the txt file we saved earlier
fh = open("SRHTest.txt", "r")
myText = fh.read().replace("\n", " ")
# Language we want to use
language = 'en'
output = gTTS(text=myText, lang=language, slow=False)
output.save("Part2.mp3")
fh.close()

# Play the converted file
os.system("mpg321 Part2.mp3")