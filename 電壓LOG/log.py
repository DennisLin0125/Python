import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import tkinter as tk
import random
import time

root = tk.Tk()
root . title ( 'Log data' )

width = 630
height = 700

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
root.geometry(size_geo)

root . config ( background = "#000000" )
root . resizable(0,0)


LabelVol =  Label  ( root , text = "電壓 (V)" , bg = 'black' , fg = 'white' ,font =( 'arial' ,  15 ,  'bold' ))
LabelVol . place  ( x = 20 , y = 20 , width = 100 , height = 30 )

LabelCurrent =  Label  ( root , text = "電流 (A)" , bg = 'black' , fg = 'white' ,font =( 'arial' ,  15 ,  'bold' ))
LabelCurrent . place  ( x = 180 , y = 20 , width = 100 , height = 30 )

LabelPower =  Label  ( root , text = "功率 (W)" , bg = 'black' , fg = 'white' ,font =( 'arial' ,  15 ,  'bold' ))
LabelPower . place  ( x = 360 , y = 20 , width = 100 , height = 30 )

f = Figure()
f_plot = f.add_subplot(221)
f_plot.set_title('Voltage')
f_plot.set_xlabel('times')
f_plot.set_ylabel('Voltage')

f_plot2 = f.add_subplot(222)
f_plot2.set_title('Current')
f_plot2.set_xlabel('times')
f_plot2.set_ylabel('Current')

f_plot3 = f.add_subplot(223)
f_plot3.set_title('Power')
f_plot3.set_xlabel('times')
f_plot3.set_ylabel('Power')

f.suptitle('Log data')
f.tight_layout()

x=[]
y=[]
z=[]

def draw_picture():
    dstr1 = tk . StringVar ()
    dstr2 = tk . StringVar ()
    dstr3 = tk . StringVar ()
    dstr4 = tk . StringVar ()
    dstr5 = tk . StringVar ()

    arr=[random.randint(10,500) for x in range(3)]
    x.append(arr[0])
    y.append(arr[1])
    z.append(arr[2])

    Mydate = time . strftime ( "%H:%M:%S" )
    Mytime = time . strftime ( "%Y-%m-%d" )

    dstr1 . set ( arr[0] )
    dstr2 . set ( arr[1] )
    dstr3 . set ( arr[2] )
    dstr4 . set ( Mydate )
    dstr5 . set ( Mytime )

    f_plot.plot(x)
    f_plot2.plot(y)
    f_plot3.plot(z)
    
    canvs.draw()

    lbVol = tk.Label ( root , textvariable = dstr1 , fg = 'green' , bg = 'black' ,font =( "arial" , 40 ))
    lbVol . place  ( x = 20 , y = 50 , width = 100 , height = 60 )
    lbCur = tk . Label ( root , textvariable = dstr2 , fg = 'green' , bg = 'black' ,font =( "arial" , 40 ))
    lbCur . place  ( x = 180 , y = 50 , width = 100 , height = 60 )
    lbPow = tk . Label ( root , textvariable = dstr3 , fg = 'green' , bg = 'black' ,font =( "arial" , 40 ))
    lbPow . place  ( x = 320 , y = 50 , width = 200 , height = 60 )

    lbtime = tk . Label ( root , textvariable = dstr4 , fg = 'green' , bg = 'black' ,font =( "arial" , 40 ))
    lbtime . place  ( x = 400 , y = 150 , width = 200 , height = 60 )

    lbdate = tk . Label ( root , textvariable = dstr5 , fg = 'green' , bg = 'black' ,font =( "arial" , 40 ))
    lbdate . place  ( x = 10 , y = 150 , width = 300 , height = 60 )

    arr=[]
    root . after ( 200 , draw_picture )

def say_goodbye():
    root.after(100, root.destroy)

canvs = FigureCanvasTkAgg(f, root)

canvs.get_tk_widget().pack(side=BOTTOM)

Button(root, text='連線', command=draw_picture).place (x=510,y=20)
Button(root, text="離開", command=say_goodbye).place (x=560,y=20)

root.mainloop()
