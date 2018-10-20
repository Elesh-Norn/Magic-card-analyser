# Magic cards analyser
Learning project to make a graphic interface for magic card analysis.

Aim of the project is to have a GUI and/or a web page, allowing us to do
various data visualisations on magic the gathering card information. I 
chooses those as a challenge, but as well because it's just nerdy and fun.

Aim of the project and advancement:

**Make a GUI interface**

I use Tkinter and the tutorial from https://pythonprogramming.net/tkinter-depth-tutorial-making-actual-program/

I'm able to set numerous graphs and button options, but not animate them
or refresh the graph for new info/data selection. Logic is distributed in
main and tkinter_logic file. *For now this part is in pause.*

*Example of the interface:*
![Exemple of the interface](https://i.imgur.com/gEgaCZQ.png)

**Data gathering and manipulation**

To get the information i need, i use the API from https://scryfall.com. 
They give back json that i can easily transform into DataFrame from pandas library.
Pandas allows easy data manipulation and is compatible with data visualisation tools, 
such as matplotlib or seaborn.

**Price history, Redis and Docker**

Magic the gathering second hand trading is pretty popular. People like to 
speculate on the price of cards and treat it as a stock market. It would 
be fun to design further my program to help visualising thoses prices 
variations and flux.

Scryfall refresh their price only once per day. To save thoses prices, 
i decided to use a Redis server which is pretty simple of utilisation.
Each card as a unique id which will be the key of a Redis hash, with time
and price as values. 

I need Redis to be online, and a script to pull the price regularly, 
without my input. This is a good occasion to learn Docker as well.

**Next step:** Docker compose! 
