import tkinter as UI
import tkinter.font as tkfont
import webbrowser

window = UI.Tk(className="/WaterLog")
mainspace = UI.Frame(master = window)
mainpage = UI.Frame(master = mainspace, relief = UI.RAISED, borderwidth = 3, width = 100, height = 300)

today = 0
page = 0
helpurl = "https://github.com/trufflewar/waterlog/wiki"


#SETUP BOTTOM MENU
base = UI.Frame(master = window, relief = UI.RAISED, borderwidth = 3, width = 30, height = 50, bg = "#00c9c3")

base.columnconfigure(0, weight = 5, minsize = 100)
base.columnconfigure(1, weight = 6, minsize = 120)
base.columnconfigure(2, weight = 5, minsize = 100)

graph_button = UI.Button(master = base, text = "Graphs", relief = UI.RAISED, borderwidth = 1, bg = "#00d9d2", width = 8)
graph_button.grid(column = 0, row = 0, padx = 5, pady = 5)

home_button = UI.Button(master = base, text = "Home", relief = UI.RAISED, borderwidth = 1, bg = "#00d9d2", width = 8)
home_button.grid(column = 1, row = 0, padx = 5, pady = 5)

log_button = UI.Button(master = base, text = "Log", relief = UI.RAISED, borderwidth = 1, bg = "#00d9d2", width = 8)
log_button.grid(column = 2, row = 0, padx = 5, pady = 5)


#SETUP TOP BAR
header = UI.Frame(master = window, relief = UI.RAISED, borderwidth = 3, width = 30, height = 50, bg = "#00c9c3")

header.columnconfigure(0, weight = 1, minsize = 50)
header.columnconfigure(1, weight = 4, minsize = 200)
header.columnconfigure(2, weight = 1, minsize = 50)

help_img = UI.PhotoImage(file = "Waterlog/clipart23133.png")
help_img_new = help_img.subsample(100,100)
help_button = UI.Button(master = header, image = help_img_new, relief = UI.RAISED, borderwidth = 1, bg = "#00d9d2")
help_button.grid(column = 0, row = 0, padx = 5, pady = 5)

title = UI.Label(master = header, text = "WaterLog", bg = "#00d9d2")
title.grid(column = 1, row = 0, padx = 5, pady = 5)

cog_img = UI.PhotoImage(file = "Waterlog/clipart171375.png")
cog_img_new = cog_img.subsample(25,25)
settings_button = UI.Button(master = header, image = cog_img_new, relief = UI.RAISED, borderwidth = 1, bg = "#00d9d2")
settings_button.grid(column = 2, row = 0, padx = 5, pady = 5)



#SETUP FUNCTIONS FOR BASE AND HEADER BUTTONS AND BIND ACTIONS TO BUTTONS
def home_btn(event):
    page = "Home"
    go_home()
home_button.bind("<Button-1>", home_btn)

def graph_btn(event):
    page = "Graphs"
    graph_page()
    
graph_button.bind("<Button-1>", graph_btn)

def log_btn(event):
    page = "Log"
    log_page()
log_button.bind("<Button-1>", log_btn)

def settings_btn(event):
    page = "Settings"
    settings_page()
settings_button.bind("<Button-1>", settings_btn)

def help_btn(event):
    webbrowser.open(helpurl)
help_button.bind("<Button-1>", help_btn)


#HOME PAGE
def go_home():
    global mainpage
    mainpage.destroy()
    
    mainpage = UI.Frame(master = mainspace)
    mainpage.pack(side = UI.TOP, fill = "both", expand = True)
    
    today_widget = UI.Frame(master = mainpage, bg = "#00d9d2", relief = UI.RAISED, borderwidth = 3, height = 75, width = 300)
    today_widget.pack(fill = UI.X, padx = 10, pady = 10, expand = True)
    
    today_widget.columnconfigure(0)
    today_widget.rowconfigure(0)
    today_message = UI.Label(master = today_widget, text = "Today you've drunk " + str(today) + "ml", bg = "#00d9d2")
    today_message.grid(row = 0, column = 0, sticky = "nsew")

    #Home log buttons
    home_log_buttons = UI.Frame(master = mainpage)
    


    #Log button 1 
    value1 = 90
    log_button_1 = UI.Button(master = home_log_buttons, text = ("Log " + str(value1) + "ml") , relief = UI.RAISED, borderwidth = 3, bg = "#00d9d2", width = 8)
    log_button_1.pack()


    
    
#LOG PAGE
def log_page():
    global mainpage
    mainpage.destroy()
    
    mainpage = UI.Frame(master = mainspace)
    mainpage.pack(side = UI.TOP, fill = "both", expand = True)
    

#GRAPH PAGE
def graph_page():
    global mainpage
    mainpage.destroy()
    
    mainpage = UI.Frame(master = mainspace)
    mainpage.pack(side = UI.TOP, fill = "both", expand = True)


#SETTINGS PAGE
def settings_page():
    global mainpage
    mainpage.destroy()
    
    mainpage = UI.Frame(master = mainspace)
    mainpage.pack(side = UI.TOP, fill = "both", expand = True)
    

#INITIATE BASE and HEADER SETUP
base.pack(fill = UI.X, side = UI.BOTTOM)
header.pack(fill = UI.X, side = UI.TOP)
mainspace.pack()

window.minsize(335, 300)

go_home()
window.mainloop()