import speech_recognition as sr    # wnat to add message on whatsapp
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
        webbrowser.open("https://web.whatsapp.com/")
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
            # "spotify" in c.lower():
            webbrowser.open(f"https://www.youtube.com/")
            speak(f"playing {song_name} in youtube")
           
            pyperclip.copy(song_name)
            time.sleep(3)
           
            pyautogui.click  (x=559, y=224)     # here is the searching button of youtube   
            time.sleep(3)

            pyautogui.write(song_name)  # Type the contact name
            time.sleep(2)
            
            pyautogui.press("enter")  
            time.sleep(1)
            pyautogui.click(x=282, y=533)
            
            # pyautogui.click (x=534, t=560) # adjust the coordinates to focus on the search bar       
            # pyautogui.click (x=534, t=560) # adjust the coordinates to focus on the search bar       
            # time.sleep(2)
            
        # # elif "youtube" in c.lower():
        # elif "youtube" in song_name:
        #     speak(f"Playing {song_name} on YouTube")
        #     webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
        #     pyautogui.press("enter")  # Select the contact
        #     time.sleep(2)
        # else:
        #      speak(f"Sorry, I couldn't find a platform for {song_name}")
             
             
    
    elif "message" in c.lower():
        # Step 1: Get the message from the user
            speak("please tell me the message")
            with sr.Microphone() as source:
                print("listening.......")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                message = recognizer.recognize_google(audio).lower()
                print(f"message:{message}")
        # Step 2: Get the contact name from the user
            speak("Please tell me the name of the contact.")
            with sr.Microphone() as source:  # New `with` block for the contact
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                contact = recognizer.recognize_google(audio).lower()
                print(f"contact:{contact}")
                speak(f"sending message to {contact}")
            
        # step 3: open whatsapp web
                webbrowser.open("https://web.whatsapp.com/")
                time.sleep(8)   # wait for the page to load
    
        # Step 4: Copy the message to the clipboard
                pyperclip.copy(message)    

        # Step 5: Search for the contact and send the message
                pyautogui.click (x=239, y=313) # adjust the coordinates to focus on the search bar                # pyautogui.click(x=208, y=311)  # Adjust coordinates to focus on the search bar
                time.sleep(3)
                pyautogui.write(contact)  # Type the contact name
                time.sleep(5)
                pyautogui.press("enter")  # Select the contact
                time.sleep(2)
                pyautogui.click(x=1086, y=965)  # Adjust coordinates to focus on the message input box
                pyautogui.hotkey("ctrl", "v")  # Paste the message from the clipboard
                time.sleep(2)
                pyautogui.press("enter")  # Send the message        
        
                speak("Message sent successfully.")
    # it colose the page in which is open
    elif "close" in c.lower():
          pyautogui.click (x=1881, y=21) # adjust the coordinates to focus on the search bar                # pyautogui.click(x=208, y=311)  # Adjust coordinates to focus on the search bar
          time.sleep(3) 

    elif "search on youtube" in c.lower():
        speak("please tell me what you want to search")
        with sr.Microphone() as source:
            print("listening_for_search........")
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
            search_topic = recognizer.recognize_google(audio).lower()
            speak(f"searchimg {search_topic} on youtube")
            pyautogui.click  (x=559, y=224)    # here is the searching button of youtube   
            time.sleep(3)

            pyautogui.write(song_name)  
            time.sleep(2)
     
    # elif "search on google" in c.lower():
        # speak("please tell me what you want to search")
        # with sr.Microphone() as source:
        #     print("listening_for_search........")
        #     audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
        #     search_topic = recognizer.recognize_google(audio).lower()
        #     speak(f"searchimg {search_topic} on google")
            # webbrowser.open("https://www.google.com") 
    
    elif "exit" in c.lower():
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")        
    
# if __name__ == "__main__":
#     speak("initialising jarvis......")
#     while True:
#        # listen to the user "jarvis"
#        # obtain audio from the microphone
#        r = sr.Recognizer()
#        print("Recognising.......")
#        try:
#            # Listen for the keyword "Jarvis" 
#           with sr.Microphone() as source:
#                print("Listening for the keyword 'Jarvis'...")
#                audio = r.listen(source, timeout =5, phrase_time_limit=5) 
#                word = r. recognize_google(audio)     
        
#           if(word.lower()== "jarvis"):
#                speak("yes sir")
               
if __name__ == "__main__":
    speak("hi i'm dummy jarvis")
    while True:
        # Initialize the recognizer
        r = sr.Recognizer()
        print("Recognizing...")

        try:
            # Listen for the keyword "Jarvis"
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)  # Adjust for background noise
                print("Listening for the keyword 'jarvis'...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                word = r.recognize_google(audio).lower()

            if word == "jarvis":
                speak("Yes sir")              
               
               # Listen for the actual command
              
                with sr.Microphone()as source:
                    r.adjust_for_ambient_noise(source)  # Adjust for background noise
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