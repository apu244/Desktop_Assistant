import subprocess
import datetime
import os
import webbrowser
import pyttsx3
import openai
import speech_recognition as sr
from config import apikey
import random


# def ai(prompt):
#     openai.api_key = apikey
#     text = f"OpenAI respose for prompt: {prompt} \n *********\n\n"
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt="Write an email to my boss for resignation?",
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     print(response["choices"][0]["text"])
#     text += response["choices"][0]["text"]
#     if not os.path.exists("aifiles"):
#         os.mkdir("aifiles")
#
#     with open(f"aifiles/{prompt[0:30]}.txt", "w") as f:
#         f.write(text)
#
#
# def chat(task):
#     global chatStr
#     print(chatStr)
#     openai.api_key = apikey
#     chatStr += f"Apurba: {task}\n Jarvis: "
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=chatStr,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )
#     # todo: Wrap this inside of a  try catch block
#     say(response["choices"][0]["text"])
#     chatStr += f"{response['choices'][0]['text']}\n"
#     return response["choices"][0]["text"]



def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# while 1:
#     print("enter the word")
#     s = input()
#     speaker.Speak(s)

# def say(text):
#     os.system(f"say {text}")

def takeCommand():
    recognizer = sr.Recognizer()

    # Recognize speech using the microphone as the source
    with sr.Microphone() as source:
        recognizer.pause_threshold = 0.6
        audio = recognizer.listen(source)

    # Now, perform the speech recognition on the captured audio
    try:
        recognized_text = recognizer.recognize_google(audio)
        # print("Recognizing......")
        print("You said: " + recognized_text)
        query = "You said: " + recognized_text
    except sr.UnknownValueError:
        query = "Speech Recognition could not understand audio."
        print(" come up again")
        # say("comme up again")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        query = "No internet connection".format(e)
    return query


# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone as source:
#         r.pause_threshold =  1
#         audio = r.listen(source)
#         query = r.recognize_google(audio, language="en-in")
#         print(f"User said: {query}")
#         return query


def open_l(l_path):
    try:
        say("opening ")
        # , check=True
        # subprocess.Popen
        subprocess.Popen(["explorer", l_path])
    except subprocess.CalledProcessError:
        print(f"Error opening the location")
        say("sorry there was an Error in opening")


if __name__ == '__main__':
    print('PyCharm')
    say("hello i am your assistant, how may i help you")
    # print("listening....")
    print("Say something...")
    say("Say something...")
    while 1:
        task = takeCommand()
        say(task)
        sites = [["youtube", "www.youtube.com"], ["google", "https://www.google.com"],
                 ["facebook", "https://www.facebook.com"], ["linkedin", "https://www.linkedin.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in task.lower():
                say(f"opening {site[0]}")
                webbrowser.open(site[1])

        if "the time" in task:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(strfTime)

        elif "open download" in task:
            # folder_path = r"C:\Users\apurb\Downloads"
            # subprocess.run(["explorer", folder_path], check=True"])
            l_path = r"C:\Users\apurb\Downloads"
            open_l(l_path)

        elif "open VLC" in task:
            l_path = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
            open_l(l_path)
        # elif "using chatGPT".lower() in task.lower():
        #     ai(prompt=task)
        # else:
        #     chat(task)
