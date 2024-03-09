#pip install SpeechRecognition
#pip install pyaudio
#pip install pyttsx3
#pip install wikipedia
#pip install chatterbot
#or
#pip install https://github.com/RaSan147/ChatterBot_update/archive/refs/heads/master.zip
#python -m spacy download en_core_web_sm
#pip3 install pyyaml
#pip install --upgrade PyYaml

#pip install chatterbot_corpus
#pip instal pygame
#pip install playsound
#pip install selenium==4.9.0
#dowload https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/
#have git installed
#git clone https://github.com/Michelangelo27/chatgpt_selenium_automation.git
#muta apoi folderul handler din chatgpt_selenium_automation
#rescrie chatgpt_selenium_automation
#pip install seleniumbase
#follow these steps: https://github.com/Simatwa/python-tgpt
#pip install python-tgpt
#pip install g4f==0.1.9.3

import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import tkinter
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
from WebChatGPT import ChatGPT
import pytgpt.phind as phind


bot = phind.PHIND()


for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f'{index}, {name}')

mic = int(input("Choose a microphone: "))
wake_word = "Jarvis"
path_to_cookies = "D:\chat.openai.com.cookies.json" #path for the cookies
engine = pyttsx3.init()
engine.setProperty('voice', 3)

chatbotv2 = ChatBot('jarvis2vs')

# Uncomment the next lines for training the bot

# Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(chatbotv2)

# Train the chatbot based on the english corpus
# trainer.train(
#     "chatterbot.corpus.english.greetings",
#     "chatterbot.corpus.english.conversations"
# )
# Get a response to an input statement
# print(chatbotv2.get_response("Hello?"))



def speak(text):
    engine.say(text)
    engine.runAndWait()

def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}.")

def change_voice():
    for voice in voices:
        print(voice, voice.id)
        engine.setProperty('voice', voice.id)
        speak("Do you like this voice?")
        with sr.Microphone(device_index=mic) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            command = r.recognize_google(audio)
            if "yes" in command:
                break
    speak("I hope you like my new voice!")


# Set up speech recognition
r = sr.Recognizer()

voices = engine.getProperty('voices')



while True:
    with sr.Microphone(device_index=mic) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        if wake_word in r.recognize_google(audio):
            speak("Yes sir?")
            ok = True
            while ok is True:
            # Listen for command
                with sr.Microphone(device_index=mic) as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)

                try:
                    # Convert speech to text
                    command = r.recognize_google(audio)
                    print("H: " + command)
                    if "quit" in command and "Jarvis" in command or "sleep" in command and "Jarvis" in command:
                        ok = False
                        speak("Going into sleep mode")

                    elif "open" in command:
                        if "website" in command:
                            url = command.split()[-1]
                            speak("opening website " + url)

                    elif "time" in command:
                        tell_time()
                    elif "change" in command and "voice" in command:
                        speak("Are you sure you want to change my voice?")
                        with sr.Microphone(device_index=mic) as source:
                            r.adjust_for_ambient_noise(source)
                            audio = r.listen(source)
                            command = r.recognize_google(audio)
                            if "yes" in command:
                                change_voice()
                    else:
                        """
                        
                        Here, if no command is recognized, the chatbot should come in
                    
                        
                        """
                        response = bot.chat(command)
                        print("R: " + response)
                        speak(response)
                        #Send command to the chatbot
                        # response = chatbotv2.get_response(command)
                        # chatgpt.send_prompt_to_chatgpt(command)
                        # response = chatgpt.return_last_response()
                        #
                        # print(response)
                        # speak(response)


                except sr.UnknownValueError:
                    speak("I'm sorry, I didn't understand that.")
                except sr.RequestError as e:
                    speak("Sorry, I couldn't reach the Google servers. Check your internet connection.")
    except :
        print('.')
