from tkinter import *
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import requests
import pygame

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am your virtual assistant Eva. Please tell me How can I help you")

#It takes microphone input from the user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

pygame.mixer.init()

def stop():
    pygame.mixer.music.stop()

def clicked():

    if __name__ == "__main__":

        wishme()
        while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                        speak("Searching Wikipedia...")
                        query = query.replace("wikipedia","")
                        results = wikipedia.summary(query, sentences = 2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)

            elif 'open youtube' in query:
                speak(f"You said {query}")
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak(f"You said {query}")
                webbrowser.open("google.com")

# time
            elif 'time' in query:
                speak(f"You said {query}")
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)                        
                speak(f"The time is: {strTime}")

# name
            elif 'what is your name' in query:
                speak("My name is Eva, How can I help you?")
 
#  lectures
            elif 'lecture' in query:
                lecture = "Maths lecture at 4 pm. Science lecture at 5 pm. Physics lecture at 10 am and Chemistry lecture at 11 am"
                speak(f"Yes there is a {lecture}")
            
# notice board
            elif 'notice' in query:
                speak('''All students are hereby informed that their exams are starting from Monday. 
                        The reporting time for the candidates is 11:45 am.You will be provided with your necessary stuffs requird for the exams''')
            
# exam time table
            elif 'exam schedule' in query:
                speak('''The first paper is english on 14 march 2022 that is Monday. At 12 pm to 2 pm in classroom 305. 
                        The second paper is Maths on 16 march 2022 that is Wednesday. At 12 pm to 2 pm in classroom 300.
                        The third paper is physics on 18 march 2022 that is Friday. At 12 pm to 2 pm in classroom 208.
                        The fourth paper is Chemistry on 21 march 2022 that is Monday. At 12 pm to 2 pm in classroom 210.''')
            
            elif 'which paper is on monday' in query:
                speak("English paper")

            elif 'which paper is on wednesday' in query:
                speak("Maths paper")

            elif 'which paper is on friday' in query:
                speak("Physics paper")
            
            elif 'which paper is on saturday' in query:
                speak("Chemistry paper")

# location
            elif 'location' in query:
                r = requests.get('https://get.geojs.io/')

                ip_request = requests.get('https://get.geojs.io/v1/ip.json')
                ipAdd = ip_request.json()['ip']


                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_req = requests.get(url)

                geo_data = geo_req.json()

                speak(f"Your location is {geo_data['city'],geo_data['country']}")
            
#city
            elif 'my city' in query:
                r = requests.get('https://get.geojs.io/')

                ip_request = requests.get('https://get.geojs.io/v1/ip.json')
                ipAdd = ip_request.json()['ip']


                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_req = requests.get(url)

                geo_data = geo_req.json()

                speak(f"Your City is {geo_data['city']}")
            
# state
            elif 'my state' in query:
                r = requests.get('https://get.geojs.io/')

                ip_request = requests.get('https://get.geojs.io/v1/ip.json')
                ipAdd = ip_request.json()['ip']


                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_req = requests.get(url)

                geo_data = geo_req.json()

                speak(f"Your State is {geo_data['region']}")
            
# country
            elif 'my country' in query:
                r = requests.get('https://get.geojs.io/')

                ip_request = requests.get('https://get.geojs.io/v1/ip.json')
                ipAdd = ip_request.json()['ip']


                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_req = requests.get(url)

                geo_data = geo_req.json()

                speak(f"Your country is {geo_data['country']}")
            
# lecture 1
            elif 'play firebase' in query:
                speak("Playing firebase")
                # song = "C:\MyComputer\Virtual Assistant\Ye tune kya kiya.mp3"
                pygame.mixer.music.load("C:\MyComputer\Virtual Assistant\lectures\Fire base.mp3")
                pygame.mixer.music.play(loops=0)
                # playsound('Ye tune kya kiya.mp3')
                if 'stop' in query:
                    speak("you said stop")
                    pygame.mixer.music.stop()
            
# lecture 2
            elif 'play data structure' in query:
                speak("Playing data structure")
                # song = "C:\MyComputer\Virtual Assistant\Ye tune kya kiya.mp3"
                pygame.mixer.music.load("C:\MyComputer\Virtual Assistant\lectures\data structure.mp3")
                pygame.mixer.music.play(loops=0)
                # playsound('Ye tune kya kiya.mp3')
                if 'stop' in query:
                    speak("you said stop")
                    pygame.mixer.music.stop()

# lecture 3
            elif 'play javascript' in query:
                speak("Playing javascript")
                # song = "C:\MyComputer\Virtual Assistant\Ye tune kya kiya.mp3"
                pygame.mixer.music.load("C:\MyComputer\Virtual Assistant\lectures\javascript.mp3")
                pygame.mixer.music.play(loops=0)
                # playsound('Ye tune kya kiya.mp3')
                if 'stop' in query:
                    speak("you said stop")
                    pygame.mixer.music.stop()

# end
            elif 'quit' in query:
                speak(f"You said {query}")
                speak("Thank You!")
                print("Thank you!")

                exit()

root = Tk()

root.title('Virtual Assistant')
root.geometry('500x300')

l_text = Label(root, text="Speech Recognition", font="times 25 bold", padx=25,pady=30, fg="blue")
l_text.place(x=580,y=0)

btn1 = Button(root, text='Allow access to microphone', font="times 15 bold", bg='green', fg='white', padx=10, pady=10, command=clicked)
btn1.place(x=610,y=100)



# btn2 = Button(root, text='Close', font="times 15 bold", bg='red', fg='black', padx=5, pady=8, command=root.destroy)
# btn2.pack()

Label(root, text="Lectures:", font="times 30 bold", fg="black").place(x=10, y=200)
Label(root,text="1. Maths lecture at 8 am", font="times 18 ").place(x=10, y=250)
Label(root,text="2. Science lecture at 9 am", font="times 18 ").place(x=10, y=300)
Label(root,text="3. Physics lecture at 10 am", font="times 18 ").place(x=10, y=350)
Label(root,text="4. Chemistry lecture at 11 am", font="times 18 ").place(x=10, y=400)

# Table
Label(root, text="Time Table", font="times 30 bold", fg="black").place(x=1000, y=200)

Label(root, text="Sr. No.", font="times 20 bold", fg="black").place(x=700, y=250)
Label(root, text="Subject", font="times 20 bold", fg="black").place(x=830, y=250)
Label(root, text="Date", font="times 20 bold", fg="black").place(x=980, y=250)
Label(root, text="Day", font="times 20 bold", fg="black").place(x=1100, y=250)
Label(root, text="Time", font="times 20 bold", fg="black").place(x=1220, y=250)
Label(root, text="Classroom No.", font="times 20 bold", fg="black").place(x=1320, y=250)

# sr. no
Label(root, text="1", font="times 15", fg="black").place(x=750, y=300)
Label(root, text="2", font="times 15", fg="black").place(x=750, y=350)
Label(root, text="3", font="times 15", fg="black").place(x=750, y=400)
Label(root, text="4", font="times 15", fg="black").place(x=750, y=450)


#  subjects
Label(root, text="English", font="times 15", fg="black").place(x=850, y=300)
Label(root, text="Maths", font="times 15", fg="black").place(x=850, y=350)
Label(root, text="Physics", font="times 15", fg="black").place(x=850, y=400)
Label(root, text="Chemistry", font="times 15", fg="black").place(x=850, y=450)

# Dates
Label(root, text="14/03/2022", font="times 15", fg="black").place(x=970, y=300)
Label(root, text="16/03/2022", font="times 15", fg="black").place(x=970, y=350)
Label(root, text="18/03/2022", font="times 15", fg="black").place(x=970, y=400)
Label(root, text="21/03/2022", font="times 15", fg="black").place(x=970, y=450)

# Days
Label(root, text="Monday", font="times 15", fg="black").place(x=1100, y=300)
Label(root, text="Wednesday", font="times 15", fg="black").place(x=1100, y=350)
Label(root, text="Friday", font="times 15", fg="black").place(x=1100, y=400)
Label(root, text="Saturday", font="times 15", fg="black").place(x=1100, y=450)

# time
Label(root, text="12-2 pm", font="times 15", fg="black").place(x=1220, y=300)
Label(root, text="12-2 pm", font="times 15", fg="black").place(x=1220, y=350)
Label(root, text="12-2 pm", font="times 15", fg="black").place(x=1220, y=400)
Label(root, text="12-2 pm", font="times 15", fg="black").place(x=1220, y=450)

# classroom
Label(root, text="305", font="times 15", fg="black").place(x=1400, y=300)
Label(root, text="300", font="times 15", fg="black").place(x=1400, y=350)
Label(root, text="208", font="times 15", fg="black").place(x=1400, y=400)
Label(root, text="210", font="times 15", fg="black").place(x=1400, y=450)

# Notice
Label(root, text="Notice:", font="times 25 bold", fg="black").place(x=10, y=500)
Label(root, text="All students are hereby informed that their exams are starting from Monday.", font="times 15 ", fg="black").place(x=10, y=550)
Label(root, text="The reporting time for the candidates is 11:45 am.", font="times 15 ", fg="black").place(x=10, y=580)
Label(root, text="You will be provided with your necessary stuffs requird for the exams", font="times 15 ", fg="black").place(x=10, y=610)

# recording
Label(root, text="My Documents", font="times 25 bold", fg="black").place(x=1000, y=500)
Label(root, text="1. Firebase lecture recording", font="times 15 ", fg="black").place(x=1000, y=550)
Label(root, text="2. Javascript lecture recording", font="times 15 ", fg="black").place(x=1000, y=600)
Label(root, text="3. Data structure lecture recording", font="times 15 ", fg="black").place(x=1000, y=650)

btn2 = Button(root, text="Stop", font="times 15 bold", bg='black', fg='white', padx=10, pady=10, command=stop)
btn2.place(x=1000,y=700)


root.mainloop()
        






