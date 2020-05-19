from django.shortcuts import render
import requests
import pyttsx3
import bs4
import urllib.request as req


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',180)
def male(audio):
   engine.setProperty('voice',voices[0].id)
   engine.say(audio)
   engine.runAndWait()
   return -1

def female(audio):
   engine.setProperty('voice',voices[1].id)
   engine.say(audio)
   engine.runAndWait()
   return -1
   


def button(request):
    return render(request,'home.html')
  


      


def output(request):
    
    
    import speech_recognition as sr
    import bs4
    import urllib.request as req
    #------------- to speak
    import win32com.client 
  

    speaker = win32com.client.Dispatch("SAPI.SpVoice") 
  
    print("Enter the word you want to speak it out by computer") 
    s = "hello" 
    speaker.Speak(s) 
	

#-------------to listen

    def rect():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Please Speak")     
            s = "Please Speak" 
            speaker.Speak(s) 
            r.pause_threshold=1 
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            print("Analyzing ...") 
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                s = "You said : {}".format(text) 
                speaker.Speak(s) 
                return text
            except:
                print("Sorry could not recognize what you said")
                s = "Sorry could not recognize what you said"
                speaker.Speak(s) 
                rect()

#-------------------news
#----------------------
    def Trendingshots():
        htp = req.urlopen("https://www.indiatoday.in")
        page = bs4.BeautifulSoup(htp, features="html.parser")
        a = page.find_all("div", class_="featured-post")
    
        
        s = "Today's top headlines"
        speaker.Speak(s) 

        for i in range(len(a)):
            print(a[i].text, "\n")
            female(a[i].text)
        
        s = "do you want to repeat again say yes or no"
        speaker.Speak(s) 
        a="yes"
        if(a== rect()):
             Trendingshots()
        else:
            start()
         

#--------------------------

    def descnews():
        htp = req.urlopen("https://www.indiatoday.in")
        page = bs4.BeautifulSoup(htp, features="html.parser")
        b = page.find_all("div", class_="widget-wrapper section_wise_order")

        print("\n\nCATEGORIES:\n ")
        
        
        s = "FOLLOWING ARE THE MAJOR CATEGORIES" 
        speaker.Speak(s) 

        x = ['1','2','3','4','5']


        for i in range(len(x)):
            c = b[i].find("span", class_="widget-title")
            print("   {}".format(x[i]), c.text, end="\n")
            
            
            s = "   {}".format(x[i])
            speaker.Speak(s) 
            female("   {}".f)
            s = "   {}".format(c.text)
            speaker.Speak(s) 



        
        s = "Speak THE CATEGORY OF NEWS YOU WANT TO EXPLORE " 
        speaker.Speak(s) 
   # choice = int(input("\n\nSpeak THE CATEGORY OF NEWS YOU WANT TO EXPLORE:"))
        ff = rect()
    
        # ff = int(rect())
        print(ff) 
    
        if int(ff) > 6:
            descnews()
        else:
        
            a = page.find_all("div", class_="widget-wrapper section_wise_order")
        
            b = a[int(ff) - 1].find_all("p")
            c = a[int(ff) - 1].find("h3")
            print()
            s =c.text 
            speaker.Speak(s) 
            
            for i in range(len(b)):
                print("\n\n", b[i].text, ".")
                s = b[i].text
                speaker.Speak(s) 
                
    
    #print("NOT A GOOD INTERNET CONNECTION:")
        s = "Speak yes to continue or no to not speak no:"
        speaker.Speak(s)  
        print()
        flag=rect()
        if flag == "yes" or flag == "YES":
            descnews()
        else:
            s = "do you want to repeat again say yes or no"
            speaker.Speak(s) 
            
            a = "yes"
            if(a == rect()):
                descnews()
            else:
                start()
 
#   while True:
#     female("Speak yes to continue or no to not speak no: ") 
#     print("\n\nSpeak yes to continue or no to not speak no:")
#     flag=rect()
#     if flag == "yes" or flag == "YES":
#         descnews()
#     else:
#         print("THANK YOU. HAVE A NICE DAY")
#         female("THANK YOU. HAVE A NICE DAY")
#         break

#--------------------------------

    print("Welcome")
    s = "Welcome"
    speaker.Speak(s) 
    
    def start():
        s =" Do you want to listen to todays top  news. Say yes or no"
        speaker.Speak(s) 
    
      
        a="yes"
        if(rect()== a):
            Trendingshots()
        else:
            #female("Do you want to listen to categorywise news. say yes or no")
            a="yes"
            if(rect()== a):
                descnews()
            else:
                s = "Do you want to repeat the menu of choices or exit. say yes to repeat or no to exit"
                speaker.Speak(s) 
    
                   # female()
                a="yes"

                if(rect()== a):
                    start() 
                else:
                    s = "THANK YOU. HAVE A NICE DAY"
                    speaker.Speak(s) 
    
                    print("THANK YOU. HAVE A NICE DAY")
                   # female("THANK YOU. HAVE A NICE DAY")
                    exit()
    start()





    