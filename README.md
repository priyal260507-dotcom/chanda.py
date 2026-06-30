# 🌙 Chanda - Smart AI Voice Assistant

**Project Submission**
*Swami Keshvanand Institute of Technology (SKIT)*
*B.Tech - Artificial Intelligence (AI)*

## 📖 About the Project
Chanda is an intelligent, web-based voice assistant built using Python, Flask, and the powerful Google Gemini AI model. Designed to be completely cloud-ready, it shifts hardware dependencies (like microphone and speaker access) to the client-side browser, ensuring seamless deployment on cloud platforms without crashing.

## 📂 Project Structure (The Two Versions)
This project has been developed in two distinct phases to show the progression from a local script to a cloud-ready web application:

1. **`main.py` (Local Prototype):** The original version built for local desktop execution. It relies on hardware-dependent libraries (`pygame`, `SpeechRecognition`) to directly access the laptop's microphone and speakers. *Best for local testing.*
2. **`app.py` (Cloud-Ready Production Server):** The upgraded Flask-based web application. It smartly shifts the hardware dependencies (microphone/speaker access) to the client's browser using the Web Speech API. *This is the version deployed on the cloud.*

## ✨ Key Features
* **Conversational AI:** Powered by Google Gemini API to answer general knowledge questions and provide smart, context-aware responses.
* **Voice User Interface (VUI):** Utilizes the Web Speech API for real-time Speech-to-Text (listening) and Text-to-Speech (speaking) directly in the browser.
* **Web Automation:** Smartly parses user intent to automatically open specific websites (YouTube, Google, LinkedIn, etc.) in new tabs.
* **Live News Fetching:** Uses RSS feeds (`feedparser`) to fetch and read out the latest top news headlines.
* **Music Library Access:** Plays predefined songs from a custom music library logic.
* **Utility Tools:** Accurately fetches and reports the current system time and date.
* **Smart Wake-Word Activation:** The AI is now more interactive; simply saying "Chanda" (or conversational phrases like "Chanda,can you listen to me?") triggers an immediate confirmation: "Yes,how can I help you?"
## 🛠️ Technology Stack
* **Backend:** Python 3, Flask (Web Framework), google-generativeai
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (DOM manipulation & Web Speech API)
* **Libraries/Modules:** datetime, feedparser

## 🚀 Architecture Update
To make this application serverless-friendly (for platforms like Vercel), the architecture was migrated from a hardware-dependent local script (`speech_recognition`, `pygame`, `webbrowser`) to a true **Client-Server model**. 
- The **Backend (Flask)** handles logic, API calls, and text processing.
- The **Frontend (Browser)** handles all media interactions (Microphone, Audio synthesis, and opening new tabs).

## ⚠️ Note for Evaluators / Users
* **Recommended Browser:** Please run this application on **Google Chrome**. The Web Speech API (used for the microphone and voice synthesis) works most seamlessly and accurately on the Chrome engine.

## 👨‍💻 Developed By
* **Name:** PRIYAL AGRAWAL
* **Roll Number:** 25ESKCA176
* **ID:** B250835
*