from tkinter import *
from tkinter.ttk import *
window = Tk()
window.geometry('500x450')
window.title('Cinema')

def movie_info():
    get_info = txtMovies.get()

lblmovie = Label(window, text='Choose a movie: ')
lblmovie.grid(column= 0, row= 0)
txtMovies = Entry(window, width= 12)
txtMovies.grid(column=0, row=1)

btnMovieInfo = Button(window, text= 'Movie Info')
btnMovieInfo.grid(column=1, row=1)


cbMovies = Combobox(window)
cbMovies['values'] = ['One piece film red', 'Black Panther', 'Avatar 2']

lblTickets = Label(window, text= 'Number of tickets: ')
lblTickets.grid(column= 0, row= 3)
txtTickets = Entry(window, width= 12)
txtTickets.grid(column= 0, row= 4)

btnBuy = Button(window, text= 'Purchase')
btnBuy.grid(column=0, row=5)

window.mainloop()