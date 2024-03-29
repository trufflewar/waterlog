import tkinter as UI
import tkinter.font as tkfont
import webbrowser
import backend
import csv

window = UI.Tk(className="/WaterLog")
#window.iconbitmap("4_generated.ico")
mainspace = UI.Frame(master=window)
mainpage = UI.Frame(master=mainspace,
                    relief=UI.RAISED,
                    borderwidth=3,
                    width=100,
                    height=300)

today = 0
page = 0
helpurl = "https://github.com/trufflewar/waterlog/wiki"
global log_value
log_value = 300

global value1
global value2
file = open("Waterlog/logbuttons.csv", "r")
reader = csv.reader(file)
contents = []


for item in reader:
    contents.append(item)
value1 = int(contents[0][0])
value2 = int(contents[1][0])
file.close()

#SETUP BOTTOM MENU
base = UI.Frame(master=window,
                relief=UI.RAISED,
                borderwidth=3,
                width=30,
                height=50,
                bg="#00c9c3")

base.columnconfigure(0, weight=5, minsize=100)
base.columnconfigure(1, weight=6, minsize=120)
base.columnconfigure(2, weight=5, minsize=100)

history_button = UI.Button(master=base,
                         text="History",
                         relief=UI.RAISED,
                         borderwidth=1,
                         bg="#00d9d2",
                         width=8)
history_button.grid(column=0, row=0, padx=5, pady=5)

home_button = UI.Button(master=base,
                        text="Home",
                        relief=UI.RAISED,
                        borderwidth=1,
                        bg="#00d9d2",
                        width=8)
home_button.grid(column=1, row=0, padx=5, pady=5)

log_button = UI.Button(master=base,
                       text="Log",
                       relief=UI.RAISED,
                       borderwidth=1,
                       bg="#00d9d2",
                       width=8)
log_button.grid(column=2, row=0, padx=5, pady=5)


#SETUP TOP BAR
header = UI.Frame(master=window,
                  relief=UI.RAISED,
                  borderwidth=3,
                  width=30,
                  height=50,
                  bg="#00c9c3")

header.columnconfigure(0, weight=1, minsize=50)
header.columnconfigure(1, weight=4, minsize=200)
header.columnconfigure(2, weight=1, minsize=50)

help_img = UI.PhotoImage(file="Waterlog/clipart23133.png")
help_img_new = help_img.subsample(100, 100)
help_button = UI.Button(master=header,
                        image=help_img_new,
                        relief=UI.RAISED,
                        borderwidth=1,
                        bg="#00d9d2")
help_button.grid(column=0, row=0, padx=5, pady=5)

title = UI.Label(master=header, text="WaterLog", bg="#00d9d2")
title.grid(column=1, row=0, padx=5, pady=5)

cog_img = UI.PhotoImage(file="Waterlog/clipart171375.png")
cog_img_new = cog_img.subsample(25, 25)
settings_button = UI.Button(master=header,
                            image=cog_img_new,
                            relief=UI.RAISED,
                            borderwidth=1,
                            bg="#00d9d2")
settings_button.grid(column=2, row=0, padx=5, pady=5)


#SETUP FUNCTIONS FOR BASE AND HEADER BUTTONS AND BIND ACTIONS TO BUTTONS
def homepage_btn(event):
    page = "Home"
    go_home()
home_button.bind("<Button-1>", homepage_btn)


def historypage_btn(event):
    page = "History"
    history_page()
history_button.bind("<Button-1>", historypage_btn)


def logpage_btn(event):
    page = "Log"
    log_page()
log_button.bind("<Button-1>", logpage_btn)


def settingspage_btn(event):
    page = "Settings"
    settings_page()
settings_button.bind("<Button-1>", settingspage_btn)


def help_btn(event):
    webbrowser.open(helpurl)
help_button.bind("<Button-1>", help_btn)


#HOME PAGE
def go_home():
    global mainpage
    mainpage.destroy()

    mainpage = UI.Frame(master=mainspace)
    mainpage.pack(side=UI.TOP, fill="both", expand=True)

    today_widget = UI.Frame(master=mainpage,
                            bg="#00d9d2",
                            relief=UI.RAISED,
                            borderwidth=3,
                            height=75,
                            width=300)
    today_widget.pack(fill=UI.X, padx=10, pady=10, expand=True)

    today_widget.columnconfigure(0)
    today_widget.rowconfigure(0)
    today_message = UI.Label(master=today_widget,
                             text="Today you've drunk " +
                             str(backend.gettoday()) + "ml",
                             bg="#00d9d2")
    today_message.grid(row=0, column=0, sticky="nsew")

    #Home log buttons
    home_log_buttons = UI.Frame(master=mainpage)
    home_log_buttons.columnconfigure(1)
    home_log_buttons.rowconfigure(0)
    home_log_buttons.pack()

    #Log buttons

    log_button_1 = UI.Button(master=home_log_buttons,
                             text=("Log  " + str(value1) + "ml"),
                             relief=UI.RAISED,
                             borderwidth=3,
                             bg="#00d9d2",
                             width=8)
    log_button_1.grid(row=0, column=0, sticky="nsew")

    def log_btn_1(event):
        backend.logvalue(value1)
        today_message.config(text="Today you've drunk " +
                             str(backend.gettoday()) + "ml")

    log_button_1.bind("<Button-1>", log_btn_1)

    log_button_2 = UI.Button(master=home_log_buttons,
                             text=("Log  " + str(value2) + "ml"),
                             relief=UI.RAISED,
                             borderwidth=3,
                             bg="#00d9d2",
                             width=8)
    log_button_2.grid(row=0, column=1, sticky="nsew")

    def log_btn_2(event):
        backend.logvalue(value2)
        today_message.config(text="Today you've drunk " +
                             str(backend.gettoday()) + "ml")
    log_button_2.bind("<Button-1>", log_btn_2)


#LOG PAGE
#LOG PAGE
def log_page():
    global mainpage
    global log_value
    mainpage.destroy()

    mainpage = UI.Frame(master=mainspace)
    mainpage.pack(side=UI.TOP, fill="both", expand=True)
    
    
    # Log widget
    log_value = 300
    log_widget = UI.Frame(master=mainpage, relief=UI.RAISED, borderwidth=1)
    log_widget.columnconfigure(0, weight = 8)
    log_widget.columnconfigure(1, weight = 2)
    log_widget.columnconfigure(2, weight = 4)
    log_widget.rowconfigure(0, weight = 4)


    num_box = UI.Label(master = log_widget, text = str(log_value) + "ml")
    num_box.grid(row = 0, column = 0)
  
    
    counter_buttons = UI.Frame(master = log_widget)
    counter_buttons.columnconfigure(0)
    counter_buttons.rowconfigure(0)
    counter_buttons.rowconfigure(1)
    
    up_button = UI.Button(master=counter_buttons, text = "+", relief = UI.RAISED, borderwidth = 1)
    up_button.grid(row=0, column = 0)
    def up_btn(event):
      global log_value
      log_value += 10
      num_box.config(text= str(log_value) + "ml")
    up_button.bind("<Button-1>", up_btn)

    down_button = UI.Button(master=counter_buttons, text = "-", relief = UI.RAISED, borderwidth = 1)
    down_button.grid(row=1, column = 0)
    def down_btn(event):
      global log_value
      log_value += -10
      if log_value < 0:
        log_value = 0
      num_box.config(text= str(log_value) + "ml")
    down_button.bind("<Button-1>", down_btn)
   
    counter_buttons.grid(row=0, column=1)

  
    log_page_log_button = UI.Button(master = log_widget, text = "Log", relief = UI.RAISED, borderwidth = 1)
    log_page_log_button.grid(row = 0, column = 2)
    def log_page_log_btn(event):
      global log_value
      backend.logvalue(log_value)
    log_page_log_button.bind("<Button-1>", log_page_log_btn)


    log_widget.pack(padx=5, pady = 5)

  
    


  

  


#GRAPH PAGE
#GRAPH PAGE
def history_page():
    global mainpage
    mainpage.destroy()

    mainpage = UI.Frame(master=mainspace)
    mainpage.pack(side=UI.TOP, fill="both", expand=True)

    today_widget = UI.Frame(master=mainpage,
                            bg="#00d9d2",
                            relief=UI.RAISED,
                            borderwidth=3,
                            height=75,
                            width=300)
    today_widget.pack(fill=UI.X, padx=10, pady=10, expand=True)

    today_widget.columnconfigure(0)
    today_widget.rowconfigure(0)
    today_message = UI.Label(master=today_widget,
                             text="Today you've drunk " +
                             str(backend.gettoday()) + "ml",
                             bg="#00d9d2")
    today_message.grid(row=0, column=0, sticky="nsew")


    week_widget = UI.Frame(master=mainpage,
                            bg="#00d9d2",
                            relief=UI.RAISED,
                            borderwidth=3,
                            height=75,
                            width=300)
    week_widget.pack(fill=UI.X, padx=10, pady=10, expand=True)

    week_widget.columnconfigure(0)
    week_widget.rowconfigure(0)
    week_message = UI.Label(master=today_widget,
                             text="This week you've drunk " +
                             #str(backend.getweek()) + 
                            "ml",
                             bg="#00d9d2")
    week_message.grid(row=0, column=0, sticky="nsew")
  


#SETTINGS PAGE
def settings_page():
    global mainpage
    mainpage.destroy()

    mainpage = UI.Frame(master=mainspace)
    mainpage.pack(side=UI.TOP, fill="both", expand=True)


#INITIATE BASE and HEADER SETUP
base.pack(fill=UI.X, side=UI.BOTTOM)
header.pack(fill=UI.X, side=UI.TOP)
mainspace.pack()

window.minsize(335, 300)

go_home()
window.mainloop()
