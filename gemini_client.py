import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def ask_gemini(user_query):
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return "Gemini API key missing in .env file."
        
    try:
        user_input = user_query.strip().lower()
        wake_words = ["chanda", "listen", "hear" ,"help", "can you"]
        if any(word in user_input for word in wake_words):
            return "Yes, how can I help you?"
        prompt = f"You are Chanda (kind AI assistant as you are named chanda as my nani), a sweet and very short-answering voice assistant. Answer this in under 2 sentences: {user_query}"
        
        model = genai.GenerativeModel('gemini-2.5-flash')
        
       
        response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "I am sorry, I faced a technical glitch."