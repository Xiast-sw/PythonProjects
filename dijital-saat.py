from tkinter import Label,Tk
import time

app_windows=Tk()
app_windows.title("Digital Clock")
app_windows.geometry("500x250")
app_windows.resizable(1,1)
app_windows.configure(bg="black")

text_font=("Boulder",36,'bold')
background ="black"
foreground ="white"
border_width=20

label= Label(app_windows,font=text_font,bg=background,fg=foreground)
label.grid(row=0,column=1,padx=border_width,pady=10)

date_label=Label(app_windows,font=text_font,bg=background,fg=foreground)
date_label.grid(row=1,column=1,padx=border_width,pady=10)

def digitalClock():
    timeLive=time.strftime("%H:%M:%S")
    label.config(text=timeLive)

    dateInfo=time.strftime("%d %B %Y")
    date_label.config(text=dateInfo)
    label.after(200,digitalClock)


digitalClock()

app_windows.mainloop()
