import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def capture_voice():
    
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"Captured Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None

def translate_text(text, target_language):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language)
        print(f"Translated Text ({target_language}): {translated.text}")
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return None

def text_to_speech(text, language):
    try:
        tts = gTTS(text=text, lang=language)
        tts.save("translated_audio.mp3")
        print("Playing translated audio...")
        os.system("start translated_audio.mp3")  
    except Exception as e:
        print(f"Text-to-speech conversion error: {e}")

if __name__ == "__main__":
    print("Voice to Text and Translation Application")
    print("Supported Languages:")
    print("| Language     | Code |")
    print("|--------------|------|")
    print("| Afrikaans    | af   |")
    print("| Arabic       | ar   |")
    print("| Bengali      | bn   |")
    print("| Chinese (Simplified) | zh-CN |")
    print("| Chinese (Traditional) | zh-TW |")
    print("| Czech        | cs   |")
    print("| Danish       | da   |")
    print("| Dutch        | nl   |")
    print("| English      | en   |")
    print("| Finnish      | fi   |")
    print("| French       | fr   |")
    print("| German       | de   |")
    print("| Greek        | el   |")
    print("| Gujarati     | gu   |")
    print("| Hebrew       | he   |")
    print("| Hindi        | hi   |")
    print("| Hungarian    | hu   |")
    print("| Indonesian   | id   |")
    print("| Italian      | it   |")
    print("| Japanese     | ja   |")
    print("| Kannada      | kn   |")
    print("| Korean       | ko   |")
    print("| Malayalam    | ml   |")
    print("| Marathi      | mr   |")
    print("| Nepali       | ne   |")
    print("| Norwegian    | no   |")
    print("| Persian      | fa   |")
    print("| Polish       | pl   |")
    print("| Portuguese   | pt   |")
    print("| Punjabi      | pa   |")
    print("| Romanian     | ro   |")
    print("| Russian      | ru   |")
    print("| Slovak       | sk   |")
    print("| Spanish      | es   |")
    print("| Swedish      | sv   |")
    print("| Tamil        | ta   |")
    print("| Telugu       | te   |")
    print("| Thai         | th   |")
    print("| Turkish      | tr   |")
    print("| Ukrainian    | uk   |")
    print("| Urdu         | ur   |")
    print("| Vietnamese   | vi   |")

    target_language = input("Enter the target language code: ").strip()
    
    text = capture_voice()
    if text:
        translated_text = translate_text(text, target_language)
        if translated_text:
            text_to_speech(translated_text, target_language)
