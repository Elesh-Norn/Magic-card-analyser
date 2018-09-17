import seaborn as sns
import matplotlib.pyplot as plt

def swarmplot(data, category, y, figure):
    sns.boxplot(x=category, y=y, data=data, ax=figure)
    sns.swarmplot(x=category, y=y, data=data, ax=figure, color='k')


def pie_graph(data, category):

    data = data[category].value_counts()
    total = sum(data.tolist())

    # plt.Circle((0, 0), 0.7, color='white')
    plt.pie(data.tolist(), labels=data.index.tolist(), autopct=lambda p: '{:.0f}'.format(p * total / 100),
            wedgeprops={'linewidth': 7, 'edgecolor': 'white'}, pctdistance=0.85)
    plt.title("Repartition of "+str(category))

    p = plt.gcf()

    return p

def lineplot(x, y):
    sns.lineplot(x=x, y=y)