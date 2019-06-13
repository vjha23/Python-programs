import datetime
name=input("enter the name please : ")
now=datetime.datetime.now()
if now.hour>5 and now.hour<12:
    print("Good Morning.. ",name)
elif now.hour>12 and now.hour<18:
    print("Good Afternoon",name)
elif now.hour>18 and now.hour<21:
    print("Good Night",name)
elif now.hour>=21:
    print("Good night",name)