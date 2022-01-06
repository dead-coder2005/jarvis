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

# debug command
#debug = "what is the temperature in Hudson"
debug = ""

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    if debug != "":
        return debug
    else:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
        return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        response = 'playing ' + song + 'sir'
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M')
        response = 'The current time is ' + time + 'sir'
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        response = info
    elif 'hello' in command:
        response = "hello, sir"
    elif 'joke' in command:
        response = pyjokes.get_joke()
    elif 'what is the temperature in' in command:
        weather_place = command.replace('what is the temperature in ', '')
        response = get_weather(weather_place)
        # response = get_weather(weather) #@TODO fix this
    elif 'goodbye' in command:
        response = "goodbye"
        talk(response)
        exit()
    else:
        response = 'Can you repeat that sir?'
    print(response)
    talk(response)


if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            run_jarvis()
        else:
            response = 'Can you repeat that sir?'
        print(response)
        talk(response)