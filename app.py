import pyttsx3
import os

pyttsx3.speak("Bonjour connections")

print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*Welcome To My LinkedIn Page*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print()
print("services available:\n1.chrome\n2.Notepad\n3.wmplayer\n4.KMPlayer\n5.spotify\n6.firefox\n7.skype\n8.atom\n........................................................THANKYOU.....................................................")

while True:
    a=input("enter the app name:") 
  
  
    if ("can" in a or "you" in a  or "run" in a or "open" in a) and ("chrome" in a):
            os.system("chrome")
    elif ("can" in a or "you" in a  or "run" in a or "open" in a) and ("notepad" in a):  
            os.system("Notepad")
    elif ("can" in a or "you" in a or "run" in a or "open" in a) and ("wmplayer" in a):
            os.system("wmplayer")
    elif ("can" in a or "you" in a or "run" in a or "open" in a) and ("kmplayer" in a):
            os.system("KMPlayer")
    elif ("can" in a or "you" in a or "run" in a or "open" in a) and ("spotify" in a):
            os.system("spotify")
    elif ("can" in a or "you" in a or "run" in a or "open" in a) and ("firefox" in a):
            os.system("firefox")
    elif ("can" in a or "you" in a or "run" in a or "open" in a) and ("skype" in a):
            os.system("skype")
    elif ("can" in a or "you" in a or "run" in a or "open" in a) and ("atom" in a):
            os.system("atom")  
    elif ("can" in a or "you" in a or "run" in a or "open" in a) and ("spotify and notepad" in a):
            os.system("spotify")
            os.system("notepad") 
    elif ("can" in a or "you" in a or "run" in a or "open" in a or "manogna" or "fb page") and ("facebook" in a or "fb" in a):
            os.system("chrome www.facebook.com/manognya.reddy.549")
    elif ("can" in a or "you" in a or "run" in a or "open" in a) and ("chrome" in a):
            os.system("chrome www.youtube.com")
    elif ("play" in a or "love you zindagi song" in a or "chrome" in a):
            os.system("chrome www.youtube.com/watch?v=hxjABEwwrTc")
    elif ("who" in a or "is" in a or "vimal daga" in a):
            os.system("chrome www.google.com/search?q=vimal+daga&oq=&aqs=chrome.0.69i59l8.88820927j0j15&sourceid=chrome&ie=UTF-8")
    elif ("feedback"):       
            y=input("Rating Please:")
            if ("10" in y):
                 print("Visit again best regards manogna *_*")
                 exit()
    elif ("can" in a or "you" in a or "please" in a) and ("exit" in a or "quit" in a):
           break       
    else:
        print("sorry service is not available")
