import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')  # sapi5 is the api for voice recognition
voices = engine.getProperty('voices')
# print(voices) #this willshow the audio present in your computer

engine.setProperty('voices', voices[0].id)
print(voices[0].id)  # give us which voice is being used


def speak(audio):
    s = engine.say(audio)
    engine.runAndWait()
    print(s)


def wishme():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        speak("Good Morning Sir")
    elif time > 12 and time < 17:
        speak("Good afternoon Sir")
    elif time > 17 and time < 0:
        speak("Good evening Sir")

    # speak("Hello,I am broda. Your Ultimate Bro")
    # speak("How may I help you today sir")


def take():
    # takes microphone user input and convert it to the string

    r = sr.Recognizer()
    with sr.Microphone(device_index= 0) as source:
        print("Listening.....")

        r.pause_threshold = 1
        # r.energy_threshold = 280
        audio = r.listen(source)

    try:
        print (audio)
        print("Please Wait\nRecognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    # we use try when we think do this if error occurs
    except Exception as e:
        # print(e)
        print("Please say that again.....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ssrijanjeet9@gmail.com', 'Jeet@2001')
    server.sendmail('ssrijanjeet9@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()

    while True:
        query = take().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia......")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentence=3)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open instagram" in query:
            webbrowser.open("instagram.com")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = take()
                to = "sndhwn@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")
