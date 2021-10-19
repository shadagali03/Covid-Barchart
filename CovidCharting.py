import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

#Create data frame
df = pd.read_csv("DeathsCovid.csv", usecols=["Entity","Date","Total Deaths","Numbers"])

#Create Dictionary
li = []
li = df.Date.unique()
dateDict = {}
i = 0
for x in li:
    dateDict[i] = x
    i += 1

#Draw BarChart Function
def draw_barchart(year):
    value = dateDict[year]
    newDf = df[df['Date'].eq(value)].sort_values(by="Total Deaths", ascending=True).tail(10)
    ax.clear()
    ax.barh(newDf["Entity"],newDf["Total Deaths"])
    dx = newDf["Total Deaths"].max() / 200
    for i, (deaths, country) in enumerate(zip(newDf["Total Deaths"], newDf["Entity"])):
        ax.text(deaths-dx, i, country,size = 14, weight = 600, ha="right", va="bottom")
        ax.text(deaths+dx, i, f'{deaths:,.0f}',size=14, ha="left", va="center")
    ax.text(1,.24,value,transform=ax.transAxes, color = '#666666',size = 36, ha = "right", weight = 800)
    ax.text(0,1.06,"Deaths", transform = ax.transAxes, size = 12, color = '#666666')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis="x", colors = '#666666',labelsize = 12)
    ax.set_yticks([])
    ax.margins(0,.01)
    ax.grid(which="major",axis="x",linestyle="-")
    ax.set_axisbelow(True)
    ax.text(0,1.12,"Covid-19 Deaths per Country Over Time",transform=ax.transAxes,size = 24, 
            weight = 600, ha="left")
    
#Animation
fig, ax = plt.subplots(figsize=(15,8))
animator = FuncAnimation(fig, draw_barchart, frames=range(0,106))
HTML(animator.to_jshtml())
plt.show()