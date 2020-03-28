import tkinter as tki



calc = tki.Tk()
calc.title('Calculadora Básica')


# Cria os botões da calculadora

visor = tki.Entry(calc,
                  text = 'TESTANDO',
                  fg = '#000000',
                  background = 'grey',
                  justify = 'center')

def logics(botao): #identifica o botao e realiza a logica da calc

    visor.insert(0,botao)

    return

b1 = tki.Button(calc,
                text = '1',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('1'))

b2 = tki.Button(calc,
                text = '2',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('2'))

b3 = tki.Button(calc,
                text = '3',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('3'))

b4 = tki.Button(calc,
                text = '4',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('4'))

b5 = tki.Button(calc,
                text = '5',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('5'))

b6 = tki.Button(calc,
                text = '6',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('6'))

b7 = tki.Button(calc,
                text = '7',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('7'))

b8 = tki.Button(calc,
                text = '8',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('8'))

b9 = tki.Button(calc,
                text = '9',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('9'))

b0 = tki.Button(calc,
                text = '0',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('0'))

bplus = tki.Button(calc,
                text = '+',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('+'))

bminus = tki.Button(calc,
                text = '-',
                fg = '#000000',
                relief = 'solid',
                padx = 34,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('-'))

bmult = tki.Button(calc,
                text = 'x',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('x'))

bdiv = tki.Button(calc,
                text = ':',
                fg = '#000000',
                relief = 'solid',
                padx = 34,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics(':'))

bdot = tki.Button(calc,
                text = '.',
                fg = '#000000',
                relief = 'solid',
                padx = 34,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('.'))

bequal = tki.Button(calc,
                text = '=',
                fg = '#000000',
                relief = 'solid',
                padx = 30,
                pady = 20,
                font = ('Helvetica','30', 'bold'),
                command = logics('='))



# Posiciona os botões

b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)
b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)
b7.grid(row = 1, column = 0)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 2)
b0.grid(row = 4, column = 1)
bplus.grid(row = 1, column = 4)
bminus.grid(row = 2, column = 4)
bmult.grid(row = 3, column = 4)
bdiv.grid(row = 4, column = 4)
bequal.grid(row = 4, column = 2)
bdot.grid(row = 4, column = 0)
visor.grid(row = 0, column = 0, columnspan = 5)


calc.mainloop()




