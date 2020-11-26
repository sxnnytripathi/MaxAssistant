# INSTALLED PACKAGES :
"""
pip install pyttsx3
pip install speechRecognition
pip install pyaudio  {pip install pipwin,  pipwin install pyaudio}
pip install wikipedia
pip install pil {pip install pipwin,  pipwin install pil}
pip install pygame
"""

# MODULES :
import datetime
import os
import random
import smtplib
import webbrowser
from tkinter import *
import pyttsx3
import speech_recognition as sr
import wikipedia
from PIL import ImageTk, Image

# Name of Max's Boss
BOSS = "Sunny Tripathi"

# Voice of Max
enigne = pyttsx3.init('sapi5')
voices = enigne.getProperty('voices')
enigne.setProperty('voice', voices[0].id)  # Remove 0 and write 1 to get Female Voice

# Background Music of Max's App
'''
b_music = 'maxbgm'                                                                 
pygame.mixer.init()
pygame.mixer.music.load("C:\\Music\\Path\\Here\\maxbgm.mp3") # Enter your Audio Path Here
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)
'''


# This is how Max speaks
def speak(text):
    enigne.say(text)
    enigne.runAndWait()


# Max will wish GOOD MORNING, GOOD NIGHT, GOOD AFTERNOON according to the Time of Device
def wishME():
    hour = datetime.datetime.now().hour
    if 12 <= hour < 16:
        speak("Good Afternoon Sir")
    elif 16 <= hour < 23:
        speak("Good Evening Sir")
    else:
        speak("Good Morning Sir")


# It takes microphone input from the user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    # noinspection PyBroadException
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None\n"
    return query


# Cretadeils in this will be used to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')  # Write your email and password here
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


# Max Talking and Work
def clicked():
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = takeCommand()
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    # Talking with Max

    elif 'hello max' in query:
        speak("Hello sir")

    elif 'hey' in query:
        speak("Hi")

    elif 'hi' in query:
        speak("hey")

    elif 'hello' in query:
        speak("oh hello there")

    elif 'hola' in query:
        speak("heya")

    elif 'can you do' in query:
        speak("I can do anything you want me to do")

    elif 'good evening' in query:
        speak("Good Evening Sir")

    elif 'good morning' in query:
        speak("Good Morning Sir")

    elif 'good afternoon' in query:
        speak("Good Afternoon Sir")

    elif 'you can do' in query:
        speak("I can do anything you want me to do")

    elif 'your owner' in query:
        speak("My owner mister" + BOSS)

    elif 'who are you' in query:
        speak("I am Max")

    elif 'your name' in query:
        speak("My name is Max.")

    elif 'your age' in query:
        speak("I don't know,but the thing is, i will never die")

    elif 'something about yourself' in query:
        speak("I am Max, I am personal assistant of mister" + BOSS)
        speak("I was made to work like jarvis")
        speak("But I an way better than him")

    elif 'something about you' in query:
        speak("I am Max, I am personal assistant of mister" + BOSS)
        speak("I was made to work like jarvis")
        speak("But I an way better than him")

    elif 'tell us something about you' in query:
        speak("I am Max. I am personal assistant of mister " + BOSS)
        speak("I was made to work like jarvis")
        speak("But I an way better than him")

    elif 'who is your owner' in query:
        speak("My owner is mister" + BOSS)

    elif 'your boss' in query:
        speak("My boss is mister" + BOSS)

    elif 'ok' in query:
        speak("Yes sir")

    elif 'how are you' in query:
        stMsgs = ['I am fine!', 'Nice!', 'I am nice and full of energy', 'I am fine, what about you']
        speak(random.choice(stMsgs))

    elif "what\'s up" in query or 'whats up' in query:
        sttMsgs = ['Nothing much', 'Just doing nothing']
        speak(random.choice(sttMsgs))

    elif 'i am fine' in query:
        speak("good to hear that")

    # Funtions Max will Perform

    elif 'open website' in query:
        try:
            speak("Which website do you want me to open")
            content = takeCommand()
            webbrowser.open('www.' + content + '.com')
        except Exception as e:
            print(e)
            speak("Sorry Sir. I am not able to open that")

    elif 'open gmail' in query:
        webbrowser.open('www.gmail.com')

    elif 'open my gmail' in query:
        webbrowser.open('www.gmail.com')

    elif 'open amazom.com' in query:
        webbrowser.open("amazon.in")

    elif 'open amazom.in' in query:
        webbrowser.open("amazon.in")

    elif 'open amazom' in query:
        webbrowser.open("amazon.in")

    elif 'open wikipedia' in query:
        webbrowser.open("wikipedia.com")

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

        '''
        try:
            speak("What should I Search?")
            content = takeCommand()
            webbrowser.open('https://www.youtube.com/results?search_query=' + content)
        except Exception as e:
            print(e)
            speak("Sorry Sir. I am not able to search that")
        '''

    elif 'open google' in query:
        webbrowser.open("google.com")

        '''
        try:
            speak("What should I Search?")
            content = takeCommand()
            webbrowser.open('https://www.google.com/search?ei=' + content)
        except Exception as e:
            print(e)
            speak("Sorry Sir. I am not able to search that")
        '''

    elif 'open my instagram' in query:
        webbrowser.open("instagram.com")

    elif 'open instagram' in query:
        webbrowser.open("instagram.com")

    elif 'shutdown' in query:
        speak("Shutting Down Computer")
        speak("Bye Sir")
        os.system('shutdown -s')

    elif 'send email' in query:
        try:
            speak("Tell the email of the person")
            remailid = takeCommand()
            to = remailid
            speak("What should I write?")
            content = takeCommand()
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry Sir. I am not able to send this email")

    elif 'play music' in query:  # Add Music Folder and Name HERE
        '''
        music_folder = Your_music_folder_path
        music = [music1, music2, music3, music4, music5]
        random_music = music_folder + random.choice(music) + '.mp3'
        os.system(random_music)
        speak('Okay, here is your music! Enjoy!')
        '''
        speak("Playing Songs on YouTube")  # For Playing Music Onilne
        webbrowser.open("https://www.youtube.com/watch?v=-z7RaJ4GztU")

    elif 'play songs' in query:  # Add Music Folder and Name HERE
        '''
        music_folder = Your_music_folder_path
        music = [music1, music2, music3, music4, music5]
        random_music = music_folder + random.choice(music) + '.mp3'
        os.system(random_music)
        speak('Okay, here is your music! Enjoy!')
        '''
        speak("Playing Songs on YouTube")  # For Playing Songs Onilne
        webbrowser.open("https://www.youtube.com/watch?v=-z7RaJ4GztU")

    # Stoping Max from Listening

    elif 'thank you' in query:
        speak("Welcome Sir")
        exit()

    elif 'good night' in query:
        speak("Good Night Sir")
        exit()

    elif 'bye max' in query:
        speak("Bye Sir")
        exit()

    elif 'stop listening' in query:
        speak("Ok Sir")
        exit()

    elif 'abort' in query or 'stop' in query:
        speak('okay sir')
        exit()

    # The Last Thing Possible
    else:

        query = query

        try:
            webbrowser.open('https://www.google.com/search?ei=' + query)
            speak('Searching' + query + 'on google')
        except:
            speak("I cannot understand that")


# Here is how the app will lock like
class Widget:

    def __init__(self):
        root = Tk()
        root.title('MAX')
        root.config(background='White')
        root.geometry('1080x700')
        root.resizable(0, 0)  # Remove this to make the App Window Resizeable
        img = ImageTk.PhotoImage(Image.open(r"C:\\Image\\Path\\Here\\maxbody.jpg")) # Enter your Image Path Here
        panel = Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="no")
        Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepSkyBlue', fg='white',
               command=clicked).pack(fill='x', expand='no')
        Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white',
               command=root.destroy).pack(fill='x', expand='no')

        speak("Initializing Max...")  # On starting Max will say these things and then listen to me
        root.bind("<Return>", clicked)  # handle the enter key event of your keyboard
        root.mainloop()


# The Final Thing
if __name__ == '__main__':
    wishME()
    widget = Widget()
