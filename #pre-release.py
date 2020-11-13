from tkinter import *
import random
from tkinter import messagebox

#Setting requirments for the GUI window
Window = Tk()
Window.geometry('400x400')
Window.title("Pre-Release Quiz")

#Globalising value


#Logic behind the desing being runned
#and all the functions creation

#Getting input within range
def inputing():
    global score
    score = []
    if tpe==0:
        Submit_Button.config(text="Submit Answer")
        start_Questioning(num=1)
        Submit_Button.config(command= lambda: answer_checking(score))
    else:
        try:
            input_variable = int(Input.get())
            Interruption.config(text='')
            if input_variable>=2 and input_variable<=12:
                global num
                num = input_variable
                start_Questioning(num=num)
                Submit_Button.config(command= lambda: answer_checking(score))
                
            else:
                Interruption.config(text='Input numbers inside the given range')

        except ValueError:
            Interruption.config(text='Type a number')

#Getting input at any range
def get_input():
        try:
            user_answer = int(Input.get())
            Interruption.config(text='')
            return user_answer
        except ValueError:
            Interruption.config(text='If number not entered it is considered as zero')
            return 0

#Asking question
def start_Questioning(num, same=False):
    global num2
    if same==True:
        question = "What is "+str(num)+"x"+str(num2)+"="
        Instruction.config(text=str(question))
    else:
        if tpe==0:
            num= random.randint(2,12)
        num2 = random.randint(1,12)
        global answer
        answer = num*num2
        question = "What is "+str(num)+"x"+str(num2)+"="
        Instruction.config(text=str(question))

#Checking answer for the input given and incrementing score
global chance
chance = 0
def answer_checking(score):
    user_input = get_input()
    if answer==user_input:
        score.append(1)
        if tpe ==2:
            Interruption.config(text="WoW your answer is correct!!!")
            incorrect = False
            global chance
            chance = 0
    else:
        if tpe ==2:
            chance=chance+1
            incorrect = True
            if user_input>answer and chance<3:
                Interruption.config(text=str(name+" your answer is larger"))
            if user_input<answer and chance<3:
                Interruption.config(text=str(name+" your answer is smaller"))
            if chance>2:
                Interruption.config(text=str(name+" the correct answer is "+str(answer)))
                score.append(0)
                chance = 0
                incorrect = False
        else:
            score.append(0)

    if len(score)<no_ofquestions:
        if tpe ==0:
            start_Questioning(1)
        elif tpe==2 and incorrect:
            start_Questioning(num, same=True)

        else:
            start_Questioning(num)
    else:
        Submit_Button.pack_forget()
        displayscore(score)

#Displaying the score
def displayscore(score):
    sco=sum(score)
    Interruption.config(text="")
    Continue_Button.pack()
    Submit_Button.config(command=inputing)
    if sco>3:
        display="Congragulations "+name+" your score is "+str(sco)+" out of "+str(no_ofquestions)
        Instruction.config(text=str(display))
    else:
        display="Well tried "+name+" your score is "+str(sco)+" out of "+str(no_ofquestions)
        Instruction.config(text=str(display))

def start(Type):
    #Making the first desing invisible
    try:
        if Type!=2:
            global no_ofquestions
            no_ofquestions = int(Numberofquestions.get())
        else:
            no_ofquestions = 5
        Text1.pack_forget()
        Text2.pack_forget()
        global name
        name = NameEntry.get()
        NameEntry.pack_forget()
        Testingmixed_Button.pack_forget()
        TestingWmixed_Button.pack_forget()
        Learning_Button.pack_forget()
        Text3.pack_forget()
        Numberofquestions.pack_forget()

        global tpe
        tpe = Type

        #Initialysing the design GUI
        if Type==0:
            Instruction.config(text='')
            Submit_Button.config(text='Start')
            inputing()

        Instruction.pack(pady=10)
        Input.pack(pady=25)   
        Submit_Button.pack()
        Interruption.pack(pady=25)
    except:
        messagebox.showerror("Input numbers", "Please input numbers in the number of questions box")
        
def restart():
    Instruction.config(text="Enter your choice of multilication")
    Instruction.pack_forget()
    Input.pack_forget()
    Submit_Button.pack_forget()
    Interruption.pack_forget()

    Text1.pack(pady=10)
    NameEntry.pack()
    Text3.pack(pady=3)
    Numberofquestions.pack()
    Text2.pack(pady=15)
    Testingmixed_Button.pack()
    TestingWmixed_Button.pack()
    Learning_Button.pack()

    Continue_Button.pack_forget()

Quit_Button = Button(Window, text="Quit", command=quit).pack(ipadx=400)

Instruction = Label(Window, text='')
Instruction.config(text="Enter your choice of multilication")

Input = Entry(Window)
Input.focus()

Text1 = Label(Window, text="Enter Your Name:")
Text1.pack(pady=10)

NameEntry = Entry(Window)
NameEntry.pack()

Text3= Label(Window, text="How many questions do you want (Optinal only if choosing Testing)")
Text3.pack(pady=3)

Numberofquestions = Entry(Window)
Numberofquestions.pack()

Submit_Button = Button(Window, text="Submit Answer", command= inputing)

Interruption = Label(Window, text='')

Text2 = Label(Window, text="Choose what you want:")
Text2.pack(pady=15)

Testingmixed_Button = Button(Window, text="Testing with mixed set", command=lambda: start(0))
Testingmixed_Button.pack()

TestingWmixed_Button = Button(Window, text="Testing without mixed set", command=lambda: start(1) )
TestingWmixed_Button.pack()

Learning_Button = Button(Window, text="Learning", command= lambda: start(2))
Learning_Button.pack()

Continue_Button = Button(Window, text="Do you wish to continue", command=restart)

#Running the desing created
Window.mainloop()