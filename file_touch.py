'use deep analysis of file handling to create a linux command similiar to touch command'
'''basically there are two ways to create a file in linux by command
1-touch command
2-cat command
cat command-used to create the file with content
touch command-used to create the file without any content.This command used when user dont't have data to store at the time of file creation
'''
print("press 1 for create a file")
print("press 2 for creating multiples files at once")
print("press 3 for checking the modication time of time" )

choice=int(input("please enter your choice"))
if(choice==1):
    print("you choose for create file")
    print("To creste a new file : ")
    f=open('abc.txt','w+')
    show=f.read()
    print(show)

if(choice==2):
    print("you choose for creating multiple files")
    print("For Creating multiple files :")
    create_file=int(input("how many file you want to create :"))
    for i in range(create_file):
        f=open(input(),"w")
if(choice==3):
    print("you choose for modification time")
    print("for accesing the modified time of time :")
    import os.path
    import time
    f_name=input("enter the file name which you want know about its modified time :")
    modTimesinceEpoc = os.path.getmtime(f_name)
    modificationTime = time.strftime('%Y - %m - %d %H:%M:%S',time.localtime((modTimesinceEpoc)))
    print("last modication time :",modificationTime)
if(choice>3):
    print("hey,you choose the wrong option !!!")


