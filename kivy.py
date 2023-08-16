from tkinter import *
import random


def main():
    # window
    window = Tk()
    window.geometry("1000x800")
    window.title("ROCK PAPER SCISSOR")
    icon = PhotoImage(file='pic\\icon.png')
    window.iconphoto(True, icon)
    window.resizable(False, False)
    
    # title
    title = Label(window, text="Rock Paper Scissor",
                  font=('Digiface', 40, 'normal'))
    title.pack()

    # resources

    # variables
    elements = ["ROCK", "PAPER", "SCISSOR"]

    # selection
    selection = Label(window, text="SETECT",
                      font=('Digiface', 20, 'normal'))
    selection.place(x=450, y=500)

    def select(str):
        run(str)

    # rock
    rock_img = PhotoImage(file='pic/rock.png')
    rock = Button(window, text="ROCK", font=('Digiface', 20, 'normal'),
                  image=rock_img, command=lambda: select("ROCK"), compound="top")

    # paper
    paper_img = PhotoImage(file='pic/paper.png')
    paper = Button(window, text="PAPER", font=('Digiface', 20, 'normal'),
                   image=paper_img, command=lambda: select("PAPER"), compound="top")

    # scissor
    scissor_img = PhotoImage(file='pic/scissor.png')
    scissor = Button(window, text="SCISSOR", font=(
        'Digiface', 20, 'normal'), image=scissor_img, command=lambda: select("SCISSOR"), compound="top")

    # selection menu
    rock.place(x=100, y=200)
    paper.place(x=400, y=200)
    scissor.place(x=700, y=200)

    # play

    def run(selectx):
        # selectx = selection.cget("text")
        # window recreate
        window.destroy()
        window1 = Tk()
        window1.geometry("1000x800")
        window1.title("ROCK PAPER SCISSOR")
        icon1 = PhotoImage(file='pic\\icon.png')
        window1.iconphoto(True, icon1)
        window1.resizable(False, False)

        item = random.choice(elements)

        path = str('pic\\'+selectx.lower()+'.png')
        img = PhotoImage(file=path)
        sel = Label(window1, text="YOU SELECTED: "+selectx, font=(
            'Digiface', 20, 'normal'), image=img, compound="top")
        sel.place(x=200, y=200)

        # pulled
        path = str('pic\\'+item.lower()+'.png')
        comp_img = PhotoImage(file=path)
        comp = Label(window1, text="COMPUTER SELECTED: "+item, font=(
            'Digiface', 20, 'normal'), image=comp_img, compound="top")
        comp.place(x=550, y=200)

        winner_label = Label(window1, text=win(selectx, item), font=(
            'Digiface', 20, 'normal'))
        winner_label.place(x=450, y=500)
        reset = Button(window1, text="RESET", font=(
            'Digiface', 20, 'normal'),  command=lambda: resetAll(window1))
        reset.place(x=450, y=700)

        window1.mainloop()
    # reset

    def resetAll(win):

        win.destroy()
        main()
    # win check

    def win(choice, pulled):
        if (choice == "ROCK" and pulled == "SCISSOR") or (choice == "SCISSOR" and pulled == "PAPER") or (choice == "PAPER" and pulled == "ROCK"):
            return "YOU WIN"
        elif (choice == pulled):
            return "IT'S A DRAW"
        else:
            return "YOU LOOSE"

    # gameloop
    window.mainloop()


main()
