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
        self.line = Graph_functions.price_lineplot("5314bae2-4930-4f8a-8a52-853bc3feb88f",
                                                   card_fetcher.get_all_standard())
        self.pieplot = Graph_functions.pie_graph(tkinter_logic.MANIPULABLE_DATAFRAME, "rarity")

        self.swarmplot = Graph_functions.swarmplot(tkinter_logic.MANIPULABLE_DATAFRAME, "rarity", "usd")


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        graph_object = Graph_object()

        pie_plot_button = ttk.Button(self, text='Pie Plot',
                             command=lambda: draw_canvas(self, graph_object.pieplot))
        pie_plot_button.pack()

        boxplot_button = ttk.Button(self, text='Boxplot',
                             command=lambda: draw_canvas(self, graph_object.swarmplot))
        boxplot_button.pack()

        canvas = FigureCanvasTkAgg(Graph_functions.price_lineplot("5314bae2-4930-4f8a-8a52-853bc3feb88f",
                                                                  card_fetcher.get_all_standard()), self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        destroy_button = ttk.Button(self, text="Destroy",
                             command=lambda: canvas.get_tk_widget().destroy())
        destroy_button.pack()




app = The_app()
app.mainloop()
