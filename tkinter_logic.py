import card_fetcher
from tkinter import ttk
import pandas as pd

ALL_STANDARD_DATAFRAME = card_fetcher.get_all_standard()
MANIPULABLE_DATAFRAME = ALL_STANDARD_DATAFRAME

class Switch_set_button(ttk.Button):

    def __init__(self, set_text, set_code):
        self.flag = "ON"
        self.set_text = set_text
        self.set_code = set_code
        ttk.Button.__init__(self, text= " (-) "+ self.set_text,
                   command=lambda:Switch_set_button.invert(self))

    def invert(self):
        global MANIPULABLE_DATAFRAME
        if self.flag == "ON":
            self.flag = "OFF"
            self['text'] = " (+) "+ self.set_text
            MANIPULABLE_DATAFRAME = MANIPULABLE_DATAFRAME[
                MANIPULABLE_DATAFRAME.set != self.set_code]
            print(MANIPULABLE_DATAFRAME.info())
        else:
            self.flag = "ON"
            self['text'] = " (-) "+ self.set_text
            MANIPULABLE_DATAFRAME = pd.concat([MANIPULABLE_DATAFRAME,
                                               ALL_STANDARD_DATAFRAME[
                                                   ALL_STANDARD_DATAFRAME.set == self.set_code]])
            print(MANIPULABLE_DATAFRAME.info())
