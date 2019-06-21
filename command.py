import os
import pyttsx3


engine=pyttsx3.init()
camm=input("enter the command:")
cm=camm.split()
cmd='which  '+cm+' &>output.txt'
path=os.system(cmd)
f=open('History.txt','+a')
r=open('History.txt')
txt=r.read().strip().split()
r.close()
boo=os.path.exists(path)
if boo:
    if cm in txt:
        engine.say('command daal gandu')
        engine.runAndWait()
    else:
        os.system(com)
else:
    print('command not found')

f.write(cm+"\n")
f.close()