#IMPORTING DESIRED LIBRARIES
import speech_recognition as sr
import pyttsx3 as py
import webbrowser as web
import pyautogui as p


#DIFINING CERTAIN FUNCTIONS
def say(sound):   #DEFINING A FUNCTION FOR BOT's VOICE
  engine.setProperty('rate',150)
  engine.say(sound)
  engine.runAndWait()
  
def tc():   #DEFINING A FUNCTION TO TAKE AUDIO COMMANDS
  r = sr.Recognizer()
  with  sr.Microphone() as source:
    say('LISTENING...')
    print('LISTENING...')
    audio = r.listen(source)
  try:
    print('RECOGNIZING...')
    response = r.recognize(audio)
    
    return response.lower()
  except Exception as UnknownValueError:
    say('found some problems in mic....try reinstalling and reestablishing your audio input device')
    print('found some problems in mic....try reinstalling and reestablishing your audio input device')
    response = ""
    return response
def wb(w):
  web.open(web)

#CREATING THE PROGRAM USING DEFINED AND IN-BUILT FUNCTIONS
engine = py.init()

say('HELLO SIR..I AM YOUR WEB ASSISTANT....say any website name to open it...and say close or exit or bye to terminate the program')

for i in range(1,10000):
  q = tc()
  if 'google' in q:
    say('okay...opening google')
    wb('https://google.com')

  elif 'youtube' in q:
    say('okay opening youtube')
    wb('https://youtube.com')
  elif 'gmail' in q:
    say('okay...opening gmail')
    wb('https://gmail.com')
  elif 'meet' in q or 'google meet' in q:
    say('okay..opening google meet')
    wb('http://meet.google.com')
  elif 'whatsapp' in q:
    say('okay...opening whatsapp')
    wb('https://web.whatsapp.com')
  elif 'facebook' in q:
    say('okay..opening facebook')
    wb('https://facebook.com')
  elif 'instagram' in q:
    ('okay... opening instagram')
    wb('https://instagram.com')
  elif 'javatpoint' in q:
    say('okay... opening javatpoint')
    wb('https://javatpoint.com')
  elif 'geek for geeks' in q:
    say('okay..opening geekforgeeks website')
    wb('https://geekforgeeks.com')
  elif 'copy assignment' in q:
    say('okay opening copy assignment.com')
    wb('https://copyassignment.com')
  elif 'yahoo' in q:
    say('okay..opening yahoo mail')
    wb('https://mail.yahoo.com')
  elif 'maps' in q:
    say('okay... opening google maps')
    wb('https://maps.google.com')
  elif 'dino' in q:
    say('okay... opening dino')
    wb('chrome://dino')
  elif 'chrome downloads' in q:
    say('okay..showing your chrome downloads')
    wb('chrome://downloads')
  elif 'zoom' in q:
    say('okay..opening zoom website')
    wb('https://zoom.us')
  elif 'exit' or 'close' or 'bye' in q:
    say('thank you sir! see you soon')
    say('program terminated')
    break
  else:
    say('i am not getting it...are you talking about any website?')
    q1 = input('ENTER (y/n):')
    if q1=='y':
      say('please type your website name')
      as = p.prompt('ENTER YOUR WEBSITE NAME HERE:{dont use https or .com etc}')
      ww = 'https://'+as+'.com'
      wb(ww)
     else:
      continue
exit()
  

  
