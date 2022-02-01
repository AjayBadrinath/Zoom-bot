'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Author:B.Ajay
Licence:Apache 2.0
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
from pywinauto import application
import pyautogui as pi
import time
import datetime
import pickle

with open ('out', 'rb') as fp:
    user = pickle.load(fp)
with open ('out1', 'rb') as kp:
    pwd = pickle.load(kp)
user1,pwd1=user,pwd
print(user1,pwd1)#list of user id and pwd available
def execute():
        
        app=application.Application()
        app.start(r"C:\Users\Admin\AppData\Roaming\Zoom\bin\zoom.exe")# instead of Admin enter your user id or copy zoom path
        time.sleep(2)
        pi.click(pi.locateCenterOnScreen('1.png'))
        time.sleep(2)
        pi.click(649,325)
        
        time.sleep(2)
        pi.typewrite(user1[0])#0 index because we need the first element of the list as we are popping the list value as soon as it is entered
        user.pop(0)
        time.sleep(2)
        pi.click(649,380)
        time.sleep(2)
        pi.doubleClick()
        pi.hotkey('ctrl', 'a')
        time.sleep(2)
        pi.typewrite("Admin")#fill the name if not filled
        time.sleep(2)
        pi.click(530,450)
        time.sleep(2)
        pi.click(530, 480)
        time.sleep(2)
        pi.click(pi.locateCenterOnScreen('2.png'))
        time.sleep(2)
        pi.typewrite(pwd1[0])#same reason
        pwd.pop(0)
        pi.click(pi.locateCenterOnScreen('3.png'))

