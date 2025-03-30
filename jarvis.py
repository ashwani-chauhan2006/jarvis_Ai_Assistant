import speech_recognition as sr
import webbrowser
import pyttsx3
import pyautogui
import time
import pyperclip
# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()
    
def processcommand(c):
    """Process the user's command."""
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")

    elif "open whatsapp" in c.lower():
        speak("opening whatsapp")
        webbrowser.open("https://www.whatsapp.com")

    elif "open github" in c.lower():
        speak("opening github")
        webbrowser.open("https://www.github.com")

    elif "open instagram" in c.lower():
        speak("opening instagram")
        webbrowser.open("https://www.instagram.com")        

    elif "play music" in c.lower():
        speak("please tell me the song name")
        with sr.Microphone() as source:
            print("listening.......")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            song_name = recognizer.recognize_google(audio).lower()
            print(f"song_name:{song_name}")
            time.sleep(1)
            webbrowser.open(f"https://www.youtube.com/")
            speak(f"playing {song_name} in youtube")
        # it copy the song name to the clipboard
            pyperclip.copy(song_name)
            time.sleep(3)
        # it click on the search bar of youtube
            pyautogui.click  (x=559, y=224)       
            time.sleep(3)
        # it paste the song name from the clipboard
            pyautogui.write(song_name) 
            time.sleep(2)
        # it click on the search button of youtube
            pyautogui.press("enter")  
            time.sleep(1)
        # it click on the first song of the youtube
            pyautogui.click(x=282, y=533)   
    
    elif "message" in c.lower():
        # Get the message from the user
            speak("please tell me the message")
            with sr.Microphone() as source:
                print("listening.......")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                message = recognizer.recognize_google(audio).lower()
                print(f"message:{message}")
        # Get the contact name from the user
            speak("Please tell me the name of the contact.")
            with sr.Microphone() as source:  
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                contact = recognizer.recognize_google(audio).lower()
                print(f"contact:{contact}")
                speak(f"sending message to {contact}")            
        # open whatsapp web
                webbrowser.open("https://web.whatsapp.com/")
                time.sleep(8)   # wait for the page to load    
        # Copy the message to the clipboard
                pyperclip.copy(message)    
        # Search for the contact and send the message
                pyautogui.click (x=239, y=313)              
                time.sleep(3)  
        # it search the contact name in the search bar of whatsapp                       
                pyautogui.write(contact) 
                time.sleep(5)
        # it click on the first contact of the whatsapp        
                pyautogui.press("enter")  
                time.sleep(2)
        # it click on the message input box of whatsapp        
                pyautogui.click(x=1086, y=965)  
        # it paste the message from the clipboard        
                pyautogui.hotkey("ctrl", "v")  
                time.sleep(2)
        # it click on the send button of whatsapp        
                pyautogui.press("enter")                 
                speak("Message sent successfully.")
    
    # it colose the page in which is open
    elif "close" in c.lower():
          pyautogui.click (x=1881, y=21)                
          time.sleep(3)         

    elif "exit" in c.lower():
        speak("Goodbye i am going to sleep")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")        
    
if __name__ == "__main__":
    speak("initialising jarvis......")
    while True:
       # listen to the user "jarvis"
       # obtain audio from the microphone
       r = sr.Recognizer()
       print("recognising.......")
       try:
          with sr.Microphone() as source:
               print("listening......")
               audio = r.listen(source, timeout =5, phrase_time_limit=5) 
          word = r. recognize_google(audio)     
          if(word.lower()== "jarvis"):
               speak("yes sir")
               # Listen for the actual command
               with sr.Microphone()as source:
                    print("jarvis active")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r. recognize_google(audio).lower()                
                    # Process the command
                    processcommand(command) 
      
       except sr.WaitTimeoutError:
            print("Listening timed out. Restarting...")
       except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
       except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
       except Exception as e:
            print(f"An unexpected error occurred: {e}")              