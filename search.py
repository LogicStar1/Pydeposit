from tkinter import*
from tkinter import ttk
import webbrowser
import speech_recognition as sr

root=Tk()
root.title("My search app")
label=ttk.Label(root,text="Query:")
label.grid(row=0,column=0)
temp=StringVar()
btn2=StringVar()

entry1=ttk.Entry(root,width=100,textvariable=temp)
entry1.grid(row=0,column=1,columnspan=4)


photo=PhotoImage(file="micro.png").subsample(130,130)

def callback():
	if btn2.get()=='google':
		webbrowser.open("http://google.com/search?q="+entry1.get())
	elif btn2.get=='YouTube':
		webbrowser.open("http://www.youtube.com/search?q="+entry1.get())

def get(event):
	if btn2.get()=='google':
		webbrowser.open("http://google.com/search?q="+entry1.get())
	elif btn2.get=='YouTube':
		webbrowser.open("http://www.youtube.com/search?q="+entry1.get())


def buttonclick():
        r=sr.Recognizer()

        with sr.Microphone() as source:
                print("dddd")
                temp.set("say something!:")
                audio=r.listen(source,timeout=5)
                
            
        try:
                a=r.recognize_google(audio)
                temp.set(a)
        except sr.UnknownValueError:
                temp.set("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
                temp.set("Could not request results from Google Speech Recognition service; {0}".format(e))

        

entry1.bind('<Return>',get)


mybutton1=Button(root,text="Search",command=callback)
mybutton1.grid(row=0,column=6)
buttonS=Button(root,text='listen',command=buttonclick).grid(row=1,column=0)

mybutton2=ttk.Radiobutton(root,text="Google",value="google",variable=btn2)
mybutton2.grid(row=1,column=1,sticky=W)

mybutton3=ttk.Radiobutton(root,text="YouTube",value="YouTube",variable=btn2)
mybutton3.grid(row=1,column=1,sticky=E)



mybutton4=Button(root,image=photo,command=buttonclick,bd=0,overrelief='groove',relief='sunken')
mybutton4.grid(row=0,column=5)


entry1.focus()
root.mainloop()
