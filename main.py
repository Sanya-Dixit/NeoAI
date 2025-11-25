import speech_recognition as sr
import os
import webbrowser
from openai import OpenAI
from config import apikey
import datetime
import random
import pyttsx3


chatStr = ""
# Initialize OpenAI client
client = OpenAI(api_key=apikey)

# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"Sanya: {query}\n Neo: "
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Neo, a helpful AI assistant."},
                {"role": "user", "content": chatStr}
            ],
            temperature=0.7,
            max_tokens=256,
            timeout=30  # Add timeout to prevent hanging
        )
        response_text = response.choices[0].message.content
        say(response_text)
        chatStr += f"{response_text}\n"
        return response_text
    except Exception as e:
        error_msg = f"Error in chat: {type(e).__name__}: {str(e)}"
        print(error_msg)  # Print detailed error to console
        
        # Provide specific error messages
        error_str = str(e).lower()
        if "authentication" in error_str or "api key" in error_str:
            say("API key authentication failed. Please check your OpenAI API key and billing.")
        elif "quota" in error_str or "billing" in error_str:
            say("OpenAI quota exceeded. Please check your billing and usage limits.")
        elif "network" in error_str or "timeout" in error_str:
            say("Network connection issue. Please check your internet connection.")
        else:
            say("Sorry, I encountered an error while processing your request.")
        
        return error_msg


def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=256,
            timeout=30  # Add timeout to prevent hanging
        )
        response_text = response.choices[0].message.content
        text += response_text
        
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
            f.write(text)
        
        say("AI response saved to file")
    except Exception as e:
        error_msg = f"Error in AI function: {type(e).__name__}: {str(e)}"
        print(error_msg)  # Print detailed error to console
        
        # Provide specific error messages
        error_str = str(e).lower()
        if "authentication" in error_str or "api key" in error_str:
            say("API key authentication failed. Please check your OpenAI API key and billing.")
        elif "quota" in error_str or "billing" in error_str:
            say("OpenAI quota exceeded. Please check your billing and usage limits.")
        elif "network" in error_str or "timeout" in error_str:
            say("Network connection issue. Please check your internet connection.")
        else:
            say("Sorry, I encountered an error while processing your AI request.")
        
        print(error_msg)

def say(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Neo"

if __name__ == '__main__':
    print('Welcome to Neo A.I')
    say("Neo A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query:
            # You can change this to your music file path
            musicPath = "C:\\Users\\demot\\Music\\music.mp3"  # Update this path
            if os.path.exists(musicPath):
                os.system(f'start "" "{musicPath}"')
            else:
                say("Music file not found. Please update the music path.")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hours and {min} minutes")

        elif "open facetime".lower() in query.lower():
            # Windows equivalent - you can replace with Skype, Teams, etc.
            say("FaceTime is not available on Windows. Opening Skype instead.")
            os.system("start skype:")

        elif "open pass".lower() in query.lower():
            # You can replace this with your preferred password manager
            say("Opening Windows Security or you can install a password manager.")
            os.system("start ms-settings:signinoptions")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Neo Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)





        # say(query)