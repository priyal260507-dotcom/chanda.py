import musicLibrary
from flask import Flask, render_template, jsonify, request
import os
import feedparser
import datetime
import time




from gemini_client import ask_gemini

app = Flask(__name__)





def process_command_text(c):
    """Processes the spoken text command and returns the reply string"""
    c_lower = c.lower()
    
    if "open google" in c_lower:
        reply = "Opening Google"
        return reply
       
    
        
    elif "open youtube" in c_lower:
        reply = "Opening Youtube"
        return reply
        
        
        
    elif "open facebook" in c_lower:
        reply = "Opening Facebook"
        return reply
        
        
        
    elif "open linkedin" in c_lower:
        reply = "Opening LinkedIn"
        return reply
      
        
        
    elif "open instagram" in c_lower:
        reply = "Opening Instagram"
        return reply
        
        
    elif "play" in c_lower:
        found_song = None
        
        for song_name in musicLibrary.music.keys():
            if song_name in c_lower:
                found_song = song_name
                break  
        
        
        if found_song:
            link = musicLibrary.music[found_song]
            reply = f"Playing {found_song} ||| {link}"
            return reply
        
        else:
            return ask_gemini(c)
    elif "time" in c_lower:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        reply = f"The current time is {current_time}"
        return reply

    elif "date" in c_lower:
        today = datetime.date.today()
        current_date = today.strftime("%B %d, %Y")
        reply = f"Today's date is {current_date}"
        return reply       
            
    elif "news" in c_lower or "headline" in c_lower:
        import feedparser
        news_url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms" 
        feed = feedparser.parse(news_url)
        
        reply = "Here are the top 5 news headlines for today. "
        for i in range(5): # यहाँ 5 लिखा है, तो वह 5 न्यूज़ ही लाएगा
            try:
                reply += f"News {i+1}: {feed.entries[i].title}. "
            except IndexError:
                break
                
        return reply       
            
    elif "news" in c_lower:
       
        rss_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
        feed = feedparser.parse(rss_url)
        entries = feed.entries[:3]  # Pulled top 3 for speed optimization
        
        if entries:
            headlines = []
        
            for i, entry in enumerate(entries, 1):
                clean_title = entry.title.split(" - ")[0]
                headlines.append(f"{i}. {clean_title}")
            return "News headlines spoken out loud!\n" + "\n".join(headlines)
        
                
        else:
            reply = "Sorry, I couldn't fetch the news right now."
            return reply
            
            
    elif "time" in c_lower:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        reply = f"The current time is {current_time}"
        return reply
        
        
    elif "date" in c_lower:
        today = datetime.date.today()
        current_date = today.strftime("%B %d, %Y")
        reply = f"Today's date is {current_date}"
        return reply
        
        
    else:
        print("Thinking...")
        ai_response = ask_gemini(c)
        print(f"Chanda: {ai_response}")
        return ai_response
        

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask-chanda', methods=['POST'])
def ask_chanda():
    try:
        
        data = request.get_json()
        user_command = data.get('message')

        if not user_command:
            return jsonify({"status": "error", "reply": "No command received"})

        
        final_reply = process_command_text(user_command)

        
        return jsonify({
            "status": "success",
            "reply": final_reply
        })

    except Exception as e:
        print(f"Backend Routing Error: {e}")
        return jsonify({"status": "error", "reply": f"System Error: {str(e)}"})
if __name__ == '__main__':
    app.run(debug=True, port=5000)