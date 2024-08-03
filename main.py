import speech_recognition as sr
import webbrowser
import pyttsx3
import AppOpener

# webbrowser is a built-in attached module in python

textToSpeech = pyttsx3.init()
# recognizer1 = sr.Recognizer()

def speak(text:str):
    textToSpeech.say(text)
    textToSpeech.runAndWait()


def processCommand(c):
    print(c)
    if "open google" in c.lower():
        speak("Opening google")
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        speak("Opening facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open github" in c.lower():
        speak("Opening github")
        webbrowser.open("https://github.com/")
    elif "open linkedin" in c.lower():
        speak("Opening linkedin")
        webbrowser.open("https://www.linkedin.com/")
    elif "open youtube" in c.lower():
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "open whatsapp" in c.lower():
        speak("Opening whatsapp")
        AppOpener.open("whatsapp", match_closest=True)
    elif "open word" in c.lower():
        speak("Opening word")
        AppOpener.open("ms word", match_closest=True)
    elif "open excel" in c.lower():
        speak("Opening excel")
        AppOpener.open("ms excel", match_closest=True)
    elif "open notepad" in c.lower():
        speak("Opening notepad")
        AppOpener.open("notepad", match_closest=True)
    elif "open vscode" in c.lower():
        speak("Opening vs code")
        AppOpener.open("visual studio code", match_closest=True)
    elif "close whatsapp" in c.lower():
        speak("closing whatsapp")
        AppOpener.close("whatsapp", match_closest=True)
    elif "close notepad" in c.lower():
        speak("closing notepad")
        AppOpener.close("notepad", match_closest=True)
    elif "close vscode" in c.lower():
        speak("closing vs code")
        AppOpener.close("visual studio code", match_closest=True)
    elif "open file explorer" in c.lower():
        speak("opening file explorer")
        AppOpener.open("file explorer", match_closest=True)
    elif "close file explorer" in c.lower():
        speak("closing file explorer")
        AppOpener.close("file explorer", match_closest=True)
    elif "open settings" in c.lower():
        speak("opening settings")
        AppOpener.open("settings", match_closest=True)
    elif "close settings" in c.lower():
        speak("closing settings")
        AppOpener.close("settings", match_closest=True)
    else:
        speak("invalid task")
    


if(__name__ == '__main__'):
    speak("Initializing Jarvis....")

    while True:
        
        recognizer = sr.Recognizer()

        try:
            # listen for the word jarvis
            with sr.Microphone() as mice:
                print("Listening....")
                audio = recognizer.listen(mice, timeout=2)

            word = recognizer.recognize_google(audio)

            print(word)

            if("jarvis" in word.lower()):
                speak("Yes I am here")
                # listening for command
                with sr.Microphone() as mice:
                    audio = recognizer.listen(mice)
                    command = recognizer.recognize_google(audio)
                    
                    processCommand(command)
                    

                    if "close yourself" in command.lower():
                        speak("closing down")
                        break

                    speak("Give me next task.")

        except Exception as e:
            pass



