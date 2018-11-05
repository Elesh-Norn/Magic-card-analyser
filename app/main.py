import tkinter as tk
from tkinter import ttk
from app import tkinter_logic
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from app import card_fetcher
from app import Graph_functions

# GLOBALS

LARGE_FONT = ("Verdana", 12)

def draw_canvas(self, function, object):
    canvas = FigureCanvasTkAgg(function, self)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    object.canvas = canvas


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

        for F in ([StartPage]):

            frame = F(container, self)
            self.frames[F] = frame
            # Place the frame object on the grid.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Graph_object:

    def __init__(self):
       pass


    def line(self):
        return Graph_functions.price_lineplot("5314bae2-4930-4f8a-8a52-853bc3feb88f",
                                                   card_fetcher.get_all_standard())

    def pieplot(self):
         return Graph_functions.pie_graph(tkinter_logic.MANIPULABLE_DATAFRAME, "rarity")


    def swarmplot(self):
        return Graph_functions.swarmplot(tkinter_logic.MANIPULABLE_DATAFRAME, "rarity", "usd")

    def set_active_canvas(self, canvas):
        self.canvas = canvas


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        graph_object = Graph_object()

        pie_plot_button = ttk.Button(self, text='Pie Plot',
                             command=lambda: draw_canvas(self, graph_object.pieplot(), graph_object))
        pie_plot_button.pack()

        boxplot_button = ttk.Button(self, text='Boxplot',
                             command=lambda: draw_canvas(self, graph_object.swarmplot(), graph_object))
        boxplot_button.pack()

        line_button = ttk.Button(self, text='Boxplot',
                                    command=lambda: draw_canvas(self, graph_object.line(), graph_object))
        line_button.pack()

        destroy2_button = ttk.Button(self, text="Destroy 2",
                                    command=lambda: graph_object.canvas.get_tk_widget().destroy())
        destroy2_button.pack()




app = The_app()
app.mainloop()
