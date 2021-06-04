import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import datetime
from win10toast import ToastNotifier
import schedule
import time
import weathercell
import weathermap

color = 'lightblue'
root = Tk()
class CoreElements(Frame):

    def __init__(self, root=None):
        super(CoreElements, self).__init__(root)
        self.initUI(root)
        

    def initUI(self, root):

        self.master.title("Lines")

        root.columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)

        self.widgets = []
        header = Label(root, text="Day")
        header.grid(row=0, column=0, sticky="EW", padx=1, pady=1)
        self.widgets.append(header)
        header = Label(root, text="Weather")
        header.grid(row=0, column=1, sticky="EW", padx=1, pady=1)
        self.widgets.append(header)
        header = Label(root, text="Min")
        header.grid(row=0, column=2, sticky="EW", padx=1, pady=1)
        self.widgets.append(header)
        header = Label(root, text="Max")
        header.grid(row=0, column=3, sticky="EW", padx=1, pady=1)
        self.widgets.append(header)
        header = Label(root, text="UV Index")
        header.grid(row=0, column=4, sticky="EW", padx=1, pady=1)
        self.widgets.append(header)
        self.notebox = Text(root, width=1)
        self.notebox.grid(column=5, columnspan=5, row=0, rowspan=5, sticky="NESW", padx=1, pady=1)

class Timer1(Frame):
    
    def __init__(self, root):

        super(Timer1, self).__init__(root)

        self.t1name = StringVar(value='Alarm Name Here')
        t1nentry = Entry(root, textvariable=self.t1name)

        t1nentry.grid(column=5, columnspan=1, row=5, sticky="EW", padx=1, pady=1)

        self.t1hour = StringVar(value=1)
        t1hspinbox = ttk.Spinbox(root, from_=1, to=12, textvariable=self.t1hour, wrap=True)

        t1hspinbox.grid(column=6, columnspan=1, row=5, sticky="EW", padx=1, pady=1)

        self.t1min = StringVar(value="00")
        t1mspinbox = ttk.Spinbox(root, from_=00, to=59, textvariable=self.t1min, wrap=True, format='%02.0f')

        t1mspinbox.grid(column=7, columnspan=1, row=5, sticky="EW", padx=1, pady=1)
        AMorPM = ('AM', 'PM')

        self.t1ampm = StringVar(value='AM')

        t1ampmCB = ttk.Combobox(root, textvariable=self.t1ampm)
        t1ampmCB['values'] = AMorPM
        t1ampmCB['state'] = 'readonly'
        t1ampmCB.grid(column=8, columnspan=1, row=5, sticky="EW", padx=1, pady=1)
        
        t1confirm = Button(root, text="Confirm", command = self.confirmtimer1)
        t1confirm.grid(column=9, columnspan=1, row=5, sticky="EW")
        self.pong()

    def pong(self):
        schedule.run_pending()
        self.after(1000, self.pong)
    toast = ToastNotifier()
    def confirmtimer1(self):
        t1preconverttime = self.t1hour.get() + ":" + self.t1min.get() + " " + self.t1ampm.get()
        ctime1 = datetime.datetime.strptime(str(t1preconverttime), "%I:%M %p")
        schedule.every().day.at(ctime1.strftime("%H:%M")).do(self.t1notif)
    
    def t1notif(self):
        self.toast.show_toast(self.t1name.get(), "Reminder 1", duration=20, icon_path=None, threaded=True)
        return schedule.CancelJob
class Timer2(Frame):
    
    def __init__(self, root):

        super(Timer2, self).__init__(root)

        self.t2name = StringVar(value='Alarm Name Here')
        t2nentry = Entry(root, textvariable=self.t2name)

        t2nentry.grid(column=5, columnspan=1, row=6, sticky="EW", padx=1, pady=1)

        self.t2hour = StringVar(value=1)
        t2hspinbox = ttk.Spinbox(root, from_=1, to=12, textvariable=self.t2hour, wrap=True)

        t2hspinbox.grid(column=6, columnspan=1, row=6, sticky="EW", padx=1, pady=1)

        self.t2min = StringVar(value="00")
        t2mspinbox = ttk.Spinbox(root, from_=00, to=59, textvariable=self.t2min, wrap=True, format='%02.0f')

        t2mspinbox.grid(column=7, columnspan=1, row=6, sticky="EW", padx=1, pady=1)
        AMorPM = ('AM', 'PM')

        self.t2ampm = StringVar(value='AM')

        t2ampmCB = ttk.Combobox(root, textvariable=self.t2ampm)
        t2ampmCB['values'] = AMorPM
        t2ampmCB['state'] = 'readonly'
        t2ampmCB.grid(column=8, columnspan=1, row=6, sticky="EW", padx=1, pady=1)
        
        t2confirm = Button(root, text="Confirm", command = self.confirmtimer1)
        t2confirm.grid(column=9, columnspan=1, row=6, sticky="EW")
        self.pong()

    def pong(self):
        schedule.run_pending()
        self.after(1000, self.pong)
    toast = ToastNotifier()
    def confirmtimer1(self):
        t2preconverttime = self.t2hour.get() + ":" + self.t2min.get() + " " + self.t2ampm.get()
        ctime1 = datetime.datetime.strptime(str(t2preconverttime), "%I:%M %p")
        schedule.every().day.at(ctime1.strftime("%H:%M")).do(self.t2notif)
    
    def t2notif(self):
        self.toast.show_toast(self.t2name.get(), "Reminder 2", duration=20, icon_path=None, threaded=True)
        return schedule.CancelJob
class Timer3(Frame):
    
    def __init__(self, root):

        super(Timer3, self).__init__(root)

        self.t3name = StringVar(value='Alarm Name Here')
        t3nentry = Entry(root, textvariable=self.t3name)

        t3nentry.grid(column=5, columnspan=1, row=7, sticky="EW", padx=1, pady=1)

        self.t3hour = StringVar(value=1)
        t3hspinbox = ttk.Spinbox(root, from_=1, to=12, textvariable=self.t3hour, wrap=True)

        t3hspinbox.grid(column=6, columnspan=1, row=7, sticky="EW", padx=1, pady=1)

        self.t3min = StringVar(value="00")
        t3mspinbox = ttk.Spinbox(root, from_=00, to=59, textvariable=self.t3min, wrap=True, format='%02.0f')

        t3mspinbox.grid(column=7, columnspan=1, row=7, sticky="EW", padx=1, pady=1)
        AMorPM = ('AM', 'PM')

        self.t3ampm = StringVar(value='AM')

        t3ampmCB = ttk.Combobox(root, textvariable=self.t3ampm)
        t3ampmCB['values'] = AMorPM
        t3ampmCB['state'] = 'readonly'
        t3ampmCB.grid(column=8, columnspan=1, row=7, sticky="EW", padx=1, pady=1)
        
        t3confirm = Button(root, text="Confirm", command = self.confirmtimer1)
        t3confirm.grid(column=9, columnspan=1, row=7, sticky="EW")
        self.pong()

    def pong(self):
        schedule.run_pending()
        self.after(1000, self.pong)
    toast = ToastNotifier()
    def confirmtimer1(self):
        t3preconverttime = self.t3hour.get() + ":" + self.t3min.get() + " " + self.t3ampm.get()
        ctime1 = datetime.datetime.strptime(str(t3preconverttime), "%I:%M %p")
        schedule.every().day.at(ctime1.strftime("%H:%M")).do(self.t3notif)
    
    def t3notif(self):
        self.toast.show_toast(self.t3name.get(), "Reminder 3", duration=20, icon_path=None, threaded=True)
        return schedule.CancelJob
class Timer4(Frame):
    
    def __init__(self, root):

        super(Timer4, self).__init__(root)

        self.t4name = StringVar(value='Alarm Name Here')
        t4nentry = Entry(root, textvariable=self.t4name)

        t4nentry.grid(column=5, columnspan=1, row=8, sticky="EW", padx=1, pady=1)

        self.t4hour = StringVar(value=1)
        t4hspinbox = ttk.Spinbox(root, from_=1, to=12, textvariable=self.t4hour, wrap=True)

        t4hspinbox.grid(column=6, columnspan=1, row=8, sticky="EW", padx=1, pady=1)

        self.t4min = StringVar(value="00")
        t4mspinbox = ttk.Spinbox(root, from_=00, to=59, textvariable=self.t4min, wrap=True, format='%02.0f')

        t4mspinbox.grid(column=7, columnspan=1, row=8, sticky="EW", padx=1, pady=1)
        AMorPM = ('AM', 'PM')

        self.t4ampm = StringVar(value='AM')

        t4ampmCB = ttk.Combobox(root, textvariable=self.t4ampm)
        t4ampmCB['values'] = AMorPM
        t4ampmCB['state'] = 'readonly'
        t4ampmCB.grid(column=8, columnspan=1, row=8, sticky="EW", padx=1, pady=1)
        
        t4confirm = Button(root, text="Confirm", command = self.confirmtimer1)
        t4confirm.grid(column=9, columnspan=1, row=8, sticky="EW")
        self.pong()

    def pong(self):
        schedule.run_pending()
        self.after(1000, self.pong)
    toast = ToastNotifier()
    def confirmtimer1(self):
        t4preconverttime = self.t4hour.get() + ":" + self.t4min.get() + " " + self.t4ampm.get()
        ctime1 = datetime.datetime.strptime(str(t4preconverttime), "%I:%M %p")
        schedule.every().day.at(ctime1.strftime("%H:%M")).do(self.t4notif)
    
    def t4notif(self):
        self.toast.show_toast(self.t4name.get(), "Reminder 4", duration=20, icon_path=None, threaded=True)
        return schedule.CancelJob
    
class weatherdisplay(Frame):
    
    def __init__(self, root):

        super(weatherdisplay, self).__init__(root)

        weather_data = weathermap.get_weather_data()
        row = 1
        for wd in weather_data["daily"]:
            wc = weathercell.WeatherCell(root, wd)
            wc.grid(row=row, column=0, columnspan=5, sticky='NESW', padx=1, pady=1)
            row += 1

def main():

    t1 = Timer1(root)
    t2 = Timer2(root)
    t3 = Timer3(root)
    t4 = Timer4(root)
    wdisp = weatherdisplay(root)
    CE = CoreElements(root)
    root['bg'] = 'lightblue'
    columntotal, rowtotal = root.grid_size()
    root.resizable(False, False)
    for columns in range(columntotal):
        root.grid_columnconfigure(columns, minsize=150)
    for rows in range(1, rowtotal):
        root.grid_rowconfigure(rows, minsize=100)
    root.mainloop()


if __name__ == '__main__':
    main()
