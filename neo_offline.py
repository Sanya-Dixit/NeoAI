import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3


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

def offline_chat(query):
    """Simple offline responses for common queries"""
    query_lower = query.lower()
    
    responses = {
        "hello": "Hello! I'm Neo, your AI assistant running in offline mode.",
        "how are you": "I'm doing well, thank you for asking!",
        "what is your name": "I'm Neo, your AI assistant.",
        "what can you do": "I can open websites, tell time, play music, and have basic conversations in offline mode.",
        "thank you": "You're welcome!",
        "bye": "Goodbye! Have a great day!",
        "weather": "I'm in offline mode, so I can't check the weather right now.",
        "news": "I'm in offline mode, so I can't fetch news right now.",
    }
    
    # Check for matches
    for key, response in responses.items():
        if key in query_lower:
            return response
    
    # Default response
    return "I'm currently running in offline mode. I can help you open websites, tell time, or play music. For AI conversations, please check your internet connection and OpenAI API setup."

if __name__ == '__main__':
    print('Welcome to Neo A.I (Offline Mode)')
    say("Welcome to Neo AI offline mode")
    
    while True:
        print("Listening...")
        query = takeCommand()
        query_lower = query.lower() if isinstance(query, str) else ""

        # Handle recognition failures
        if query_lower.startswith("some error occurred"):
            say("I didn't catch that. Please repeat.")
            continue

        # Exit commands (accept several variants)
        if any(keyword in query_lower for keyword in ("neo quit", "quit", "exit", "goodbye", "bye", "stop", "shutdown")):
            say("Goodbye!")
            break

        # Website opening (works offline)
        sites = [["youtube", "https://www.youtube.com"], 
                ["wikipedia", "https://www.wikipedia.com"], 
                ["google", "https://www.google.com"]]
        
        site_opened = False
        for site in sites:
            if f"open {site[0]}" in query_lower:
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                site_opened = True
                break
        
        if site_opened:
            continue
            
        # Music (works offline)
        if "open music" in query_lower:
            musicPath = "C:\\Users\\demot\\Music\\music.mp3"
            if os.path.exists(musicPath):
                os.system(f'start "" "{musicPath}"')
                say("Opening music")
            else:
                say("Music file not found. Please update the music path.")
                
        # Time (works offline)
        elif "time" in query_lower:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"The time is {hour} hours and {min} minutes")
            
        # Offline chat
        else:
            response = offline_chat(query)
            say(response)
            print(f"Neo: {response}")

print("Neo offline mode ended.")
