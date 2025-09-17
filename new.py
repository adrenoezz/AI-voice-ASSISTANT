import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif c.startswith("play "):  # command like "play despacito"
        song = c.split(" ")[1]   # take the word after "play"
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open_new_tab(link)
            speak(f"Playing {song}")
        else:
            speak(f"Sorry, I don't know the song {song}")

            

        

if __name__ == "__main__":
    speak("Initializing Jarvis...")
else:
    

    while True:
        with sr.Microphone() as source:
            print("Adjusting for background noise... Please wait.")
            r.adjust_for_ambient_noise(source, duration=1)

            print("🎤 Say something:")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="en-IN")
            print("You said:", text)

            # Call processCommand here
            processCommand(text)

            if "stop" in text.lower() or "exit" in text.lower():
                speak("Goodbye!")
                break

        except sr.UnknownValueError:
            print("❌ Sorry, I could not understand that.")
        except sr.RequestError:
            print("⚠️ Could not request results; check your internet connection.")
