import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def ask_gemini(user_query):
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return "Gemini API key missing in .env file."
        
    try:
        prompt = f"You are Chanda (kind AI assistant as you are named chanda as my nani), a sweet and very short-answering voice assistant. Answer this in under 2 sentences: {user_query}"
        # यहाँ Client की जगह GenerativeModel का इस्तेमाल करें
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 'client.models.generate_content' की जगह सीधे 'model.generate_content'
        response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "I am sorry, I faced a technical glitch."