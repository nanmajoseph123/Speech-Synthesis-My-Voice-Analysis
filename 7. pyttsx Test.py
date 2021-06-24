import pyttsx3
engine = pyttsx3.init()             #Object Creation

#Rate
rate = engine.getProperty('rate')   #Getting details of current speaking rate
engine.setProperty('rate', 300)     #Setting up new voice rate

#Volume
volume = engine.getProperty('volume')   #Getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',0.5)        #Setting up volume level  between 0 and 1

#Voice
voices = engine.getProperty('voices')       #Getting details of current voice
engine.setProperty('voice', voices[1].id)   #Changing index, changes voices. 0 M, 1 F

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.say('My current speaking volume is ' + str(volume))
engine.runAndWait()
engine.stop()

