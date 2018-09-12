import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from card_fetcher import get_set

# GLOBALS
LARGE_FONT = ("Verdana", 12)


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

        button = ttk.Button(self, text='Visit Page 1',
                           command = lambda: controller.show_frame(
                               PageOne))
        button.pack()

        button2 = ttk.Button(self, text='Visit Page 2',
                            command=lambda: controller.show_frame(
                                PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text='Gimme the graph shit',
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
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(
                                 StartPage))
        button1.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        ax1 = f.add_subplot(111)
        df = get_set('m19')
        sns.boxplot(x='rarity', y='usd', data=df, ax=ax1)
        sns.swarmplot(x='rarity', y='usd', data=df, ax=ax1, color='k')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = The_app()
app.mainloop()
