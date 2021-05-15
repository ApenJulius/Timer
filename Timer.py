import time
import tkinter as tk

root = tk.Tk()
root.geometry("400x350+1000+300")
root.title("Big boy timer")
def timerStart(lbl):
    global running
    running = True
    counterLabel(lbl)
    startButt['state']='disabled'
    stopButt['state']='normal'

def timerStop():
    global running
    startButt['state']='normal'
    stopButt['state']='disabled'
    running = False


def counterLabel(lbl):
    def count():
        if running:
            global sec1, sec2, min1, min2, h1, h2
            if sec2 == -1:
                display="00:00:00"
            else:
                display = str(f"{h1}{h2}:{min1}{min2}:{sec1}{sec2}")
            
            lbl['text']=display

            lbl.after(1, count)
            if sec2 == 9: #if first digit is 9 it will go set second as 1 instead of going to 10
                sec2 = 0
                if sec1 == 5: #same but for turning sec to min
                    sec1 = 0
                    if min2 == 9: #turns from 09 to 10
                        min2 = 0
                        if min1 == 5:
                            min1 = 0
                            if h2 == 9:
                                h2 = 0
                                h1 += 1
                            else: h2 +=1
                        else: min1 +=1
                    else: min2 += 1
                else: sec1 += 1
            else: sec2 +=1

            
            
    count()



sec1 = 0
sec2 = -1
min1 = 0
min2 = 0
h1 = 0
h2 = 0

counter = f"{h1}{h2}:{min1}{min2}:{sec1}{sec2}"

running = False



lbl = tk.Label(root, text="00:00:00", fg="black", font="Verdana 40 bold")

label_msg = tk.Label(root, text="Next alarm in", fg="black",font="Verdana 10 bold")

lbl.place(x=60, y=70)
label_msg.place(x=145, y=150)



startButt = tk.Button(root, bg="green4", activebackground="green4", width=15, text="Start", command = lambda:timerStart(lbl))
startButt.place(x=30, y=290)

stopButt = tk.Button(root, bg="red",activebackground="red", width=15, state='disabled', text="Stop", command=timerStop)
stopButt.place(x=270, y=290)



root.mainloop()