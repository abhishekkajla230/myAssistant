import pyttsx3 #pip install this
import datetime
from time import sleep
import webbrowser
import wikipedia #pip install this
import speech_recognition #pip install this speechRecognition
import os
from random import randint
import smtplib #modules for sending email

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
rate = engine.getProperty('rate') # to check the rate/speed of speech
engine.setProperty('rate',150) # to set or update new properties
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour >= 0 and hour <12:
        speak("Good Morning Abhishek")
    elif hour >=12 and hour <18:
        speak("Good Afternoon Abhishek")
    else:
        speak("Good Evening Abhishek")
    speak("Abhishek, I am your assistant speed 1 Terahertz and a memory 1 Zettabyte,tell me What I can do for you Sir")


def takeCommand():
    #to take voice(microphone) input and return string
    r = speech_recognition.Recognizer() 
    with speech_recognition.Microphone() as source:
        speak("I am listening sir")
        print("I am Listening sir .....")
        r.pause_threshold = 0.5
        # bolte waqt hum do words ke beech kitna time ruk sakte hai
        audio = r.listen(source)
    try: # kyuki yaha error aa sakta hai
        print("recognizing ...")
        command = r.recognize_google(audio, language="en-in")
        print(f"you said: {command} \n")

    except Exception as e:
        # speak("say that again please")
        print("say that again please !! ...\n\n")
        return "None"
    return command 
def take_my_command(my_command):
    #to take voice(microphone) input and return string
    r = speech_recognition.Recognizer() 
    with speech_recognition.Microphone() as source:
        speak(f'{my_command}......')
        print(f"{my_command}........")
        r.pause_threshold = 0.5
        # bolte waqt hum do words ke beech kitna time ruk sakte hai
        audio = r.listen(source)
    try: # kyuki yaha error aa sakta hai
        print("recognizing ...")
        command = r.recognize_google(audio, language="en-in")
        print(f"you said: {command} \n")

    except Exception as e:
        # speak("say that again please")
        print("say that again please !! ...\n\n")
        return "None"
    return command 

def search_movie(name):
    movies_path="F:/MOVIES/"
    movies=os.listdir(movies_path)
    for mov in movies:
        mov=mov.lower()
        if name in mov:
            file_path=os.path.join(movies_path,mov)
            print('step 1')
            if os.path.isfile(file_path):
                os.startfile(file_path)
                speak(f'playing {mov}')
                
            elif os.path.isdir(file_path):
                movies_path2=os.path.join(movies_path,mov)
                movies2=os.listdir(movies_path2)
                print('step 2')
                for mov in movies2:
                    mov=mov.lower()
                    if name in mov:
                        file_path2=os.path.join(movies_path2,mov)
                        if os.path.isfile(file_path2):
                            os.startfile(file_path2)
                            speak(f'playing {mov}')
    
                        elif os.path.isdir(file_path2):
                            movies_path3=os.path.join(movies_path2,mov)
                            movies3=os.listdir(movies_path3)
                            print('step 3')
                            for mov in movies3:
                                mov=mov.lower()
                                if name in mov:
                                    file_path3=os.path.join(movies_path3,mov)
                                    if os.path.isfile(file_path3):
                                        os.startfile(file_path3)
                                        speak(f'playing {mov}')

def search_song(name):
    songs_path="C:\\Users\\Abhishek\\Music"
    songs=os.listdir(songs_path)
    for son in songs:
        son=son.lower()
        if name in son:
            file_path=os.path.join(songs_path,son)
            if os.path.isfile(file_path):
                os.startfile(file_path)
                print(f"playing {son[:15]}")
                speak(f"playing {son[:15]}")
                                                        
                                        
def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abhishekkajla2303@gmail.com','email-password')
    server.sendmail('abhishekkajla2303@gmail.com',to,content)
    server.close()

    
def facebook():
    browser.get("https://www.facebook.com/")
    email=browser.find_element_by_xpath('//*[@id="email"]')
    email.send_keys("abhishekkajla58@yahoo.com")
    password=browser.find_element_by_xpath('//*[@id="pass"]')
    pwd="fb password"
    password.send_keys(f"{pwd}")
    password.send_keys(Keys.ENTER)

if __name__ == "__main__":
#     #speak("Pranishka is a good girl")
    while True:
        command = takeCommand().lower()
        if command == "hello shakti" or command == 'shakti':
            wishme()
            command=takeCommand().lower()
        # ALL Functionality for this assistant
            if 'tell me about' in command or  'wikipedia' in command:
                speak('searching for your results sir ...')
                command = command.replace('tell me about','')# replaced extra stuff for search
                results = wikipedia.summary(command, sentences=2) #here summary is a function for searching results it takes 2 args 1st is what to  search 2nd no. of sentences to return
                speak("Sir, According to wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in command:
                speak('opening youtube for you sir')
                webbrowser.open('https://www.youtube.com')

            elif 'open google' in command:
                speak('opening google for you sir')
                webbrowser.open('https://www.google.com/')

            elif 'my github account' in command or 'open github' in command:
                speak('sure sir , just a second')
                webbrowser.open('https://github.com/abhishekkajla230')

            elif 'search on google' in command:
                speak('searching for your results sir ...')
                command = command.replace('search on google for','')# replaced extra stuff for search
                print(command)
                webbrowser.open(command)

            elif ('play music' in command) or ('play songs' in command):
                command=take_my_command("Which song do you want to play sir")
                try:
                    if 'anything' in command or 'any' in command:   
                        songs_path = 'C:\\Users\\Abhishek\\Music'#used // b/s to escape characters
                        songs = os.listdir(songs_path)
                        #print(songs) #it will list all the songs(from songs_path) in songs
                        rand_song=randint(1,len(songs)-1)
                        file_path=os.path.join(songs_path, songs[rand_song])
                        if os.path.isfile(file_path):
                            os.startfile(file_path)
                            print(f"playing...{songs[rand_song]}")
                            speak(f"playing {songs[rand_song]}")
                    elif 'favourite song' in command or 'favourite' in command:
                        songs = os.listdir(songs_path2)
                        #print(songs)
                        rand_song=randint(1,len(songs)-1)
                        file_path=os.path.join(songs_path2, songs[rand_song])
                        if os.path.isfile(file_path):
                            os.startfile(file_path)
                            print(f"playing...{songs[rand_song]}")
                            speak(f"playing {songs[rand_song]}")
                    else:
                        search_song(command)
                except Exception as e:
                    print(e)
                        

                        
                
                
            elif ('play movie' in command) or ('a movie' in command):
                name=take_my_command("Which movie do you want to play sir")
                search_movie(name)
            elif 'the time' in command:
                str_Time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir the time is {str_Time}")

            # elif 'the day' in command:
            #     str_day = datetime.datetime().day()
            elif ('open vs code' in command) or ('open visual studio' in command) or ('open visual studio code' in command):
                vscode_path="C:\\Users\\Abhishek\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"# this is its target path which is copied from its properties at file location
                os.startfile(vscode_path)
            elif 'open powershell' in command or 'open windows powershell' in command:
                # shell_path="SystemRoot\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
                shell_path='C:\\Users\\Abhishek\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell'
                os.startfile(shell_path)
            # elif 'open jupyter' in command or 'open jupyter notebook' in command:
            #     jupy_path='C:\Users\Abhishek\Anaconda3\pkgs\python-3.7.3-h8c8aaf0_0\python.exe C:\Users\Abhishek\Anaconda3\cwp.py C:\Users\Abhishek\Anaconda3 C:\Users\Abhishek\Anaconda3\python.exe C:\Users\Abhishek\Anaconda3\Scripts\jupyter-notebook-script.py "%USERPROFILE%/"
            elif 'open whatsapp' in command:
                whatsapp_path='C:\\Users\\Abhishek\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
                os.startfile(whatsapp_path)

            elif 'send email' in command:
                to_list=["abhishekkajla4313@gmail.com","rathorevishnu666@gmail.com",'akayiphone2303@icloud.com']
                try:
                    mail_to=take_my_command("who do you want to send sir").lower()
                    if mail_to == 'abhishek':
                        to=to_list[0]
                    elif mail_to == 'vishnu':
                        to=to_list[1]
                    elif mail_to == 'iphone':
                        to=to_list[2]
                    else:
                        speak(f"Nobody named {mail_to}")
                    speak("What do you want to say")
                    content= takeCommand()
                    sendEmail(to,content)
                    print('Email Sent Successfully :)')
                    speak("email sent successfully sir")
                except Exception as e:
                    print(e)
                    speak("please try again")

            elif 'send whatsapp message' in command or 'send whatsapp' in command:

                ###############################################################################################
                def whatsapp():
                    global browser
                    browser=webdriver.Chrome('C:\\Users\\Abhishek\\Desktop\\lockdown\\selenium\\chromedriver') #to open chrome browse
                    browser.get('https://web.whatsapp.com/') #to open the desired website 
                    return browser
                #############################################################################################################
                try:
                    if browser.find_element_by_class_name('_1WliW'):
                        sender()
                except:
                    whatsapp()
                    sleep(5)

                def sender():
                    if browser.find_element_by_class_name('_1WliW'):
                        #name=input("Who do you want to send :-")
                        #what=input("what do you want to say :-")
                        #times=int(input("how many times"))
                        name=take_my_command('who do you want to send ').capitalize()
                        print(name)
                        if name:
                            times=take_my_command('how many times you want to send')
                            times=times.replace('X','')
                            times=int(times)
                        if times:
                            what=take_my_command("what is your message")
                        user=browser.find_element_by_xpath(f'//span[@title ="{name}"]').click()
                        msg=browser.find_element_by_class_name('_1Plpp')

                        for var in range(times):
                            #r=randint(0,len(L7)-1)
                            msg.send_keys(what)
                            browser.find_element_by_class_name('_35EW6').click()
                try:
                    sender()

                except Exception as e:
                    print(e)
                    speak("Please Scan the Whatsapp QR code with your mobile app in next 15 seconds")
                    for var in range(15):
                        print(var,end='..')
                        sleep(1)
                    sender()

            elif 'open my facebook' in command or 'facebook account' in command:
                try:
                    facebook()
                except:
                    browser=webdriver.Chrome("C:\\Users\\Abhishek\\Desktop\\lockdown\\selenium\\chromedriver")
                    facebook()

            elif ('close browser' in command) or ('close' in command):
                try:
                    browser.close()
                except:
                    speak("Unable to close or Browser not opened")
                    print('Unable to close or Browser not opened')

        elif ("bye shakti" in command) or ("bye" in command):
            speak("Bye Sir, have a good day")
            break


            

            
