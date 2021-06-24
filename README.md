# Speech-Synthesis-My-Voice-Analysis

Module 1 :My Voice Analysis and Speech Synthesis using Python with Code Examples

SRH UNIVERSITY OF APPLIED SCIENCES
Professor: Mr.Alexander Iliev

*********************************************************************************************************************************************************************************************************************************
Introduction 
 
Voice Analysis :- Voice analysis is the experiment conducted on different sound origins for purposes that range from Speaker Identification,Emotional state also finds its way in medical field where it used to replicate sounds for people with damaged organ.

Speech Synthesis :- It is the process or program through which a user is able to translate any text to a given speech in various different languages. Even images could be first translated to text and then again to the desired language speech.

----------------------------Course Description------------------------------------------

To conduct experiment on sound data samples and collect information via voice anaylsis as well as to perform Speech synthesis on any given text. Python is the programming language used to code both topics.

System Requirements
Make sure you have the latest Python, CUDA and NVIDIA Drivers for proper installation and smooth execution

Pre-Requistes
 1. To install Anaconda Prompt
 2. To install gTTS using Anaconda
 3. To install Pyttsx using Anaconda
 4. Mac OS
 5. Microphone
 6. Install Pyzo IDE

************************************************************************************Installation**********************************************************************************************************************************

- Installing all required libraries: Type the following commands in the Terminal:
	- pip install my-voice-analysis
	- pip install gTTS
	- pip install pyttsx3
	- pip install pytesseract
	- pip install PIL
	- pip install praat-parselmouth
	- pip install matplotlib
	- pip install seaborn
	- pip install numpy

- Installing mpg321 in Mac OSX (To Play Audio)
	- Press Command+Space and type Terminal and press enter/return key.
	- Run in Terminal app:
	  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /	  dev/null and press enter/return key. 
	- Run:
	  brew install mpg321


- Possible Errors:
	- PIL unable to be installed. Instead enter 'pip install Pillow'
	- pytesseract unable to be installed. Instead enter 'brew install tesseract'	

**************************************************************************************************************Order of Execution***************************************************************************************************

Execute the following files in the order displayed below. Make sure all libraries and pre-requisites mentioned above have been met:

1. gTTS Test.py
	- Program to display working of gTTS with simple text to speech.

2. Text to Speech Hindi.py
	- Program to display working of gTTS with simple text to Hindi speech.

3. Text to Speech Hindi (Slow).py
	- Program to display working of gTTS and variation of speed.

4. Text to Speech Hindi 'en'.py
	- Program to display working of gTTS and speech synthesis with different language.

5. Text to Speech Hindi 'de'.py
	- Program to display working of gTTS and speech synthesis with different language.

6.1 Image to Text.py
	- Requires TechP.png to be in directory.
	- Program to convert text in TechP.png and save it to SRHTest.txt
	
6.2 Text to Speech.py
	- Requires SRHTest.txt generated from 6.1 Image to Text.py to be in directory.
	- Program to convert text from SRHTest.txt to audio speech.

7. Pyttsx Test.py
	- Program to display Adjusting of Rate, Volume and Sound using pyttsx.

8. Amplitude Analysis.py
	- Requires WilhelmScream.wav to be in directory.
	- Program to generate Time v Amplitude plot of WilhelmScream.wav audio file.

9. Frequency & Intensity Analysis.py
	- Requires WilhelmScream.wav to be in directory.
	- Program to generate Time v Frequency & Intensity plot of WilhelmScream.wav audio file.

10. My Voice Analysis.py 
	- Requires all files in folder 'My Voice Analysis Pre-requisites' to be copied into directory of py file.
	- Program to carry out analysis of audio sample of 44 kHz frequency and 16 bit resolution, including gender, number of syllables, mood of speech.
	- ERROR : When we execute the code, it is not locating the file and giving the error couldnÕt locate the file or audio is not clear even though myspsolution.praat and .wav are in same folder.

 ---------------------------------------Acknowledgements---------------------------------------

DeJong N.H, and Ton Wempe [2009]; “Praat script to detect syllable nuclei and measure speech rate automatically”; Behavior Research Methods, 41(2).385-390.
Paul Boersma and David Weenink; http://www.fon.hum.uva.nl/praat/
Gussenhoven C. [2002]; “ Intonation and Interpretation: Phonetics and Phonology”; Centre for Language Studies, Univerity of Nijmegen, The Netherlands.
Witt S.M and Young S.J [2000]; “Phone-level pronunciation scoring and assessment or interactive language learning”; Speech Communication, 30 (2000) 95-108.
Jadoul, Y., Thompson, B., & de Boer, B. (2018). Introducing Parselmouth: A Python interface to Praat. Journal of Phonetics, 71, 1-15. https://doi.org/10.1016/j.wocn.2018.07.001 (https://parselmouth.readthedocs.io/en/latest/)
https://parselmouth.readthedocs.io/en/docs/examples.html
https://github.com/Shahabks/my-voice-analysis
https://www.geeksforgeeks.org/convert-text-speech-python/
https://www.geeksforgeeks.org/python-text-to-speech-pyttsx-module/
https://www.geeksforgeeks.org/python-convert-image-to-text-and-then-to-speech/
https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/
https://gtts.readthedocs.io/en/latest/changelog.html#id1
https://pyttsx3.readthedocs.io/en/latest/engine.html


        

'  
