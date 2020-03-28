import tkinter as tk
import controller as c

#Main window settings
main_window = tk.Tk()
main_window.title("Calculator")
main_window.configure(background='#d9d9d9', relief='flat')
main_window.minsize(300,400)
main_window.grid_rowconfigure(0, weight=1)
main_window.grid_columnconfigure(0, weight=1)

main_frame = tk.Frame(main_window, relief='flat', borderwidth=3, bg='#d9d9d9')
main_frame.grid(column=0, row=0, sticky=('N', 'S','E', 'W'))
main_frame.grid_columnconfigure((0,1,2,3), weight=1)
main_frame.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)

#Controller reading
operation = []
alreadyFloat = False

def read(arg):
    global operation

    if arg in '0123456789.':
        if arg == '.' and ('.' not in displayResult.get("1.0",tk.END)):
            displayResult.insert(tk.END ,arg)
        elif arg == '.' and ('.' in displayResult.get("1.0",tk.END)):
            pass
        else:
            displayResult.insert(tk.END, arg)
    elif (arg == 'sig'):
        val = float(displayResult.get("1.0",tk.END))
        val *= -1
        displayResult.delete("1.0",tk.END)
        displayResult.insert(tk.END, val)

    elif arg in ['+','-','/','*']:
        if not displayResult.get("1.0", tk.END).strip():
            pass
        else:
            copy = displayResult.get("1.0", tk.END)
            displayResult.delete("1.0",tk.END)
            val = float(copy)
            operation.append(val)
            operation.append(arg)
            displayOp.insert(tk.END, val)
            displayOp.insert(tk.END, ' '+arg+' ')

    elif arg in ['pc','in','sq','sr']:
        if not displayResult.get("1.0", tk.END).strip():
            pass
        else:
            copy = displayResult.get("1.0", tk.END)
            displayResult.delete("1.0", tk.END)
            val = float(copy)
            ans = c.instaSolve(val,arg)
            displayResult.insert(tk.END, ans)
    elif arg == 'bs':
        displayResult.delete('1.'+str(len(displayResult.get("1.0", tk.END))-2), tk.END)
    elif arg in ['cl', 'ce']:
        if arg == 'cl':
            operation = []
            displayResult.delete("1.0", tk.END)
            displayOp.delete("1.0", tk.END)
        elif arg == 'ce':
            displayResult.delete("1.0", tk.END)
        else:
            pass
    elif arg == '=':
        if not displayResult.get("1.0", tk.END).strip():
            pass
        else:
            copy = displayResult.get("1.0", tk.END)
            displayResult.delete("1.0", tk.END)
            val = float(copy)
            operation.append(val)
            displayOp.insert(tk.END, val)
            displayOp.insert(tk.END, ' ')
            print(operation)
            ans = c.solve(operation)
            operation = []
            displayOp.delete("1.0", tk.END)
            displayResult.insert(tk.END, ans)

    else:
        pass

    return


#Widgets definition
displayOp= tk.Text(main_frame,bg='#d9d9d9',relief='flat', height=1, width= 20)
displayOp.configure(font=('Arial',20))
displayResult= tk.Text(main_frame,bg='#d9d9d9',relief='flat', height=1, width= 20)
displayResult.configure(font=('Arial',24,'bold'))

button_0 = tk.Button(main_frame, text='0', bg='#ffffff', relief='flat', command= lambda: read('0'))
button_1 = tk.Button(main_frame, text='1', bg='#ffffff', relief='flat', command= lambda: read('1'))
button_2 = tk.Button(main_frame, text='2', bg='#ffffff', relief='flat', command= lambda: read('2'))
button_3 = tk.Button(main_frame, text='3', bg='#ffffff', relief='flat', command= lambda: read('3'))
button_4 = tk.Button(main_frame, text='4', bg='#ffffff', relief='flat', command= lambda: read('4'))
button_5 = tk.Button(main_frame, text='5', bg='#ffffff', relief='flat', command= lambda: read('5'))
button_6 = tk.Button(main_frame, text='6', bg='#ffffff', relief='flat', command= lambda: read('6'))
button_7 = tk.Button(main_frame, text='7', bg='#ffffff', relief='flat', command= lambda: read('7'))
button_8 = tk.Button(main_frame, text='8', bg='#ffffff', relief='flat', command= lambda: read('8'))
button_9 = tk.Button(main_frame, text='9', bg='#ffffff', relief='flat', command= lambda: read('9'))
button_signal = tk.Button(main_frame, text='+/-', bg='#ffffff', relief='flat', command= lambda: read('sig'))
button_comma = tk.Button(main_frame, text=',', bg='#ffffff', relief='flat', command= lambda: read('.'))

button_plus = tk.Button(main_frame, text='+', bg='#f1f1f1', relief='flat', command= lambda: read('+'))
button_minus = tk.Button(main_frame, text='-', bg='#f1f1f1', relief='flat', command= lambda: read('-'))
button_times = tk.Button(main_frame, text='x' ,bg='#f1f1f1', relief='flat', command= lambda: read('*'))
button_div = tk.Button(main_frame, text='/', bg='#f1f1f1', relief='flat', command= lambda: read('/'))
button_equals = tk.Button(main_frame, text='=', bg='#f1f1f1', relief='flat', command= lambda: read('='))
button_percent = tk.Button(main_frame, text='%', bg='#f1f1f1', relief='flat', command= lambda: read('pc'))
button_inverse = tk.Button(main_frame, text='1/x', bg='#f1f1f1', relief='flat', command= lambda: read('in'))
button_square = tk.Button(main_frame, text='x^2', bg='#f1f1f1', relief='flat', command= lambda: read('sq'))
button_sqroot = tk.Button(main_frame, text='sqrt', bg='#f1f1f1', relief='flat', command= lambda: read('sr'))

button_clear = tk.Button(main_frame, text='C',bg='#f1f1f1', relief='flat', command= lambda: read('cl'))
button_ce = tk.Button(main_frame, text='CE',bg='#f1f1f1', relief='flat', command= lambda: read('ce'))
button_backspace = tk.Button(main_frame, text='<-',bg='#f1f1f1', relief='flat', command= lambda: read('bs'))

#grid positioning

displayOp.grid(row=0, column=0, rowspan=1, columnspan=4, sticky=('N', 'S','E', 'W'))
displayResult.grid(row=1, column=0, rowspan=1, columnspan=4, sticky=('N', 'S','E', 'W'))

button_0.grid(row=7, column=1, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_1.grid(row=6, column=0, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_2.grid(row=6, column=1, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_3.grid(row=6, column=2, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_4.grid(row=5, column=0, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_5.grid(row=5, column=1, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_6.grid(row=5, column=2, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_7.grid(row=4, column=0, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_8.grid(row=4, column=1, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_9.grid(row=4, column=2, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_signal.grid(row=7, column=0, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_comma.grid(row=7, column=2, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))

button_plus.grid(row=6, column=3, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_minus.grid(row=5, column=3, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_times.grid(row=4, column=3, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_div.grid(row=3, column=3, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_equals.grid(row=7, column=3, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_percent.grid(row=2, column=0, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_inverse.grid(row=3, column=0, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_square.grid(row=3, column=1, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_sqroot.grid(row=3, column=2, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))

button_clear.grid(row=2, column=2, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_ce.grid(row=2, column=1, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))
button_backspace.grid(row=2, column=3, rowspan=1, columnspan=1, padx= 2, pady=2, sticky=('N', 'S','E', 'W'))


#Window show
main_window.mainloop()