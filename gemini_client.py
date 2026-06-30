import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def ask_gemini(user_query):
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return "Gemini API key missing in .env file."
        
    try:
        
        client = genai.Client(api_key=api_key)
       
        prompt = f"You are Chanda (kind AI assistant as you are named chanda as my nani), a sweet and very short-answering voice assistant. Answer this in under 2 sentences: {user_query}"
        
        response = client.models.generate_content(
            model='gemini-1.5-flash', 
            contents=prompt,
        )
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "I am sorry, I faced a technical glitch."