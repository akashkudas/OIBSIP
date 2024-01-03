import datetime
import os
import webbrowser
import speech_recognition as sr
import win32com.client
import  random
import openai
from config import apikey



def ai(prompt):
    openai.api_key = apikey
    text = f"opne ai responce for prompt: {prompt} \n ****************************\n\n"

    # Make an API request using openai.Completion.create
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    #todo: wap this inside of a try catch block
    #print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("openai"):
        os.mkdir("openai")
    # with open(f"openai/prompt- {random.randint(1, 234567676)}", "w") as f:
    with open(f"openai/{' '.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):
    speaker=win32com.client.Dispatch("SAPI.spvoice")
    speaker.speak(text)
def takecommand():
    r = sr.Recognizer()
    mic_index = 1  # Adjust this index based on your system
    with sr.Microphone(device_index=mic_index) as source:

    # Rest of your code
        #r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred . sorry from jarvis"



if __name__ == '__main__':
    print("pycham")
    say("Hello I am Jarvis AI")
    while True:
        print("Listening...")
        query = takecommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir..")
                webbrowser.open(site[1])
        if "open music" in query:
            musicpath= r"C:\Users\KIIT\Downloads\10song.mp3"
            os.startfile(musicpath)
        if "stop music" in query:
            print("Stopping music playback...")
            break
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"sir the time is {hour} bajjke {min} minutes")
        if "open anydesk" in query.lower():
            anydesk_path = r"C:\Users\KIIT\Desktop\AnyDesk.exe"
            os.system(f'"{anydesk_path}"')
        if "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        if "search for" in query.lower():
            search_query = query.lower().replace("search for", "")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")


