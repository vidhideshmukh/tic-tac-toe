from tkinter import *
import tkinter.messagebox

root = tkinter.Tk()     #create a instance of TK() this is going to let us use T kenter's method

root.iconbitmap('C:\\Users\\user\\PycharmProjects\\j.a.r.v.i.s\\tic-tac-toe.ico')    #change the icon of window and put it our tictactoe icon

root.title('Tic-Tac-Toe')          #change the title of window

root.resizable(False, False)#it take 2 parameters one for width and one for height false means u cannot resize it

click = True

count = 0   #keep the track of how many moves have been made so in tictactoe we have 9 moves so if it already in 9th move it means it is tie.

# text variable are associated with widgets in tkinter inin our case we are going to associate these text variables
#with our buttonswe are going to create total 9 buttons so we are going to create a total of nine text variable
#so if we click on button number one we aregoing to set the text variable associated with button number one to X and so on .
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

#store image in the variables
xPhoto = PhotoImage(file='C:\\Users\\user\\PycharmProjects\\j.a.r.v.i.s\\X.png')
oPhoto = PhotoImage(file='C:\\Users\\user\\PycharmProjects\\j.a.r.v.i.s\\O.png')

#this play function contain the total 9 buttons that we need to play
def playtictaktoe():
    global xPhoto
    global oPhoto
    button1 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#f2e6ff', textvariable=btn1,
                     command=lambda: press(1, 0, 0)) #set height width and all prameter for buttons relief is for border
    #in ridge style bg is for background color textvariable is for type X or O so when user want to click buttons we want to
    #click buttons we want to something happen to do that we have to type command=lambda it allows us to call on a function on
    #press function same for all buttons.
    button1.grid(row=0, column=0) #location of buttons same for all

    button2 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#f2e6ff', textvariable=btn2,
                     command=lambda: press(2, 0, 1))
    button2.grid(row=0, column=1)

    button3 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#f2e6ff', textvariable=btn3,
                     command=lambda: press(3, 0, 2))
    button3.grid(row=0, column=2)

    button4 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#d9b3ff', textvariable=btn4,
                     command=lambda: press(4, 1, 0))
    button4.grid(row=1, column=0)

    button5 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#d9b3ff', textvariable=btn5,
                     command=lambda: press(5, 1, 1))
    button5.grid(row=1, column=1)

    button6 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#d9b3ff', textvariable=btn6,
                     command=lambda: press(6, 1, 2))
    button6.grid(row=1, column=2)

    button7 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#bf80ff', textvariable=btn7,
                     command=lambda: press(7, 2, 0))
    button7.grid(row=2, column=0)

    button8 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#bf80ff', textvariable=btn8,
                     command=lambda: press(8, 2, 1))
    button8.grid(row=2, column=1)

    button9 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#bf80ff', textvariable=btn9,
                     command=lambda: press(9, 2, 2))
    button9.grid(row=2, column=2)


def press(num, r, c):  #r for row and c for coloum
    global click, count
    if click == True:
        labelPhoto = Label(root, image=xPhoto) #lable class first parameter is name of our window and we want this lable
                                               #to have a particular image of x
        labelPhoto.grid(row=r, column=c)    #for the location of buttons and we used it here so we are placing this pic
                                            #in place of that button
        if num == 1:     #if num==1 the we set the text variable for that particular buttonin this case it would be
                        #button number one to X and doing for every button.
            btn1.set('X')
        elif num == 2:
            btn2.set('X')
        elif num == 3:
            btn3.set('X')
        elif num == 4:
            btn4.set('X')
        elif num == 5:
            btn5.set('X')
        elif num == 6:
            btn6.set('X')
        elif num == 7:
            btn7.set('X')
        elif num == 8:
            btn8.set('X')
        else:
            btn9.set('X')
        count += 1 #increse it becoz this point one move has been made
        click = False  # first is for x if it is true then it always print x only
        checkWin()

    else:
        labelPhoto = Label(root, image=oPhoto) # same as X we are here doing for O
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            btn1.set('O')
        elif num == 2:
            btn2.set('O')
        elif num == 3:
            btn3.set('O')
        elif num == 4:
            btn4.set('O')
        elif num == 5:
            btn5.set('O')
        elif num == 6:
            btn6.set('O')
        elif num == 7:
            btn7.set('O')
        elif num == 8:
            btn8.set('O')
        else:
            btn9.set('O')
        count += 1
        click = True  #turns go to X
        checkWin()

#check who won
def checkWin():
    global count, click

#if x wins
    if(btn1.get() == 'X' and btn2.get() == 'X' and btn3.get() == 'X' or
            btn4.get() == 'X' and btn5.get() == 'X' and btn6.get() == 'X' or
            btn7.get() == 'X' and btn8.get() == 'X' and btn9.get() == 'X' or
            btn1.get() == 'X' and btn4.get() == 'X' and btn7.get() == 'X' or
            btn2.get() == 'X' and btn5.get() == 'X' and btn8.get() == 'X' or
            btn3.get() == 'X' and btn6.get() == 'X' and btn9.get() == 'X' or
            btn1.get() == 'X' and btn5.get() == 'X' and btn9.get() == 'X' or
            btn3.get() == 'X' and btn5.get() == 'X' and btn7.get() == 'X'):

        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'X Wins !')
        click = True
        count = 0
        clear()
        playtictaktoe()

#if o wins
    elif (btn1.get() == 'O' and btn2.get() == 'O' and btn3.get() == 'O' or
          btn4.get() == 'O' and btn5.get() == 'O' and btn6.get() == 'O' or
          btn7.get() == 'O' and btn8.get() == 'O' and btn9.get() == 'O' or
          btn1.get() == 'O' and btn4.get() == 'O' and btn7.get() == 'O' or
          btn2.get() == 'O' and btn5.get() == 'O' and btn8.get() == 'O' or
          btn3.get() == 'O' and btn6.get() == 'O' and btn9.get() == 'O' or
          btn1.get() == 'O' and btn5.get() == 'O' and btn9.get() == 'O' or
          btn3.get() == 'O' and btn5.get() == 'O' and btn7.get() == 'O'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'O Wins !')
        count = 0
        clear()
        playtictaktoe()

    elif (count == 9):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'Tie Game!')
        click = True
        count = 0
        clear()
        playtictaktoe()

#for clearing the game for next play
def clear():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')


playtictaktoe()

root.mainloop()     #first method of t kenter's it is an event handler it's looking outfor events like the click of a button