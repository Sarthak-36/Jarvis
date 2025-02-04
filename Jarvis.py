import pyttsx3 #(For text to Speak) 
import datetime 
import speech_recognition as sr 
import wikipedia #(information)
import smtplib  #(to send mails)
import webbrowser as wb  #to browse on web
import os
import pyautogui  #for  
import psutil 
import pyjokes 
import wolframalpha
import time
from urllib.request import urlopen
import winshell



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    print("The current time is ", Time)
    speak("the current time is")
    speak(Time)
   
    Time=datetime.datetime.now().strftime("%I:%M:%S") # for 12-hour clock
    print("The current time is ", Time)
    speak(Time)
    
def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    print("Todays Date is %d/%d/%d" % (date, month, year))
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    speak("Welcome back!")
    # time_()
    # date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    elif hour >=18 and hour <24:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Jarvis at your service. Please tell me how can I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('email id', 'password')
    server.sendmail('email id', to, content)
    server.close()
def screenshot():
    img = pyautogui.screenshot()
    img.save(r"C:/Users/Sarthak Ukharde/Desktop/Notes/C Programming/Python/jarvis/sceenshot.png")
def cpu():
    usage = str(psutil.cpu_percent())
    print('CPU is at'+ usage)
    speak('CPU is at'+ usage)
    
    battery = psutil.sensors_battery()
    print("Battery is at ",battery.percent, '%')
    speak("Battery is at")
    speak(battery.percent)
    
def jokes():
    print(pyjokes.get_joke())
    speak(pyjokes.get_joke())
    
def Introduction():
    speak("I am JARVIS  , Personal AI assistant , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")
def q():
    speak("going Offline")
    quit()




    
if __name__ == '__main__':


    clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file
    clear()

    wishme()
    
    while True:
        query = TakeCommand().lower()
        '''All the commands said by user will be 
		stored here in 'query' and will be 
		converted to lower case for easily 
		recognition of command '''

        if 'time' in query:
            time_()
        elif 'date' in query:
            date()
        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("in wikipedia","")
            query= query.replace("search","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            time.sleep(5)
        elif 'google' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)
        
        elif 'search' in query: 
            query = query.replace("query","")
            wb.open(query)
        
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")
        elif "why you came to this world" in query:
            speak("Thanks to MAK. further it is a secret")
        elif 'word' in query:
            speak("opening MS Word")
            word = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
            os.startfile(word)
        elif 'publisher' in query:
            speak("opening MS Publisher")
            word = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Publisher.lnk"
            os.startfile(word)
        elif 'powerpoint' in query:
            speak("opening MS Powerpoint")
            word = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
            os.startfile(word)
        elif 'exel' in query:
            speak("opening MS Exel")
            word = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
            os.startfile(word)
        elif 'outlook' in query:
            speak("opening Ms Outlook")
            word = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
            os.startfile(word)
       
        

        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")

        elif 'recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled") 

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak("Who is the Reciever?")
                reciept = input("Enter recieptant's name: ")
                to = (reciept)
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")
        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        

        elif 'music' in query or 'song' in query:
            music_dir = 'D:\Music'
            songs = os.listdir(music_dir)
            print(songs)
            speak("Enter the Serial Number of The song") 
            sng=int(TakeCommand())   
            os.startfile(os.path.join(music_dir, songs[sng]))
                


            
        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())
        
        
        elif "write a note" in query:
            speak("What should i write, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)
                
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 

        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")    
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'tell me about yourself' and 'who are you' in query:
            Introduction()
        
        
        #show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query or 'girlfriend' in query or 'boyfriend' in query:
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("It's hard to understand, I am still trying to figure this out.")
        

        #calculation
        elif "calculate" in query:
            
            app_id = "KX8U6P-JWH89LVA6Y"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        #General Questions
        elif "what is" in query or "who is" in query: 
			
			# Use the same API key 
			# that we have generated earlier
            client = wolframalpha.Client("KX8U6P-JWH89LVA6Y")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results") 

        #sleep-time
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        #quit
        elif 'offline' in query  or 'quit'in query:
            q()
        
            