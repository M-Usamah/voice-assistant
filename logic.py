import pyttsx3
import speech_recognition as sr
import datetime

def speak(talk):
    engine = pyttsx3.init()
    engine.say(talk)
    engine.runAndWait()

def time():
    hour = int(datetime.datetime.now().hour)
    minu = int(datetime.datetime.now().minute)
    he = ["Sir the time is ", hour , 'Hours' "and" , minu ,"minutes"]
    speak(he)

# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
#         print(f"User said: {query}\n")  #User query will be printed.

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")   #Say that again will be printed in case of improper voice 
#         return "None" #None string will be returned
#     return query

def order():
    r = sr.Recognizer()
    
    with sr.Microphone() as mic:
        command = str("sir give me a command...... ")
        speak(command)
        print(command)
        r.pause_threshold = 1
        audio = r.listen(mic)

    try:
        speak("searching")
        print("Searching..........")
        query = r.recognize_google(audio, language='en-US')
        print(f"Your command is : {query}\n")

    except Exception as e:
        # print(e)
        # speak("sir can you repeat it again....")
        return"none"
    return query
        # break

if __name__ == "__main__":
    speak("hello sir..... \n did you have a good day\n")
    # time()
    # takeCommand()
    order()