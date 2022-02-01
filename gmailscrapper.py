'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Author:B.Ajay
Licence:Apache 2.0
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
import imaplib
def gmailscrapper():
    imap_host='imap.gmail.com'
    imap_port=993
    username="**********"#enter your mail id here
    password="**************"#enter your password
    server = imaplib.IMAP4_SSL(imap_host,imap_port)
    server.login(username,password)
    status,count=server.select('inbox')
    status,data=server.fetch \
                 (count[0],\
                  ("(UID BODY[TEXT])"))
    f=data[0][1].decode('utf8')

    x=open("email.txt","w+")
    x.write(f)
    x.seek(1844)
    read=x.read()
    x.truncate(1844)
    print(read)
    x.flush()
    x.close()
def edit():
    global line1
    q=open("email.txt","r+")
    line1=q.readlines()
    q.close()
    print(line1)
    for i in range(0,10):
        line1.pop(i)
    y=open("email1.txt","w+")
    for x in line1:
        y.write(x)
    y.flush()
    y.close()

def output():
    l=[]
    l1=[]
    l3=[]#l3 contain meeting id
    l4=[]#l4 contain password
    l5=[]
    for i, elem in enumerate(line1):
        if 'Meeting ID' in elem:
            l.append(i)
    for j, elem in enumerate(line1):
        if 'Password:' in elem:
            l1.append(j)
    print(l,l1)
    for i in l:
        l3.append(line1[i])
    for j in l1:
        l4.append(line1[j])
    print(l3,l4)
    i=0
    l5.insert(0,l3[0])
    l5.insert(2,l3[1])
    l5.insert(4,l3[2])
    l5.insert(6,l3[3])
    l5.insert(8,l3[4])
    l5.insert(1,l4[0])
    l5.insert(3,l4[1])
    l5.insert(5,l4[2])
    l5.insert(7,l4[3])
    l5.insert(9,l4[4])
            
    print(l,l1,l3,l4,l5)
    z=open("class1.txt","w+")
    for p in l5:
        z.write(p)
    z.flush()
    z.close()    

    

