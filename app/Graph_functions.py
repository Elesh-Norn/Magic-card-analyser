import seaborn as sns
import matplotlib.pyplot as plt

def swarmplot(data, category, y):
    """
    Plot x against y, boxplot+swarplot, y must be continuous
    return a matplotlib figure object
    """

    fig, ax = plt.subplots()
    sns.boxplot(x=category, y=y, data=data, ax=ax)
    sns.swarmplot(x=category, y=y, data=data, ax=ax, color='k')

    return fig

def pie_graph(data, category):
    """
    Make a donut pie graph from a repartition of values
    return a matplotlib figure object
    """

    # Count Data
    data = data[category].value_counts()
    total = sum(data.tolist())

    # Graph part
    plt.pie(data.tolist(), labels=data.index.tolist(), autopct=lambda p: '{:.0f}'.format(p * total / 100),
            wedgeprops={'linewidth': 7, 'edgecolor': 'white'}, pctdistance=0.85)
    fig = plt.gcf()
    ax = plt.gca()
    ax.set_title("Repartition of "+str(category))
    ax.add_artist(plt.Circle((0, 0), 0.7, color='white'))

    return fig


from app.redis_price_server import get_price_list_from_redis


def price_lineplot(card_id, df):
    """in construction"""

    fig, ax = plt.subplots()
    df_price =(get_price_list_from_redis(card_id))
    sns.lineplot(x=df_price.index, y=df_price['price'], ax=ax)
    ax.set_title(df.loc[df['id'] == card_id]['name'].values[0])
    return fig
