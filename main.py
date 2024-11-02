
import speech_recognition as sr
import pyttsx3
import requests  # Import the requests library

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define the URL to which the alert will be sent
ALERT_URL = "http://your-server-url/alert"  # Replace with your actual server URL

while True:
    try:
        with sr.Microphone() as mic:
            # Adjust for ambient noise to improve accuracy
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)

            # Listen for audio input
            audio = recognizer.listen(mic)

            # Recognize and convert audio to text
            text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {text}")

            # Check if the recognized text is exactly "help"
            if text == "help":
                print("Alert triggered: 'Help' detected")
                engine.say("Help message received")
                engine.runAndWait()
                
                # Send an alert to the server
                payload = {'alert': 'Help detected!'}  # Customize the payload as needed
                response = requests.post(ALERT_URL, json=payload)

                # Print the response from the server (for debugging purposes)
                print(f"Response from server: {response.status_code} - {response.json()}")

    except sr.UnknownValueError:
        # If speech is unintelligible, reset recognizer and continue listening
        recognizer = sr.Recognizer()
        continue

