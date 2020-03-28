import tkinter as tk

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
#Widgets definition
main_screen= tk.Text(main_frame,bg='#d9d9d9',relief='flat', height=1, width= 20)

button_0 = tk.Button(main_frame, text='0', bg='#f1f1f1', relief='flat')
button_1 = tk.Button(main_frame, text='1', bg='#f1f1f1', relief='flat')
button_2 = tk.Button(main_frame, text='2', bg='#f1f1f1', relief='flat')
button_3 = tk.Button(main_frame, text='3', bg='#f1f1f1', relief='flat')
button_4 = tk.Button(main_frame, text='4', bg='#f1f1f1', relief='flat')
button_5 = tk.Button(main_frame, text='5', bg='#f1f1f1', relief='flat')
button_6 = tk.Button(main_frame, text='6', bg='#f1f1f1', relief='flat')
button_7 = tk.Button(main_frame, text='7', bg='#f1f1f1', relief='flat')
button_8 = tk.Button(main_frame, text='8', bg='#f1f1f1', relief='flat')
button_9 = tk.Button(main_frame, text='9', bg='#f1f1f1', relief='flat')
button_signal = tk.Button(main_frame, text='+/-', bg='#f1f1f1', relief='flat')
button_comma = tk.Button(main_frame, text=',', bg='#f1f1f1', relief='flat')

button_plus = tk.Button(main_frame, text='+', bg='#f1f1f1', relief='flat')
button_minus = tk.Button(main_frame, text='-', bg='#f1f1f1', relief='flat')
button_times = tk.Button(main_frame, text='x' ,bg='#f1f1f1', relief='flat')
button_div = tk.Button(main_frame, text='/', bg='#f1f1f1', relief='flat')
button_equals = tk.Button(main_frame, text='=', bg='#f1f1f1', relief='flat')
button_percent = tk.Button(main_frame, text='%', bg='#f1f1f1', relief='flat')
button_inverse = tk.Button(main_frame, text='1/x', bg='#f1f1f1', relief='flat')
button_square = tk.Button(main_frame, text='x^2', bg='#f1f1f1', relief='flat')
button_sqroot = tk.Button(main_frame, text='sqrt', bg='#f1f1f1', relief='flat')

button_clear = tk.Button(main_frame, text='C',bg='#f1f1f1', relief='flat')
button_ce = tk.Button(main_frame, text='CE',bg='#f1f1f1', relief='flat')
button_backspace = tk.Button(main_frame, text='<-',bg='#f1f1f1', relief='flat')

#grid positioning

main_screen.grid(row=0, column=0, rowspan=2, columnspan=4, sticky=('N', 'S','E', 'W'))

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