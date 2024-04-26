import eel
import time
import pygame
from io import BytesIO
from gtts import gTTS
import speech_recognition as sr
import google.generativeai as genai

def speak(text):
    print(text)
    tts = gTTS(text, lang='en')
    pygame.mixer.init()
    for chunk in tts.stream():
        f = BytesIO()
        f.write(chunk)
        f.seek(0)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()
    pygame.mixer.quit()

@eel.expose
def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 5)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio)
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        response= ai_response(query)
        eel.DisplayResponse(response)
        speak(response)
        time.sleep(2)
        eel.ShowHood()
    except sr.UnknownValueError:
        eel.DisplayMessage("Something went wrong")
        eel.ShowHood()
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))  
    except Exception as e:
        return "Something went wrong"
    
    return query.lower()

def ai_response(text):
    instruction = 'output instruction: word length<30 and use alphabets and numbers only (avoid asterisk and avoid answer in points)'
    full_text = f'{instruction}\nquery:{text}'
    genai.configure(api_key='API_KEY')
    response= ''
    try:
        model= genai.GenerativeModel(model_name='gemini-pro')
        response= model.generate_content(full_text)
    except Exception as e:
        response= 'Something went wrong'
    
    return response.text.replace("*", "")

if __name__ == '__main__':
    print(speak("hey ai model, what can you do. today we will learn python and build a new program."))