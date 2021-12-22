import zoomexec
import datetime
import time
import pickle
import pyautogui as pi
import gmailscrapper
def execzoom():
        #i have included comments for the legiblity of my code
        l=[]#pls enter the time as string list in HH:MM:SS format change accordingly the time
        #l=["04:28:00","04:29:00","04:30:00"]#test data
        file=open("class1.txt")
        x=file.readlines()#list var storing the meeting id and password
        print("Available ID and pwd",x)
        l3=[]#meetingid
        l4=[]#pwd
        linectr=0
        if datetime.datetime.now().strftime("%H:%M:%S")=="20:50:00":# Checks your mail at 8 :50 pm YOu can change it if you want
                gmailscrapper.gmailscrapper()
                gmailscrapper.edit()
                gmailscrapper.output()
        for i in x:
                linectr+=1
                if linectr%2==1:
                        l3.append(i[12:25])#string slicing
                else:
                        
                        l4.append(i[10:16])#pwd str slice
        print("left meeting id:",l3)
        print("left pwd:",l4)


        with open('out', 'wb') as fp:
            pickle.dump(l3, fp)#dump list var to a file 


        with open('out1', 'wb') as f:    
            pickle.dump(l4, f)#same as above

        def check():
                
                if datetime.datetime.now().strftime("%H:%M:%S")in l:
                    zoomexec.execute()#calling the method execute() from the other file
                
        for i in l:
                
                if datetime.datetime.now().strftime("%H:%M:%S")==i:
                    check()
                if datetime.datetime.now().strftime("%H:%M")=="00:11":
                        gmailscrapper.gmailscrapper()
                        gmailscrapper.edit()
                        gmailscrapper.output()

                if datetime.datetime.now().strftime("%p")=="PM":
                    
                        x=((int(i[0:2])+24)-int(datetime.datetime.now().strftime("%H")))*3600
                        y=(int(i[3:5])-int(datetime.datetime.now().strftime("%M")))*60
                        z=(int(i[6:])-int(datetime.datetime.now().strftime("%S")))
                        print("This program cant be modified into a countdown ")
                        print(x+y+z)
                        time.sleep(x+y+z)
                        check()#recursion
                elif datetime.datetime.now().strftime("%p")=="AM":
                        x=((int(i[0:2]))-int(datetime.datetime.now().strftime("%H")))*3600
                        y=(int(i[3:5])-int(datetime.datetime.now().strftime("%M")))*60
                        z=(int(i[6:])-int(datetime.datetime.now().strftime("%S")))
                        print("This program cant be modified into a countdown ")
                        print(x+y+z)
                        time.sleep(x+y+z)
                        check()#recursion
                   
                
                    
                    
        check()#failsafe



