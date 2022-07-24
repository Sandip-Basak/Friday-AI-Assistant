import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia
import sys
import os
import random
import pyautogui
import cv2
import numpy as np
from datetime import date
import speedtest
import pywhatkit

engine = pyttsx3.init()
path = "file path"
user = ""
is_screenshot = False
is_screen_record = False
screenshot_path = ""
screen_recording_path = ""
st = speedtest.Speedtest()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning Sir')
    elif 12 <= hour < 18:
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')
    speak('How may I help you ?')


def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 0.5
        r.energy_threshold = 1000
        audio = r.listen(source)
    try:
        print("Recognising ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        return "none"
    return query


def send_whatsapp_message(name):
    contact = {
        " dad": "+919433403243",
        " captain america": "+917980844715",
        " iron man": "+919073559190",
        " brothers": "+919903791038",
        " computer sir": "+919038963728",
        " maths sir": "+919163790031",
        " surya": "+919123685803"
    }
    speak("What do you wanna text ?")
    text = get_command()
    speak("Loading Whatsapp ! Please wait")
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    try:
        pywhatkit.sendwhatmsg(contact.get(name, "No Contact found"), text, hour, minute + 1)
        speak("Message sent successfully ! What more can I do for you")
    except:
        speak("Error Occurred ! Please try again")


def screen_recorder():
    speak('Sir, what do you wanna call it ?')
    video_name = f"C:\\Users\\Sandip Basak\\Videos\\Friday Screen Recording\\{get_command()}.avi"
    resolution = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    fps = 20
    speak("Sir press Q to stop recording")

    # Creating the video file
    out = cv2.VideoWriter(video_name, codec, fps, resolution)

    # Creating a window and resizing it
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 480, 270)

    while True:
        img = pyautogui.screenshot()  # Capturing each frame
        frame = np.array(img)  # Appending the frame in an numpy array
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converting BGR to RGB color format
        out.write(frame)  # Writing the frame in the file
        cv2.imshow('Live', frame)  # Showing the live recording
        if cv2.waitKey(1) == ord('q'):
            break

    # Saving the video
    out.release()

    # Destroying the live screen
    cv2.destroyAllWindows()

    return video_name


speak('Hello My name is Friday')
speak('Please provide the password')
trial = 0
password = 'i am iron man'
while True:
    user_password = get_command().lower()
    if user_password == password:
        break
    else:
        if trial < 2:
            speak('Wrong Password! Please try again')
    trial += 1
    if trial == 3:
        speak('Sorry Wrong password ! Automatic system shutdown')
        sys.exit()

wish_me()
while True:
    user = get_command().lower()
    if 'wikipedia' in user:
        speak('Searching Wikipedia ...')
        user = user.replace('wikipedia', '')
        try:
            results = wikipedia.summary(user, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        except Exception as es:
            speak("Sorry, Try saying something specific !!!")
    elif 'search' in user:
        user = user.replace('search', '')
        try:
            pywhatkit.search(user)
            speak("Searching")
        except:
            speak("Error occurred ! Please try again")
    elif 'open youtube' in user:
        webbrowser.open('youtube.com')
        speak("You may enjoy watching videos on youtube")
    elif 'youtube' in user:
        speak('Searching Youtube')
        user = user.replace('youtube', '')
        try:
            pywhatkit.playonyt(user)
            speak('Playing Video')
        except:
            speak('Network Error Occurred ! Please try again')
    elif 'amazon' in user:
        webbrowser.open('amazon.com')
        speak("You may enjoy your Online shopping")
    elif 'flipkart' in user:
        webbrowser.open('flipkart.com')
        speak("You may enjoy your Online shopping")
    elif 'speed test' in user:
        speak("Executing an Internet Speed Test ! Please Wait")
        download = st.download()
        upload = st.upload()
        speak(f"The Download Speed is {download / 1024 / 1024: .2f} m b p s")
        speak(f"The Upload Speed is {upload / 1024 / 1024: .2f} m b p s")
    elif 'google' in user:
        webbrowser.open('google.com')
        speak("You may enjoy your web browsing")
    elif 'facebook' in user:
        webbrowser.open('facebook.com')
    elif 'shortcut' in user:
        path = "A:\\Shotcut Installation\\Shotcut\\shotcut.exe"
        os.startfile(path)
    elif 'steam' in user:
        path = "A:\\Game\\Steam.exe"
        os.startfile(path)
    elif 'counter strike' in user:
        path = "steam://rungameid/730"
        os.startfile(path)
        sys.exit()
    elif 'chrome' in user:
        path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(path)
    elif 'ms word' in user:
        path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(path)
    elif 'excel' in user:
        path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(path)
    elif 'power point' in user:
        path = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(path)
    elif 'trick shots' in user:
        path = "C:\\Users\\Sandip Basak\\Videos\\Trick Shots"
        videos = os.listdir(path)
        os.startfile(os.path.join(path, random.choice(videos)))
    elif 'music' in user:
        path = "C:\\Users\\Sandip Basak\\Music\\My Music"
        music = os.listdir(path)
        os.startfile(os.path.join(path, random.choice(music)))
    elif 'photos' in user:
        path = "C:\\Users\\Sandip Basak\\Pictures\\Post Processing"
        photos = os.listdir(path)
        os.startfile(os.path.join(path, random.choice(photos)))
    elif 'magic' in user:
        path = "C:\\Users\\Sandip Basak\\Videos\\Magic Tutorial"
        magic = os.listdir(path)
        os.startfile(os.path.join(path, random.choice(magic)))
    elif 'comedy videos' in user:
        path = "C:\\Users\\Sandip Basak\\Videos\\Comedy"
        videos = os.listdir(path)
        os.startfile(os.path.join(path, random.choice(videos)))
    elif 'android studio' in user:
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio\\Android Studio.lnk"
        os.startfile(path)
    elif 'python' in user:
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition " \
               "2021.2.2.lnk "
        os.startfile(path)
    elif 'c programming' in user:
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Bloodshed Dev-C++\\Dev-C++.lnk"
        os.startfile(path)
    elif 'my sql' in user:
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\XAMPP\\XAMPP Control Panel.lnk"
        os.startfile(path)
    elif 'whatsapp' in user:
        send_whatsapp_message(user.replace('whatsapp', ''))
    elif 'take screenshot' in user or 'take a screenshot' in user:
        path = "C:\\Users\\Sandip Basak\\Pictures\\friday Screenshot"
        speak("what do you wanna name the screenshot ?")
        screenshot_name = get_command().lower()
        my_screenshot = pyautogui.screenshot()
        my_screenshot.save(path + f"\\{screenshot_name}.png")
        is_screenshot = True
        screenshot_path = path + f"\\{screenshot_name}.png"
        speak("Screenshot saved successfully")
        speak("What more can I do for you ?")
    elif 'show me the screenshot' in user or 'show screenshot' in user:
        if is_screenshot:
            os.startfile(screenshot_path)
        else:
            speak("No screenshot was taken")
    elif 'good morning friday' in user or 'good afternoon friday' in user or 'good evening friday' in user:
        wish_me()
    elif 'who are you' in user:
        speak('My name is Friday, an artificial intelligence developed by Sandip')
    elif 'time' in user:
        h = int(datetime.datetime.now().hour)
        m = int(datetime.datetime.now().minute)
        if h < 12:
            speak(f'It is {h} {m} am')
        else:
            if h == 12:
                speak(f'It is {h} {m} pm')
            else:
                speak(f'It is {h - 12} {m} pm')
    elif 'date' in user:
        today = date.today()
        speak(today)
    elif 'volume up' in user:
        pyautogui.press("volumeup")
    elif 'volume down' in user:
        pyautogui.press("volumedown")
    elif 'volume of' in user or 'volume on' in user:
        pyautogui.press("volumemute")
    elif 'start screen recording' in user or 'record screen' in user:
        screen_recording_path = screen_recorder()
        is_screen_record = True
        speak("Video saved successfully")
        speak("What more can I do for you ?")
    elif 'play screen recording' in user or 'show me the screen recording' in user or 'show screen recording' in user:
        if is_screen_record:
            os.startfile(screen_recording_path)
        else:
            speak('No video was not recorded')
    elif 'thank you' in user:
        speak('Welcome sir, it was my pleasure to help you')
        speak('what more can i do for you ?')
    elif 'offline' in user or 'turn off' in user:
        speak("Thank you Sir, for giving your time.")
        speak("Turning off the system")
        sys.exit()
