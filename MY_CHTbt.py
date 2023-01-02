from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from tkinter import messagebox

chatbot = ChatBot("Dr. Bot")

# Main Window
win = Tk()
win.geometry('450x680')
win.title('Doctor_Bot')

def Ask_from_bot():
   query = textF.get()
   answer_from_bot = chatbot.get_response(query)
   msgs.insert(END,'You :' + query)
   msgs.insert(END,'Bot :' + str(answer_from_bot))
   textF.delete(0,END)

def click(*args):
    textF.delete(0,END)

# Popup Message Box
def book():
    appointment = messagebox.askquestion("confirm","Are you sure? You want to book your appointment for 3 o'clock next Wednesday?")
    if appointment == 'yes':
        messagebox.showinfo('info','Your appointment is confirmed.')
        win.destroy()
    else:
        win.destroy()

def show():
    win.state(newstate='iconic')
    # Second Window
    root = Tk()
    root.geometry('300x400')
    def submit():
        messagebox.showinfo('msg','Your message is submitted!...\nOur operator will contact you soon.')
        root.destroy()
        win.destroy()

    def click1(*args):
        e1.delete(0, END)
    def click2(*args):
        e2.delete(0, END)

    l = Label(root,text='Enter your message here...',font='Elephant',pady=2)
    l.pack(pady=2)
    tx = Text(root,height=10)
    tx.pack()

    f = Frame(root)
    f.pack()
    e1 = Entry(f,font='timesnewroman')
    e1.pack(pady=4)
    e1.insert(0,'Enter your name')
    e1.bind('<Button-1>', click1)
    e2 = Entry(f,font='timesnewroman')
    e2.pack(pady=4)
    e2.insert(0,'Enter your contact number')
    e2.bind('<Button-1>', click2)

    b = Button(root,text='Submit',font='timesnewroman 10',bg='deep sky blue',fg='black',command=submit)
    b.pack(pady=10)
    root.config(bg='Navajo White')
    root.mainloop()

# Image
img = PhotoImage(file='img/doc.png')
photoL = Label(win,image=img,bg='black')
photoL.pack(pady=5)

# Icon
win.wm_iconbitmap('img/icon.ico')

# Main Window Frame
frame = Frame(win)

sc = Scrollbar(frame)
sc.pack(side=RIGHT,fill=Y)
msgs = Listbox(frame,width=80,height=20,bg='light cyan',fg='black')
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

textF = Entry(win,font='timesnewroman 15')
textF.pack(fill=X,pady=10)
textF.insert(0,'write your query here')
textF.bind('<Button-1>',click)
btn1 = Button(win,text='Ask from bot',font='aharoni 20',bg='green',fg='white',command=Ask_from_bot).pack(pady=10)

frame1 = Frame(win)
btn2 = Button(frame1,text='Book An Appointment',padx=20,pady=5,command=book)
btn2.pack(side=LEFT,pady=2,padx=3)
btn3 = Button(frame1,text='Contact Operator Directly',padx=20,pady=5,command=show)
btn3.pack(side=LEFT,pady=2,padx=3)
frame1.pack()

win.config(bg='coral')
win.mainloop()

# conversations
conversations = [
    "hello doctor bot",
    "hi I am talking from Doctor Mehta's clinic. How may I help you?",
    "I'd like to make an appointment to see Doctor Mehta, please.",
    "Have you been in to see Doctor Mehta before?",
    "Yes, I have.",
    "Fine, what is your name",
    "Namira Patel.",
    "Thank you, Miss. Namira, let me pull up your file... Okay, I've located your information. What's the reason for your making an appointment?",
    "I haven't been feeling very well lately. ",
    "Do you need urgent care?",
    "No, not necessarily, but I'd like to see the doctor soon. ",
    "Of course, how about next Monday? There's a slot available at 10 in the morning.",
    "Is there anything available after 3? ",
    "Let me see. Not on Monday, but we have a 3 o'clock opening next Wednesday. Would you like to come in then?",
    "Yes, next Wednesday at 3 would be great. ",
    "All right, Just click on Book Appointment bellow and your appointment will be scheduled for 3 o'clock next Wednesday.",
    "Thank you for your help. "
    "You're welcome. We'll see you next week. Goodbye.",
    "Goodbye."
]
trainer = ListTrainer(chatbot)
trainer.train(conversations)