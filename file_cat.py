'''Run a program that act as cat command :-
cat commmand can be used as
1-display the content of file
2-copy text into a new document
3-append the content of a text file to the end of another text file,combing them
4-
'''
option = '''
press 1 for displaying the content of file
press 2 for copy text into a new document
press 3 for append method
'''
print(option)
choice=int(input())
print("your choice is :",choice)
if(choice==1):
    print("For displaying the content of file = ")
    f=open("file",'r')
    show=f.read()
    print(show)

if(choice==2):
    print("For copy text into a new document : ")
    f1=open("newfile.txt",'w+')
    print(f1)
    for i in show:
        f1.write(i)
        f1.close()
        f1=open("newfile.txt",'r')
        show2=f1.read()
        print(show2)

if(choice==3):
    print("For append method :-")
    f=open("file",'a')
    f.write("something..")

    f=open("file",'r')
    print(f.read())
if(choice>3):
    print("sorry you choose wrong option!!!")