import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import subprocess
import wolframalpha
import cv2
import json
import requests
import pyaudio

# Setting speech recognition engine
engine=pyttsx3.init('espeak')
voices=engine.getProperty('voices')
engine.setProperty('voices','voices[0].id')
# engine.setProperty('voice', 'english_rp+f4')

# To pass commands that need to be spoken by Hikan
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Pass and speak name of the user
name = input("Enter your name: ")
toSpeak = "Welcome, " + name
speak(toSpeak)


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

# Calling method to wish the user
wishMe()

# Function to take voice input from user
def voiceInput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


# Starting to take commands from user
if __name__=='__main__':

    # Loop to repeat till user exits
    while True:
        speak("Tell me how can I help you now?")
        statement: str = voiceInput().lower()
        if statement==0:
            continue

        # If user wants to exit the software
        if "good bye" in statement or "goodbye" in statement or "ok bye" in statement or "stop" in statement or "quit" in statement:
            speak('Good bye from Hikan, see you later')
            print('Good bye from Hikan, see you later')
            break

        # To search content on wikipedia
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            print(statement)
            try:
                results = wikipedia.summary(statement, sentences=3)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)

                j = 0
                for i, topic in enumerate(e.options):
                    if statement.lower() in topic.lower():
                        print("\n topic = ")
                        print(topic)
                        j = i
                        break

                print("\nOptions = ")
                print(e.options[j])
                results = wikipedia.summary(e.options[j], sentences=3)

        # To open youtube
        elif 'open youtube' in statement:
            print("youtube")
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        # To open google
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            time.sleep(5)

        # To open gmail
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        # To show current time to user
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is {strTime}")
            speak(f"the time is {strTime}")

        # To show news headlines to user from Times-of-India
        elif 'news' in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines/")
            speak("Here are some headlines from the Times of India Happy reading")
            print("Displayed output from Times of India")
            time.sleep(5)

        # To search any content from browser
        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab()
            speak(f"Searching for {statement}")
            print(f"Searching for {statement}")
            time.sleep(5)

        # To ask computational and geographical questions
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = voiceInput()
            app_id = "WV4JHL-28PWQ4X37Y"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        # To Shutdown Computer
        elif 'shutdown' in statement:
            speak("Your system is on its way to shut down")
            cmdCommand = "shutdown -h now"
            process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)

        # To specify the developers
        elif "who made you" in statement or "who created you" in statement or "who developed you" in statement:
            speak("I am developed by Anshuman Mishra, Animesh Deka, Aakash Nath and Himanshu Kumar Gupta")
            print("I am developed by Anshuman Mishra, Animesh Deka, Aakash Nath and Himanshu Kumar Gupta")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Hikan your personal voice assistant. I am developed to perform minor tasks like'
                  'opening youtube,google, gmail,display time,take a photo,search wikipedia,predict weather'
                  'In different cities, get top headline news from times of india and I can further answer to computational or geographical questions!')

        # To capture photos from camera
        elif 'photo' or 'picture' in statement:
            camera = cv2.VideoCapture(0)
            ret, frame = camera.read()
            cv2.imwrite("updated.png", frame)
            print("Image is recorded")
            camera.release()
            cv2.destroyAllWindows()
            del(camera)

        else:
            print("\nDidn't get it! Please say it again")