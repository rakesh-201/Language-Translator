import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from datetime import datetime
from googletrans import LANGUAGES, Translator
import os

# Code For Speech Output
def speak(text, lang='en'):
    tts = gTTS(text, lang=lang)
    filename=f'voice.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# Code for Speech Input
def takeCommand(lang):
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 1500
        speak('Speak the sentence')
        audio = r.listen(source)
        speak('done')
    try:
        query = r.recognize_google(audio, language = lang)
        print(f"User said: {query}\n")
        speak(f"User said:  {query}\n")
        return query
    except Exception as e:
        global i
        if i<3:
            speak("Say that again please......")
            i += 1
            return takeCommand(lang)
        else:
            speak('There is some problem in the voice connection, please check your internet connection.')
            i=0
            return 0

# Program Starts From Here
i = 0

speak('Hello Sir. You may translate any of your sentences into almost any language by following three basic steps, which are, Selecting your text language, Speaking the text to be translated, Selecting the language of the output text. ')

speak('This is the list of languages with the code words. Please enter the code word of the language you are using.')
for lang in LANGUAGES:
    print(f"{lang} - {LANGUAGES[lang]}")

lang = input('Enter the language code: ')

text = takeCommand(lang)

if text:
    speak('Please enter the output language')
    for lang in LANGUAGES:
        print(f"{lang} - {LANGUAGES[lang]}")
    outLang = input('Enter the Output Language code: ')

    trans = Translator()
    trans = trans.translate(text, src=lang, dest=outLang)
    
    speak(trans.text)
    print(trans.text)