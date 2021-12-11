import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from Py_Weather import get_weather

listener = sr.Recognizer()
engine = pyttsx3.init()

engine.say('Hello sir welcome back')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song + 'sir')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M')
        print(time)
        talk('The current time is ' + time + 'sir')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'hello' in command:
        print('hello sir')
        talk('hello sir')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'what is the temperature in' in command:
        weather_place = command.replace('what is the temperature in', '')
        weather = get_weather(weather_place)
        talk(get_weather(weather))
    else:
        talk('Can you repeat that sir?')


while True:
    run_jarvis()