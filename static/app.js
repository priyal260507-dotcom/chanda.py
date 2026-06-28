// 1. आपके HTML के एलिमेंट्स को कनेक्ट करना
const micBtn = document.getElementById('micBtn');
const statusText = document.getElementById('status');
const responseBox = document.getElementById('response-box');

// 2. ब्राउज़र का माइक सेटअप
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.lang = 'en-IN'; 

// 3. जब आप Moon बटन पर क्लिक करेंगी
micBtn.addEventListener('click', () => {
    statusText.innerText = "Status: Listening...";
    responseBox.innerText = "Listening for your command...";
    recognition.start();
});

// 4. जब आप बोलना बंद कर देंगी
recognition.onresult = function(event) {
    const userSpokenText = event.results[0][0].transcript;
    
    statusText.innerText = "Status: Processing...";
    responseBox.innerText = "You said: " + userSpokenText;

    // Python (app.py) को टेक्स्ट भेजें
    fetch('/ask-chanda', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userSpokenText })
    })
    .then(response => response.json())
    .then(data => {
        let aiReply = data.reply;
        
        // --- 🎵 म्यूज़िक वाला नया लॉजिक यहाँ आ गया है 🎵 ---
        if (aiReply.includes("|||")) {
            let parts = aiReply.split("|||");
            let textToSpeak = parts[0].trim(); // "Playing Song"
            let musicLink = parts[1].trim();   // "https://youtube..."

            statusText.innerText = "Status: Idle";
            responseBox.innerText = "Chanda: " + textToSpeak; 
            speakResponse(textToSpeak);       // Chanda बोलेगी
            window.open(musicLink, "_blank"); // यहाँ गाना प्ले हो जाएगा!
            return; // आगे का कोड मत चलाओ
        }
        // ----------------------------------------------------

        // बाकी नार्मल जवाब और वेबसाइट्स के लिए
        statusText.innerText = "Status: Idle";
        responseBox.innerText = "Chanda: " + aiReply; 
        speakResponse(aiReply); 

        if (aiReply.includes("Opening Google")) window.open("https://google.com", "_blank");
        else if (aiReply.includes("Opening Youtube")) window.open("https://youtube.com", "_blank");
        else if (aiReply.includes("Opening Facebook")) window.open("https://facebook.com", "_blank");
        else if (aiReply.includes("Opening LinkedIn")) window.open("https://linkedin.com", "_blank");
        else if (aiReply.includes("Opening Instagram")) window.open("https://instagram.com", "_blank");
    })
    .catch(error => {
        console.error("Error:", error);
        statusText.innerText = "Status: Error connecting to server";
    });
};

// 5. बोलने वाला फंक्शन (Voice)
function speakResponse(text) {
    const speech = new SpeechSynthesisUtterance();
    speech.text = text;
    speech.volume = 1;
    speech.rate = 1;
    speech.pitch = 1;

    // --- यहाँ से नया कोड (लड़की की आवाज़ के लिए) ---
    let voices = window.speechSynthesis.getVoices();
    
    // यह लाइन Zira या किसी भी फीमेल वॉइस को ढूँढेगी
    let femaleVoice = voices.find(voice => 
        voice.name.includes('Zira') || 
        voice.name.includes('Female') || 
        voice.name.includes('Samantha') || 
        voice.name.includes('Google हिन्दी')
    );
    
    if (femaleVoice) {
        speech.voice = femaleVoice;
    }
    // ----------------------------------------------

    window.speechSynthesis.speak(speech);
}