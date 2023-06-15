import datetime
import pyttsx3
import speech_recognition as sr 
import pyaudio

def tellDay(): 



    day = datetime.datetime.today().weekday() + 1



    Day_dict = {1: 'lunes', 2: 'martes',  
                3: 'miercoles', 4: 'jueves',  
                5: 'viernes', 6: 'sabado', 
                7: 'domingo'} 

    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("el dia es " + day_of_the_week) 

def tellTime(): 


    time = str(datetime.datetime.now()) 




    print(time) 
    hour = time[11:13] 
    min = time[14:16] 
    speak("la hora es" + hour + "horas y" + min + "minutos")     



def speak(audio): 

    engine = pyttsx3.init() 


    voices = engine.getProperty('voices') 



    engine.setProperty('voice', voices[0].id) 


    engine.say(audio)   



    engine.runAndWait() 


def Hello(): 
    speak("hola me llamo bob y soy tu asistente personalizado, cual es tu duda") 


def takeCommand(): 

    r = sr.Recognizer() 

    with sr.Microphone() as source: 
        print('escuchando') 

        r.pause_threshold = 1.7
        audio = r.listen(source) 

        try: 
            print("grabando") 




            Query = r.recognize_google(audio, language='en') 
            print("el comando esta impreso=", Query) 

        except Exception as e: 
            print(e) 
            print("decilo de nuevo") 
            return "None"

        return Query 
    
def Take_query(): 

    Hello() 

    while(True): 

        query = takeCommand().lower() 
        if "open geeksforgeeks" in query: 
            speak("Opening GeeksforGeeks ") 
            open("www.geeksforgeeks.com") 
            continue

        elif "what are you" in query: 
            speak("soy un braquiosaurio") 
            continue

        elif "home" in query: 
            speak("que hace un tsunami en africa, chococrispis jajajajaja") 
            continue

        elif "estas" in query: 
            speak("estoy bien y vos") 
            continue    

        elif "bien" in query: 
            speak("me alegro") 
            continue    


        elif "anime" in query: 
            speak("abriendo anime FVL")
            open("https://www3.animeflv.net/") 
            continue

        elif "whatsapp" in query: 
            speak("abriendo whatsapp") 
            open("https://web.whatsapp.com/") 
            continue    
   
    
        elif "youtube" in query: 
            speak("abiriendo youtube") 
            open("www.youtube.com/watch?v=mCdA4bJAGGk") 
            continue

        elif "google" in query: 
            speak("abiriendo google ") 
            open("www.google.com") 
            continue

        elif "dia" in query: 
            tellDay() 
            continue

        elif "hora" in query: 
            tellTime() 
            continue


        elif "de wikipedia" in query: 



            speak("buscando en wikipedia ") 
            query = query.replace("wikipedia", "") 



        elif "nombre" in query: 
            speak("yo soy bob tu asistente, me gusta el porro  y el fernet")    

        


        elif "adios" in query: 
            speak("Bye. cualquien cosa me hablas") 
            exit() 

        else :
            speak("no te entiendo")

        if __name__ == "__main__" :

            Take_query()
