# pip install SpeechRecognition
# pip install pyaudio
# pip install pyttsx3
# pip install wikipedia
# pip install chatterbot
# or
# pip install https://github.com/RaSan147/ChatterBot_update/archive/refs/heads/master.zip
# python -m spacy download en_core_web_sm
# pip3 install pyyaml
# pip install --upgrade PyYaml

# pip install chatterbot_corpus
# pip instal pygame
# pip install playsound
# pip install selenium==4.9.0
# dowload https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/
# have git installed
# git clone https://github.com/Michelangelo27/chatgpt_selenium_automation.git
# muta apoi folderul handler din chatgpt_selenium_automation
# rescrie chatgpt_selenium_automation
# pip install seleniumbase
# follow these steps: https://github.com/Simatwa/python-tgpt
# pip install python-tgpt
# pip install g4f==0.1.9.3
# install https://pimylifeup.com/raspberry-pi-vlc/
# pip3 install youtube-search-python
# pip install yt-dlp
from youtubesearchpython import VideosSearch
import subprocess
import os
from playsound import playsound
import os
import speech_recognition as sr
import pyttsx3
import datetime
import pytgpt.phind as phind


# elevenlabs = "fea71e702f8f3bf55620937499b5730c"
# def text_to_speech(text, voice_id, api_key):
#     url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
#     headers = {
#         "xi-api-key": "e6544386341418fa400345857ec819cc",
#         "Content-Type": "application/json",
#         "accept": "audio/mpeg"
#     }
#     data = {
#         "text": text,
#         "voice_settings": {
#             "stability": 0,
#             "similarity_boost": 0
#         }
#     }
#     response = requests.post(url, headers=headers, json=data)
#     with tempfile.NamedTemporaryFile(delete=False) as f:
#         f.write(response.content)
#         filepath = f.name
#     return filepath

def delete_temp_file(filepath):
    os.remove(filepath)


bot = phind.PHIND()
basic_commands_file = open("commands.txt", "r")
basic_commands = basic_commands_file.read()
bot.chat(basic_commands)
# create a set of commands for the jarvis
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f'{index}, {name}')

mic = int(input("Choose a microphone: "))

wake_word = "Jarvis"
engine = pyttsx3.init()
engine.setProperty('voice', 3)

os.add_dll_directory(os.getcwd())


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


def downloadaudio(link):
    folder_path = os.getcwd()
    files = os.listdir(folder_path)

    for file in files:
        if "output.mp3" in file or "opus" in file:
            try:
                os.remove(file)
            except:
                print('all is good')
    command1 = "yt-dlp -x " + link + " --restrict-filenames"

    process = subprocess.Popen(command1, shell=True)
    process.wait()
    folder_path = os.getcwd()
    files = os.listdir(folder_path)

    for file in files:
        if ".opus" in file:
            try:
                command2 = "ffmpeg -i " + file + " output.mp3"
                os.system(command2)
                os.remove(file)
            except:
                print('all is good')



def playsong():
    playsound('output.mp3')
    os.remove('output.mp3')


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
                        # Send command to the chatbot
                        # response = chatbotv2.get_response(command)
                        # chatgpt.send_prompt_to_chatgpt(command)
                        # response = chatgpt.return_last_response()
                        #
                        # print(response)
                        # speak(response)
                        # [{'type': 'video', 'id': 'iyLdoQGBchQ', 'title': 'Kaoma - Lambada (Official Video) 1989 HD', 'publishedTime': '9 years ago', 'duration': '3:27', 'viewCount': {'text': '584,132,476 views', 'short': '584M views'}, 'thumbnails': [{'url': 'https://i.ytimg.com/vi/iyLdoQGBchQ/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAXupRMu-PJDbvhkK2P4-aBdYwAew', 'width': 480, 'height': 270}], 'richThumbnail': {'url': 'https://i.ytimg.com/an_webp/iyLdoQGBchQ/mqdefault_6s.webp?du=3000&sqp=CKjE2q8G&rs=AOn4CLApOqMPehQD-IZoUX5FqYisa25bcQ', 'width': 320, 'height': 180}, 'descriptionSnippet': [{'text': 'Lyrics : Chorando se foi quem um dia só me fez chorar Chorando se foi quem um dia só me fez chorar Chorando estará ao\xa0...'}], 'channel': {'name': 'Club Music 80', 'id': 'UCvSLvgYtFw_9Ubdjk74OqbA', 'thumbnails': [{'url': 'https://yt3.ggpht.com/95zgG2eEtF9lDw_5z4DMeMSf7W0Sh7TJMQqVW5egukyjUe_qLxW8MU1TTZej7yXIoiCdekGM=s68-c-k-c0x00ffffff-no-rj', 'width': 68, 'height': 68}], 'link': 'https://www.youtube.com/channel/UCvSLvgYtFw_9Ubdjk74OqbA'}, 'accessibility': {'title': 'Kaoma - Lambada (Official Video) 1989 HD by Club Music 80 584,132,476 views 9 years ago 3 minutes, 27 seconds', 'duration': '3 minutes, 27 seconds'}, 'link': 'https://www.youtube.com/watch?v=iyLdoQGBchQ', 'shelfTitle': None}]

                        if "< Play" in response:
                            first_quote_index = response.find('"')
                            second_quote_index = response.find('"', first_quote_index + 1)
                            melody_title = response[first_quote_index + 1:second_quote_index]
                            print("R: Playing : " + melody_title)
                            speak("Playing : " + melody_title)
                            videosSearch = VideosSearch(melody_title, limit=1)
                            melody_link = videosSearch.result()['result'][0]['link']
                            # melody_link = videosSearch.result()['link']
                            print(melody_link)
                            downloadaudio(melody_link)
                            playsong()


                except sr.UnknownValueError:
                    speak("I'm sorry, I didn't understand that.")
                except sr.RequestError as e:
                    speak("Sorry, I couldn't reach the Google servers. Check your internet connection.")
    except:
        print('.')
