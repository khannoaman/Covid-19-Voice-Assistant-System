from Methods import *
from tkinter import *
from tkinter import messagebox
import os
import threading


class ChatInterface(Frame):

    def __init__(self, master=None):


        Frame.__init__(self, master)
        self.status=True
        self.master = master

        # sets default bg for top level windows
        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"
        self.font = "Verdana 10"

        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)
        # Menu bar

        # File
        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
        #file.add_command(label="Save Chat Log", command=self.save_chat)
        file.add_command(label="Clear Chat", command=self.clear_chat)
        file.add_command(label="Exit", command=self.chatexit)

        # Options
        options = Menu(menu, tearoff=0)
        menu.add_cascade(label="Options", menu=options)

        # font
        font = Menu(options, tearoff=0)
        options.add_cascade(label="Font", menu=font)
        font.add_command(label="Default", command=self.font_change_default)
        font.add_command(label="Times", command=self.font_change_times)
        font.add_command(label="System", command=self.font_change_system)
        font.add_command(label="Helvetica", command=self.font_change_helvetica)
        font.add_command(label="Fixedsys", command=self.font_change_fixedsys)

        # color theme
        color_theme = Menu(options, tearoff=0)
        options.add_cascade(label="Color Theme", menu=color_theme)
        color_theme.add_command(label="Default", command=self.color_theme_default)
        color_theme.add_command(label="Night",command=self.color_theme_dark)
        color_theme.add_command(label="Grey", command=self.color_theme_grey)
        color_theme.add_command(label="Blue", command=self.color_theme_dark_blue)
        color_theme.add_command(label="Torque", command=self.color_theme_turquoise)
        color_theme.add_command(label="Hacker", command=self.color_theme_hacker)


        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)
        # help_option.add_command(label="Features", command=self.features_msg)
        help_option.add_command(label="About Covid-19 Voice Assistant", command=self.msg)
        help_option.add_command(label="Develpoer", command=self.about)

        #Text Frame
        self.text_frame = Frame(self.master, bd=6)
        self.text_frame.pack(expand=True, fill=BOTH)

        # scrollbar for text box
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # contains messages
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)


        # frame containing buttons
        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH)

        #Left Side Buttons

        self.send_button1 = Button(self.send_button_frame,  text="World Map", width=14, relief=RIDGE,
                                  bg='#EEEEEE',
                                  bd=1, command=CountryMap.run, activebackground="#FFFFFF",
                                  activeforeground="#000000")
        self.send_button1.pack(side=LEFT, ipady=3,padx=5, pady=5)



        self.send_button2 = Button(self.send_button_frame, text="Myth Buster", width=15, relief=RIDGE,
                                   bg='#EEEEEE',
                                   bd=1, command=MythBuster.run, activebackground="#FFFFFF",
                                   activeforeground="#000000")
        self.send_button2.pack(side=LEFT, ipady=3,padx=5, pady=5)


        self.send_button3 = Button(self.send_button_frame, text="Symptoms", width=14, relief=RIDGE,
                                   bg='#EEEEEE',
                                   bd=1, command=Symptoms.run, activebackground="#FFFFFF",
                                   activeforeground="#000000")
        self.send_button3.pack(side=LEFT, ipady=3,padx=5, pady=5)


        #Center button

        self.loadimage = PhotoImage(file="micon.png")
        self.send_button = Button(self.send_button_frame, image=self.loadimage,text="Send", width=50, relief=GROOVE, bg='#EEEEEE',
                                  bd=0, command=self.state, activebackground="#EEEEEE",
                                  activeforeground="#000000")
        self.send_button.pack(side=LEFT, ipady=5,padx=5, pady=5)
        self.master.bind("<Return>", self.state)
        self.master.bind("<Escape>", self.chatexit)


        #RIGHT Button

        self.send_button4 = Button(self.send_button_frame, text="Spread & Prevention", width=16, relief=RIDGE,
                                   bg='#EEEEEE',
                                   bd=1, command=SpreadPrevention.run, activebackground="#FFFFFF",
                                   activeforeground="#000000")
        self.send_button4.pack(side=LEFT, ipady=3,padx=5, pady=5)


        self.send_button5 = Button(self.send_button_frame, text="Do's & Don'ts", width=15, relief=RIDGE,
                                   bg='#EEEEEE',
                                   bd=1, command=DoDont.run, activebackground="#FFFFFF",
                                   activeforeground="#000000")
        self.send_button5.pack(side=LEFT, ipady=3,padx=5, pady=5)


        self.send_button6 = Button(self.send_button_frame, text="India Map", width=15, relief=RIDGE,
                                   bg='#EEEEEE',
                                   bd=1, command=StateMap.run, activebackground="#FFFFFF",
                                   activeforeground="#000000")
        self.send_button6.pack(side=LEFT, ipady=3,padx=5, pady=5)

        self.sent_label = Label(self.text_box, font="Verdana 7", padx=10, text="Starting", bg=self.tl_bg2, fg=self.tl_fg)
        self.sent_label.pack(side=BOTTOM, fill=None, padx=5)



    def last_sent_label(self, txt):

        try:
            self.sent_label.destroy()
        except AttributeError:
            pass

        self.sent_label = Label(self.text_box, font="Verdana 7",padx=10, text=txt, bg=self.tl_bg2, fg=self.tl_fg)
        self.sent_label.pack(side=BOTTOM, fill=None, padx=5)

    def clear_chat(self):
        self.text_box.config(state=NORMAL)
        self.text_box.delete(1.0, END)
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

    def chatexit(self,key=None):
        self.master.destroy()


    def msg(self):
        messagebox.showinfo("Covid-19 Voice Assistant System",
                            '''Covid-19 Voice Assistant System\n\nIt is a voice assistant system which aware people about covid-19. Since there is no treatment available for covid-19 till now so in order to avoid getting affected by this disease, we have to take all necessary precautions. For that everyone should be aware about this disease.So, this application will help for that purpose.
This application will recognise user voice commands about covid-19 and based on that command it will repond.Incase if anyone don't want to use voice commands they can use buttons which are provided.
It have Following features:

-It can be used to know about coronavirus.
-It track live number of corona cases in any country or in any states of India.(By voice command or on Map by moving mouse coursor over the country or states)
-It can be used to know the symptoms of covid-19.
-It can be used to know how covid-19 spreads and what we can do to prevent it.
-It can be used to know the Do's and Dont's about covid-19.
-It can be used to check the fact about the myths that are circulating about covid-19.
-It will send you notifications about symptoms,preventions and fact about myths in regular time interval so, it will keep you updated while you're working on your machine.
  

Note: You can access all the features either by voice command or by the buttons as well.''')

    def about(self):
        messagebox.showinfo("Covid-19 Voice Assistant System Developer","Mohammad Noaman Khan \nEmail: khan.noamaan@gmail.com")


    def state(self,key=None):
        if self.status:
            self.status=False
            self.loadimage = PhotoImage(file="micoff.png")
            self.send_button.config(image=self.loadimage)
            self.last_sent_label("Not Listening")

        else:
            self.loadimage = PhotoImage(file="micon.png")
            self.send_button.config(image=self.loadimage)
            self.last_sent_label("Restarting")
            self.status = True


    def font_change_default(self):
        self.text_box.config(font="Verdana 10")
        self.font = "Verdana 10"

    def font_change_times(self):
        self.text_box.config(font="Times")
        self.font = "Times"

    def font_change_system(self):
        self.text_box.config(font="System")
        self.font = "System"

    def font_change_helvetica(self):
        self.text_box.config(font="helvetica 10")
        self.font = "helvetica 10"

    def font_change_fixedsys(self):
        self.text_box.config(font="fixedsys")
        self.font = "fixedsys"

    def color_theme_default(self):
        self.master.config(bg="#EEEEEE")
        self.text_frame.config(bg="#EEEEEE")
        self.text_box.config(bg="#FFFFFF", fg="#000000")
        self.send_button_frame.config(bg="#EEEEEE")
        self.send_button.config(bg="#EEEEEE", fg=F"#000000", activebackground="#EEEEEE", activeforeground="#000000")
        self.send_button1.config(bg="#EEEEEE", fg=F"#000000", activebackground="#FFFFFF", activeforeground="#000000")
        self.send_button2.config(bg="#EEEEEE", fg=F"#000000", activebackground="#FFFFFF", activeforeground="#000000")
        self.send_button3.config(bg="#EEEEEE", fg=F"#000000", activebackground="#FFFFFF", activeforeground="#000000")
        self.send_button4.config(bg="#EEEEEE", fg=F"#000000", activebackground="#FFFFFF", activeforeground="#000000")
        self.send_button5.config(bg="#EEEEEE", fg=F"#000000", activebackground="#FFFFFF", activeforeground="#000000")
        self.send_button6.config(bg="#EEEEEE", fg=F"#000000", activebackground="#FFFFFF", activeforeground="#000000")
        self.sent_label.config(bg="#EEEEEE", fg="#000000")

        self.tl_bg = "#FFFFFF"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"

    # Dark
    def color_theme_dark(self):
        self.master.config(bg="#2a2b2d")
        self.text_frame.config(bg="#2a2b2d")
        self.text_box.config(bg="#212121", fg="#FFFFFF")
        self.send_button_frame.config(bg="#2a2b2d")
        self.send_button.config(bg="#2a2b2d", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        self.send_button1.config(bg="#2a2b2d", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        self.send_button2.config(bg="#2a2b2d", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        self.send_button3.config(bg="#2a2b2d", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        self.send_button4.config(bg="#2a2b2d", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        self.send_button5.config(bg="#2a2b2d", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        self.send_button6.config(bg="#2a2b2d", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#2a2b2d", fg="#FFFFFF")

        self.tl_bg = "#212121"
        self.tl_bg2 = "#2a2b2d"
        self.tl_fg = "#FFFFFF"

    # Grey
    def color_theme_grey(self):
        self.master.config(bg="#444444")
        self.text_frame.config(bg="#444444")
        self.text_box.config(bg="#4f4f4f", fg="#ffffff")
        self.send_button_frame.config(bg="#444444")
        self.send_button.config(bg="#444444", fg="#ffffff", activebackground="#444444", activeforeground="#ffffff")
        self.send_button1.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.send_button2.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.send_button3.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.send_button4.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.send_button5.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.send_button6.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.sent_label.config(bg="#444444", fg="#ffffff")

        self.tl_bg = "#4f4f4f"
        self.tl_bg2 = "#444444"
        self.tl_fg = "#ffffff"


        # Blue

    def color_theme_dark_blue(self):
        self.master.config(bg="#263b54")
        self.text_frame.config(bg="#263b54")
        self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
        self.send_button_frame.config(bg="#263b54")
        self.send_button.config(bg="#263b54", fg="#FFFFFF", activebackground="#263b54", activeforeground="#FFFFFF")
        self.send_button1.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.send_button2.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.send_button3.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.send_button4.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.send_button5.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.send_button6.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#263b54", fg="#FFFFFF")

        self.tl_bg = "#1c2e44"
        self.tl_bg2 = "#263b54"
        self.tl_fg = "#FFFFFF"

    # Torque
    def color_theme_turquoise(self):
        self.master.config(bg="#003333")
        self.text_frame.config(bg="#003333")
        self.text_box.config(bg="#669999", fg="#FFFFFF")
        self.send_button_frame.config(bg="#003333")
        self.send_button.config(bg="#003333", fg="#FFFFFF", activebackground="#003333", activeforeground="#FFFFFF")
        self.send_button1.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.send_button2.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.send_button3.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.send_button4.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.send_button5.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.send_button6.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#003333", fg="#FFFFFF")

        self.tl_bg = "#669999"
        self.tl_bg2 = "#003333"
        self.tl_fg = "#FFFFFF"

    # Hacker
    def color_theme_hacker(self):
        self.master.config(bg="#0F0F0F")
        self.text_frame.config(bg="#0F0F0F")
        self.text_box.config(bg="#0F0F0F", fg="#33FF33")
        self.send_button_frame.config(bg="#0F0F0F")
        self.send_button.config(bg="#0F0F0F", fg="#33FF33", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.send_button1.config(bg="#0F0F0F", fg="#33FF33", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.send_button2.config(bg="#0F0F0F", fg="#33FF33", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.send_button3.config(bg="#0F0F0F", fg="#33FF33", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.send_button4.config(bg="#0F0F0F", fg="#33FF33", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.send_button5.config(bg="#0F0F0F", fg="#33FF33", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.send_button6.config(bg="#0F0F0F", fg="#33FF33", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#0F0F0F", fg="#33FF33")

        self.tl_bg = "#0F0F0F"
        self.tl_bg2 = "#0F0F0F"
        self.tl_fg = "#33FF33"

    # Default font and color theme
    def default_format(self):
        self.font_change_default()
        self.color_theme_default()

    def user(self,user_input):
        pr1 = "You : " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)

    def bot(self,ob):
        pr = "covid-19 voice assistant : " + ob + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)

    def main(self):
        c = Country()
        s = States()

        c.start()
        s.start()

        wishMe()

        c.join()
        s.join()
        df = pd.concat([c.countriesData, s.statesData])

        while True:
            if self.status:
                query = takeCommand(self)
                if Exit(query):
                    self.bot("Bye")
                    speak("Bye")
                    self.chatexit()
                    break

                elif "map" in query:
                    if "India" in query:
                        StateMap.run()
                    else:
                        CountryMap.run()

                elif "symptom" in query:
                    symp=Symptoms()
                    symp.start()
                    lines = data()
                    st = ""
                    for j in lines[11:16]:
                        st += j
                    for j in lines[25:29]:
                        st += j

                    self.bot(st)
                    speak(st)
                    symp.join()


                elif "myth" in query:
                    MythBuster.run()

                elif "spread" in query or "prevention" in query:
                    sprd=SpreadPrevention()
                    sprd.start()
                    lines = data()
                    st=lines[5]+lines[4]
                    self.bot(st)
                    speak(st)
                    sprd.join()


                elif "do" in  query or "don't" in query:
                    DoDont.run()


                elif ("coronavirus" in query or "covid-19" in query) and find_place(query,s,c)==[]:
                    lines=data()
                    st=lines[2]+lines[3]+lines[6]
                    self.bot(st)
                    speak(st)



                else:
                    places = find_place(query, s, c)
                    for i in places:
                        p, q, r, t = df.loc[i, :]

                        self.last_sent_label('Searching Cases for {}...'.format(i))
                        speak('Searching Cases for {}...'.format(i))

                        self.bot(
                            "{} have Total {} corona cases in which {} are still active , {} have recovered and {} are dead.".format(
                                i, p, q, r, t))
                        self.last_sent_label('{}'.format(i))
                        speak(
                            "{} have Total {} corona  cases in which {} are still active , {} have recovered and {} are dead.".format(
                                i, p, q, r, t))


window_size = "800x500"
#Notification Thread
noti = notifi()
noti.start()

root=Tk()

a = ChatInterface(root)

#main
m=threading.Thread(target=a.main)
m.start()


root.geometry(window_size)
root.minsize(800,400)
root.maxsize(800,400)
root.title("Covid-19 Voice Assistant")
root.mainloop()

os._exit(0)


