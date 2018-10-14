import tkinter as tk
from tkinter import ttk
import tkinter_logic
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import card_fetcher
import Graph_functions

# GLOBALS

LARGE_FONT = ("Verdana", 12)


def draw_canvas(self, function):
    canvas = FigureCanvasTkAgg(function, self)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2TkAgg(canvas, self)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class The_app(tk.Tk):

    def __init__(self, *args, **kwargs):
        # Inherited class init
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="fox_icon.ico")
        tk.Tk.wm_title(self, "MagicApp")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary of different frames
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)
            self.frames[F] = frame
            # Place the frame object on the grid.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Starting Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text='Pie Plot',
                             command=lambda: controller.show_frame(
                                PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text='Boxplot',
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        # Testing purposes
        # Graph_functions.pie_graph(tkinter_logic.MANIPULABLE_DATAFRAME, "rarity")
        canvas = FigureCanvasTkAgg(Graph_functions.price_lineplot("5314bae2-4930-4f8a-8a52-853bc3feb88f",
                                                                  card_fetcher.get_all_standard()), self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        button = tkinter_logic.Switch_set_button("Magic Core set 2019", 'm19')
        button.pack()
        button2 = ttk.Button(self, text="Destroy",
                             command=lambda: canvas.get_tk_widget().destroy())
        button2.pack()

        button3 = ttk.Button(self, text="Draw",
                             command=lambda: draw_canvas(self, Graph_functions.
                                                         pie_graph(tkinter_logic.MANIPULABLE_DATAFRAME, "rarity")))
        button3.pack()

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(
                                 StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(Graph_functions.swarmplot(tkinter_logic.MANIPULABLE_DATAFRAME, "rarity", "usd"), self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        button2 = ttk.Button(self, text="Destroy",
                             command=lambda:canvas.get_tk_widget().destroy())
        button2.pack()

        button3 = ttk.Button(self, text="Draw",
                             command=lambda: draw_canvas(self, Graph_functions.swarmplot(tkinter_logic.MANIPULABLE_DATAFRAME, "rarity", "usd")))
        button3.pack()



app = The_app()
app.mainloop()
