from gtts import gTTS
from playsound import playsound
from pytchat import LiveChat
import os
from google_trans_new import google_translator
translator = google_translator()
import keyboard
import threading
import time


"""
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 110)
voices = engine.getProperty('voices')
for v in voices:
    print("id %s " %v.id)
engine.setProperty('voice', voices[1].id)
"""
waitt=0
flag=0
paused=0
def pause():
    global flag
    global th
    global waitt
    global paused
    while True:
        try:
            if keyboard.is_pressed('{'):
                flag=1
                print('Paused voice')
                text_val="Daksh Voice is paused"
                text_val = translator.translate(text_val,lang_src='en',lang_tgt='en')
                language = 'hi'
                obj = gTTS(text=text_val,tld='co.in', lang=language, slow=False)
                while(waitt==1):
                    yy=5
                waitt=1
                playsound("starting.mp3")
                os.remove("test.mp3")
                obj.save("test.mp3")
                playsound("test.mp3")
                waitt=0
                
                #time.sleep(2)

            if keyboard.is_pressed('('):
                paused=1
                print('BOT Paused')
                text_val="Daksh BOT is paused"
                text_val = translator.translate(text_val,lang_src='en',lang_tgt='e')
                language = 'hi'
                obj = gTTS(text=text_val,tld='co.in', lang=language, slow=False)
                while(waitt==1):
                    yy=5
                waitt=1
                playsound("starting.mp3")
                os.remove("test.mp3")
                obj.save("test.mp3")
                playsound("test.mp3")
                waitt=0

            if keyboard.is_pressed(')'):
                paused=0
                print('BOT Resumed')
                text_val="Daksh BOT is working"
                text_val = translator.translate(text_val,lang_src='en',lang_tgt='en')
                language = 'hi'
                obj = gTTS(text=text_val,tld='co.in', lang=language, slow=False)
                while(waitt==1):
                    yy=5
                waitt=1
                playsound("starting.mp3")
                os.remove("test.mp3")
                obj.save("test.mp3")
                playsound("test.mp3")
                waitt=0
                
                #time.sleep(2)
                
            if keyboard.is_pressed('}'):
                flag=0
                print("Resumed voice")
                text_val="Daksh Voice is working"
                text_val = translator.translate(text_val,lang_src='en',lang_tgt='en')
                language = 'hi'
                obj = gTTS(text=text_val,tld='co.in', lang=language, slow=False)
                while(waitt==1):
                    yy=5
                waitt=1
                playsound("starting.mp3")
                os.remove("test.mp3")
                obj.save("test.mp3")
                playsound("test.mp3")
                waitt=0
                
                #time.sleep(2)
        except:
            yy=5
        finally:
            time.sleep(1)

idd=str(input("Enter youtube ID: "))
livechat=LiveChat(video_id=idd)
th = threading.Thread(target=pause)
th.start()
bf=0
def fun():
    global bf
    global waitt
    try:
        while livechat.is_alive():
            try:
                while(paused==1):
                    yy=5
                chatdata=livechat.get()
                for c in chatdata.items:
                    bf=0
                    block = open("Blocklist.txt", "r")
                    blocklist=block.readlines()
                    blocklist = [xx.strip() for xx in blocklist] 
                    #print(blocklist)
                    for linee in blocklist:
                        if (linee==str(c.author.name)):
                            print("Message ignored because of Blacklist")
                            chatdata.tick()
                            bf=1
                            break
                    block.close()

                            
                        
                    c.datetime
                    text_val = f"{c.author.name} said,{c.message}"
                    text_val2=f"{c.datetime}: {c.author.name} !!said!!, {c.message}"
                    print(text_val2)
                    if(bf==1):
                        bf=0
                        continue
                    
                    if(flag==0):
                        #text_val=""
                        try:
                            text_val = translator.translate(text_val,lang_src='en',lang_tgt='en')
                            #print(text_val)
                            pass
                        except Exception as e:
                            try:
                                text_val = translator.translate(text_val,lang_src='en',lang_tgt='en')
                                pass
                            except Exception as e:
                                continue
                        #print('sss')
                        language = 'hi'
                        i=1
                        ddict={}
                        etemp=""
                        eflag=0
                        while(i<len(text_val)):
                            if not((ord(text_val[i])>=48 and ord(text_val[i]) <=57) or (ord(text_val[i])>=65 and ord(text_val[i])<=90) or (ord(text_val[i])>=97 and ord(text_val[i])<=122)):
                                if(text_val[i-1]==text_val[i]):
                                    text_val=text_val[:i-1]+text_val[i:]
                                    i=i-1
                            if(text_val[i]==':' and eflag==0):
                                eflag=1
                            elif(text_val[i]==':' and eflag==1):
                                eflag=0
                                ddict[etemp]=i
                                etemp=""
                            if(eflag==1 and text_val[i]!=':'):
                                etemp=etemp+text_val[i]
                            
                            i=i+1
                            pass
                        #print(ddict)
                        for i in ddict.keys():
                            print(i)
                            text_val=text_val.replace(i,"emoji")
                        text_val=text_val.replace(":"," ")
                        print(text_val)
                        obj=None
                        try:
                            obj = gTTS(text=text_val,tld='co.in', lang=language, slow=False)
                            pass
                        except Exception as e:
                            try:
                                obj = gTTS(text=text_val,tld='co.in', lang=language, slow=False)
                                pass
                            except Exception as e:
                                continue
                        while(waitt==1):
                            yy=5
                        waitt=1
                        
                        #playsound("starting.mp3")
                        os.remove("test.mp3")
                        
                        obj.save("test.mp3")
                        playsound('D:/personal/python-youtubechat-master/test.mp3')
                        waitt=0
                        if(str(c.message).lower()=="hi" or str(c.message).lower()=="hello"):
                            text_val=f"Hello {c.author.name}, Daksh welcomes you to stream"
                            print(text_val)
                            text_val = translator.translate(text_val,lang_src='hi',lang_tgt='hi')
                            obj = gTTS(text=text_val,tld='co.in', lang=language, slow=False)
                            while(waitt==1):
                                yy=5
                            waitt=1
                            playsound("starting.mp3")
                            os.remove("test.mp3")
                            obj.save("test.mp3")
                            playsound("test.mp3")
                            waitt=0
                    
                    ##engine.say(text_val)
                    # play the speech
                    ##engine.runAndWait()
                    chatdata.tick()
            except Exception as e:
                print(e)
    except Exception as e:
        fun()
fun()
