import os
import speech_recognition as sr
import webbrowser
from gtts import gTTS
import pygame
import time
import musicLibrary
import feedparser
import datetime
from gemini_client import ask_gemini

pygame.mixer.init()

def speak(text):
    print(f"[Chanda Speaking]: {text}")
    try:
        
        tts = gTTS(text=text ,lang='en', tld='co.in')
        filename = "temp_voice.mp3"
        tts.save(filename)
        
        
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        
        
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
        
        pygame.mixer.music.unload()
        os.remove(filename)
    except Exception as e:
        print(f"Speaking Error: {e}")

def processCommand(c):
    # print(f"Executing command: {c}")
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening Youtube")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")    
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram")
    elif c.lower().startswith("play"):
        song=" ".join(c.lower().split(" ")[1:])
        link= musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
      speak("Fetching the latest headlines from Google News...")
      rss_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
      feed = feedparser.parse(rss_url)
      entries = feed.entries[:5]
    
      if entries:
        speak("Here are the top five news headlines for today:")
        for i, entry in enumerate(entries, 1):
            clean_title = entry.title.split(" - ")[0]
            print(f"Headline {i}: {clean_title}")
            speak(f"Headline number {i}. {clean_title}")
            time.sleep(0.3)
        speak("That's all the news for now.")
      else:
        speak("Sorry, I couldn't fetch the news right now.")
    elif "time" in c.lower():
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in c.lower():
        today = datetime.date.today()
        current_date = today.strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")    
    else:
        print("Thinking...")
        ai_response = ask_gemini(c)
        print(f"Chanda: {ai_response}")
        speak(ai_response)    
    
if __name__ == "__main__":
    speak("Initializing chanda.....")
    
    r = sr.Recognizer()
    
    while True:
        print("\nrecognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word.....")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=6, phrase_time_limit=4)
            
            word = r.recognize_google(audio)
            print(f"Google heard: {word}")
            
            if "chanda" in word.lower() or "chandra" in word.lower():
                print("chanda active.....")
                speak("Yes, how can I help you?")
                
                time.sleep(1) 
                
                with sr.Microphone() as source:
                    print("Listening for your command.....")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, timeout=6, phrase_time_limit=10)
                
                command = r.recognize_google(audio, language='en-in')
                print(f"Your command: {command}")
                processCommand(command)

        except sr.UnknownValueError:
            pass
        except Exception as e:
            print(f"System Error: {e}") 