import speech_recognition as speech_rec
import pyttsx4 as tts
from dotenv import load_dotenv
from os import getenv
import AppOpener
import pywhatkit as pwk

load_dotenv()

listener = speech_rec.Recognizer()

engine = tts.init()

engine.setProperty("rate", 180)  # setting up new voice rate

# changing index, changes voices. 0 for male and 1 for female
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(speech: str) -> None:
    print(f"Speaking {speech}")
    tts.speak(speech)


def listen():
    try:
        with speech_rec.Microphone() as source:
            print("\nListening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source, timeout=7, phrase_time_limit=5)
            command = listener.recognize_wit(voice, key=getenv("WIT_API_KEY")).lower()
            return command
    except speech_rec.UnknownValueError:
        print("Didn't get that!")
        return ""
    except speech_rec.RequestError:
        speak("VoxoLaunch can't connect to Wit.ai. Retrying...")
        return ""
    except Exception as e:
        speak(f"VoxoLaunch error: {str(e)}. Retrying...")
        return ""


while True:
    try:
        command = listen()
        if command.startswith("open "):
            app_name = command[5:]
            speak("Opening " + app_name)
            try:
                output = AppOpener.open(app_name, match_closest=True, throw_error=True)
                print(output)
            except AppOpener.features.AppNotFound:
                speak(
                    f"Could not find {app_name}\nMake sure it is installed on the system"
                )
        elif command.startswith("search "):
            query = command[7:]
            speak("Searching " + query + " on Google")
            pwk.search(query)
        elif command.startswith("play "):
            video_name = command[5:]
            speak("Playing " + video_name + " on YouTube")
            pwk.playonyt(video_name)
    except speech_rec.exceptions.UnknownValueError:
        print("Didn't get that!")
    except KeyboardInterrupt:
        print("Gracefully exiting...")
        break
